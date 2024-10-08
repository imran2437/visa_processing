from odoo import models, fields, api



class VisaAppointment(models.Model):
    _name = 'visa.appointment'
    _description = 'Visa Appointment'

    applicant_id = fields.Many2one('res.partner', string='Applicant', required=True)
    visa_application_id = fields.Many2one('visa.application', string='Visa Application', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    location = fields.Char(string='Appointment Location')
    notes = fields.Text(string='Additional Notes')

    # Action method
    def action_confirm_appointment(self):
        self.write({'confirmed': True})


class VisaApplication(models.Model):
    _name = 'visa.application'
    _description = 'Visa Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(string='Application Number', required=True, copy=False, readonly=True, default='New')
    applicant_id = fields.Many2one('res.partner', string='Applicant', required=True)
    agent_id = fields.Many2one('res.partner', string='Agent', help='The agent submitting on behalf of the applicant')
    visa_type = fields.Selection([
        ('tourist', 'Tourist Visa'),
        ('business', 'Business Visa'),
        ('student', 'Student Visa'),
        ('work', 'Work Visa'),
        ('family', 'Family Visa'),
        ('permanent_residency', 'Permanent Residency'),
        ('other', 'Other')
    ], string='Visa Type', required=True, tracking=True)
    country_id = fields.Many2one('res.country', string='Destination Country', required=True)
    processing_stage_id = fields.Many2one('visa.processing.stage', string='Processing Stage', tracking=True)
    document_ids = fields.One2many('visa.document', 'visa_application_id', string='Documents')
    communication_ids = fields.One2many('visa.communication', 'visa_application_id', string='Communications')
    payment_ids = fields.One2many('visa.payment', 'visa_application_id', string='Payments')
    fee_amount = fields.Float(string='Application Fee', required=True, default=0.0)
    payment_status = fields.Selection([('not_paid', 'Not Paid'), ('paid', 'Paid'), ('failed', 'Payment Failed')], string='Payment Status', default='not_paid', tracking=True)
    status = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft', tracking=True)
    application_date = fields.Date(string='Application Date', default=fields.Date.today())
    approval_date = fields.Date(string='Approval Date')
    rejection_reason = fields.Text(string='Rejection Reason')
    notes = fields.Text(string='Additional Notes')
    applicant_age = fields.Integer(string='Applicant Age')

    # Action methods
    def action_submit(self):
        self.write({'status': 'submitted', 'processing_stage_id': self.env.ref('visa_processing.stage_under_review').id})

    def action_approve(self):
        self.write({'status': 'approved', 'approval_date': fields.Date.today(), 'processing_stage_id': self.env.ref('visa_processing.stage_approved').id})

    def action_reject(self, reason):
        self.write({'status': 'rejected', 'rejection_reason': reason, 'processing_stage_id': self.env.ref('visa_processing.stage_rejected').id})

    def action_request_more_documents(self, document_type):
        # Logic to request additional documents from the applicant
        pass

    # Compute method
    # @api.depends('applicant_id.birthdate_date')
    # def _compute_applicant_age(self):
    #     for record in self:
    #         if record.applicant_id and record.applicant_id.birthdate_date:
    #             record.applicant_age = fields.Date.today().year - record.applicant_id.birthdate_date.year
    #         else:
    #             record.applicant_age = 0

    # Override create method
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('visa.application') or 'New'
        return super(VisaApplication, self).create(vals)



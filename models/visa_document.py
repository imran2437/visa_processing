from odoo import models, fields, api


class VisaDocument(models.Model):
    _name = 'visa.document'
    _description = 'Visa Application Document'

    name = fields.Char(string='Document Name', required=True)
    visa_application_id = fields.Many2one('visa.application', string='Visa Application', required=True, ondelete='cascade')
    document_type = fields.Selection([
        ('passport', 'Passport'),
        ('photo', 'Photo'),
        ('visa_form', 'Visa Form'),
        ('medical_report', 'Medical Report'),
        ('financial_statement', 'Financial Statement'),
        ('travel_itinerary', 'Travel Itinerary'),
        ('other', 'Other')
    ], string='Document Type', required=True)
    document_file = fields.Binary(string='Document File', required=True)
    upload_date = fields.Datetime(string='Uploaded On', default=fields.Datetime.now)
    verified = fields.Boolean(string='Verified', default=False)
    remarks = fields.Text(string='Remarks')

    # Action method
    def action_mark_as_verified(self):
        self.write({'verified': True})
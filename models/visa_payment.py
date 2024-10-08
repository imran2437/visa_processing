from odoo import models, fields, api


class VisaPayment(models.Model):
    _name = 'visa.payment'
    _description = 'Visa Payment Information'

    visa_application_id = fields.Many2one('visa.application', string='Visa Application', required=True, ondelete='cascade')
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', default=fields.Date.today())
    payment_method = fields.Selection([('paypal', 'PayPal'), ('stripe', 'Stripe'), ('bank', 'Bank Transfer')], string='Payment Method', required=True)
    status = fields.Selection([('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], string='Payment Status', default='pending')
    transaction_id = fields.Char(string='Transaction ID')

    # Action method
    def mark_as_paid(self):
        self.write({'status': 'completed', 'payment_date': fields.Date.today()})
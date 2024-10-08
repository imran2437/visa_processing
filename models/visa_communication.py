from odoo import models, fields, api

class VisaCommunication(models.Model):
    _name = 'visa.communication'
    _description = 'Visa Application Communication Log'

    visa_application_id = fields.Many2one('visa.application', string='Visa Application', required=True, ondelete='cascade')
    message = fields.Text(string='Message', required=True)
    author_id = fields.Many2one('res.partner', string='Author', required=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    document_id = fields.Many2one('visa.document', string='Linked Document')
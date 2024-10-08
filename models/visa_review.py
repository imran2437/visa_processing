from odoo import models, fields, api

class VisaReview(models.Model):
    _name = 'visa.review'
    _description = 'Visa Application Review'

    visa_application_id = fields.Many2one('visa.application', string='Visa Application', required=True, ondelete='cascade')
    reviewer_id = fields.Many2one('res.partner', string='Reviewer', required=True)
    review_date = fields.Datetime(string='Review Date', default=fields.Datetime.now)
    review_outcome = fields.Selection([('pass', 'Pass'), ('fail', 'Fail'), ('pending', 'Pending')], string='Outcome', required=True)
    comments = fields.Text(string='Comments')
from odoo import models, fields, api

class VisaInterview(models.Model):
    _name = 'visa.interview'
    _description = 'Visa Interview'

    applicant_id = fields.Many2one('res.partner', string='Applicant', required=True)
    visa_application_id = fields.Many2one('visa.application', string='Visa Application', required=True)
    interview_date = fields.Datetime(string='Interview Date', required=True)
    interview_location = fields.Char(string='Location')
    interview_outcome = fields.Selection([('pass', 'Pass'), ('fail', 'Fail'), ('pending', 'Pending')], string='Outcome')
    comments = fields.Text(string='Comments')
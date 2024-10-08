from odoo import models, fields, api


class VisaApplicationChecklist(models.Model):
    _name = 'visa.application.checklist'
    _description = 'Visa Application Checklist'

    visa_type = fields.Selection([
        ('tourist', 'Tourist Visa'),
        ('business', 'Business Visa'),
        ('student', 'Student Visa'),
        ('work', 'Work Visa')
    ], string='Visa Type', required=True)
    document_ids = fields.One2many('visa.document.checklist', 'checklist_id', string='Required Documents')
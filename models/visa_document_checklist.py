from odoo import models, fields, api



class VisaDocumentChecklist(models.Model):
    _name = 'visa.document.checklist'
    _description = 'Visa Document Checklist'

    checklist_id = fields.Many2one('visa.application.checklist', string='Checklist', required=True, ondelete='cascade')
    document_type = fields.Selection([
        ('passport', 'Passport'),
        ('photo', 'Photo'),
        ('visa_form', 'Visa Form'),
        ('medical_report', 'Medical Report'),
        ('financial_statement', 'Financial Statement'),
        ('travel_itinerary', 'Travel Itinerary'),
        ('other', 'Other')
    ], string='Document Type', required=True)
    mandatory = fields.Boolean(string='Mandatory', default=True)
    description = fields.Text(string='Description')
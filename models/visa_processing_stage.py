# -*- coding: utf-8 -*-
from odoo import models, fields, api


class VisaProcessingStage(models.Model):
    _name = 'visa.processing.stage'
    _description = 'Visa Processing Stage'
    _order = 'sequence'

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    is_final_stage = fields.Boolean(string='Final Stage', default=False)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_unique', 'unique (name)', 'The stage name must be unique!')
    ]

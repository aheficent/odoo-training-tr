# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import timedelta


class CertificationWizard(models.TransientModel):
    _name = 'certification.wizard'

    date = fields.Date(string='Expiration Date')
    entity_id = fields.Many2one('res.partner', string='Certification Entity')
    is_entity = fields.Boolean(string="Is Valid Entity", readonly=True)
    certification_count = fields.Integer(string="# Certifications", readonly=True)

    @api.multi
    def certification_entity_date_valid(self):
        self.ensure_one()  # Recordset must contain only 1 record
        action = self.env.ref('certification.certification')  # act windows defined in views
        result = action.read()[0]  # After reference an action we always do
        if not result.get('domain', False):  # if domain key doesn’t exist
            result['domain'] = []  # We create them
        if self.entity_id:  # If we have marked a Certification entity
            result['domain'] += [('entity_id', '=', self.entity_id.id)]  # Filter by that entity
        if self.date:  # If we have select a date
            result['domain'] += [('date', '>=', self.date)]  # Date bigger than selected
        return result

    @api.onchange('entity_id', 'date')
    def onchange_entity_date(self):
        if self.entity_id:
            domain = [('entity_id', '=', self.entity_id.id)]
            if self.date:
                domain += [('date', '>=', self.date)]
            certification_model = self.env['certification']
            certification_ids = certification_model.search(domain)
            self.certification_count = len(certification_ids)
        else:
            self.certification_count = 0

    @api.onchange('entity_id')
    def onchange_entity_id(self):
        self.is_entity = self.entity_id.is_certification_body

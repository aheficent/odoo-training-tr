# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class Certification(models.Model):
    _name = 'certification'
    _description = 'Certification'

    number = fields.Char(required=True)
    date = fields.Date(string='Validation Date', required=True)
    description = fields.Text(string='Validation Details')
    standard_id = fields.Many2one('certification.standard', required=True)
    owner_id = fields.Many2one("res.partner", required=True)
    entity_id = fields.Many2one('res.partner', required=True)
    expiry_days = fields.Integer('Expiry Days', compute='_compute_expiry_days',
                                 readonly=True)
    expiry_status = fields.Selection([
        ('expired', 'Expired'),
        ('available', 'Available')], readonly=True, compute='_compute_expiry_days', store=True
    )

    @api.constrains('entity_id')
    def _check_entity_id(self):
        if self.entity_id and self.entity_id.is_certification_body == False:
            raise ValidationError('This partner is not an entity')

    @api.depends('date')
    def _compute_expiry_days(self):
        if self.date:
            self.expiry_days = (self.date - fields.Date.today()).days
            if self.expiry_days > 0:
                self.expiry_status = 'available'
            else:
                self.expiry_status = 'expired'

    # Actualitzar registre - diferents maneres
    # @api.multi
    # def update_date_one_month(self):
    #     self.ensure_one()
    #     if self.date:
    #         self.date += timedelta(days=30)

    @api.multi
    def update_date_one_month(self):
        self.ensure_one()
        if self.date:
            self.write({'date': self.date + timedelta(days=30)})

    # @api.multi
    # def update_date_one_month(self):
    #     self.ensure_one()
    #     if self.date:
    #         self.update({'date': self.date + timedelta(days=30)})


class PartnerCertificationStatus(models.Model):
    _name = 'partner.certification.status'
    _description = 'Partner Certification Status'

    name = fields.Char(string="Status", required=True)
    description = fields.Text(required=True)


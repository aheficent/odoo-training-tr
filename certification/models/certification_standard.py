# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class CertificationStandard(models.Model):

    _name = 'certification.standard'
    _description = 'Certification Types'

    name = fields.Char(required=True)
    description = fields.Text()

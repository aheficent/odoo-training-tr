# Copyright 2019 Patrick Wilson <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # certification_ids = fields.One2many(comodel_name='certification',
    #                                     inverse_name='owner_id')
    certification_ids = fields.One2many(comodel_name='certification', inverse_name='owner_id')
    is_certification_body = fields.Boolean(string='It is an entity', default='True',
                                           help='Check this box if the contact is a certification entity')











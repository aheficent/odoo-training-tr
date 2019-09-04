from odoo import fields,models


class ResPartner (models.Model):
    _inherit = 'res.partner'

    employee_ids = fields.One2many(comodel_name='identification.documents', inverse_name='employee_id')

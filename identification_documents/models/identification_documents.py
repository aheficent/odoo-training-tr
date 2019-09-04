from odoo.exceptions import UserError
from odoo import fields,models,api


class Identification(models.Model):
    _name = "identification.documents"

    employee_id = fields.Many2one('res.partner')
    number = fields.Char()
    type = fields.Selection([
        ('passport', 'Passport'),
        ('card', 'ID Card'),
        ('driving', 'Driving License')
    ])
    date = fields.Date()

    @api.constrains('number')
    def check_number(self):
        if self.number == ' ':
            msg = 'Empty field'
            raise UserError(msg)
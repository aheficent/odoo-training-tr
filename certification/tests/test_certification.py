
# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>).
# Copyright 2016 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestCertification(TransactionCase):
    def setUp(self):
        super(TestCertification, self).setUp()
        self.res_partner = self.env['res.partner']
        self.partner = self.res_partner.create({
            'name': "test1",
            'email': "test@test.com"})

    def test_certification(self):
        """ Test expiry status of the certification"""
        certification = self.env['certification'].create({
            'number': 'AAA',
            'date': '2025-12-31'})
        self.assertEqual(certification.expiry_status, 'available')

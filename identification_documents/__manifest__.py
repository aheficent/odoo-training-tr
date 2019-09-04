# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Identity Documents',
    'summary': "Shows the identification documents of each employee.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/<my_github_user>",
    'category': 'Identification documents',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base',
                'contacts'],
    'data': ['security/ir.model.access.csv',
             'views/identification_view.xml',
             'views/res_partner.xml'
             ],
    'development_status': 'Beta',
    'maintainers': ['ceeficent'],
}
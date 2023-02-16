# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Albin P J (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
{
    'name': 'Certificates And Licenses With Expiry Management',
    'version': '16.0.1.0.0',
    'summary': """Certificates And Licenses With Expiry Management""",
    'description': """Certificates And Licenses With Expiry Management""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'project', 'contacts', 'website', 'mail', 'portal', 'product'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/certificates_licenses_menus.xml',
        'views/certificates_views.xml',
        'views/licences_views.xml',
        'views/certificates_portal.xml',
        'views/res_partner_certificates_licences.xml',
        'views/licences_portal.xml',
        'views/certificates_search.xml',
        'views/licences_search.xml',
        'data/certificate_number.xml',
        'data/certificate_licence_sheduled_action.xml',
        'data/certificate_email_template.xml',
        'data/certificates_licences_types.xml',
        'data/certificates_licences_tags.xml',
        'data/licence_email_template.xml',
        'report/certificate_licence_report.xml',
        'report/certificate_template.xml',
        'report/licence_template.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'certificates_licenses_expiry/static/src/css/certificate_licence.css',

        ],
        'web.assets_frontend': [
            'certificates_licenses_expiry/static/src/js/certificates_search.js',
            'certificates_licenses_expiry/static/src/js/licences_search.js',
            'certificates_licenses_expiry/static/src/js/certificates_group_by.js',
            'certificates_licenses_expiry/static/src/js/licences_group_by.js',
        ],
    },
    'license': 'LGPL-3',
    'price': 2900,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}

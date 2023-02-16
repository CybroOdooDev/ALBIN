"""This is user for licences portal tree and form templates"""
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

from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal


class MyLicences(http.Controller):
    """It returns the login person"""

    def _get_tickets_domain(self):
        """It returns the login person"""
        return [('customer_id', '=', request.env.user.partner_id.id)]

    @http.route(['/my/licences'], type='http', auth="user", website=True)
    def get_my_licences(self):
        """Take values from licences and render to portal tree template """
        domain = self._get_tickets_domain()
        licences = request.env['licences'].sudo().search(domain)
        values = {'licences': licences,
                  }

        return request.render("certificates_licenses_expiry.portal_my_licences", values)

    @http.route(['/my/licences/form/<int:lic_id>'], type='http', auth="user", website=True)
    def get_my_licences_form(self, lic_id):
        """Take values from licences and render to portal form template.It also passes the id in the root for
               rendering the corresponding form template"""
        licences = request.env['licences'].sudo().search([('id', '=', lic_id)])
        values = {
            'my_licences': licences,
        }
        return request.render("certificates_licenses_expiry.licences_portal_form_template", values)


class Return(portal.CustomerPortal):
    """This will take the count of total licences"""
    def _prepare_home_portal_values(self, counters):
        """This will return the licences count"""
        values = super(Return, self)._prepare_home_portal_values(counters)
        licences = request.env['licences'].search([('customer_id', '=', request.env.user.partner_id.id)])
        count = len(licences)
        values.update({
            'licences': count
        })
        return values

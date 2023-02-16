"""This is used to group by on portal tree for licences"""
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


class LicencesGroupBy(http.Controller):
    """This is used to licences group by in tree view"""

    @http.route(['/licencesgroupby'], type='json', auth="public", website=True)
    def licences_group_by(self, **kwargs):
        """Call from rpc for group by, and it returns the corresponding values"""
        context = []
        group_value = kwargs.get("search_value")
        if group_value == '1':
            context = []
            type_ids = request.env['licences.types'].search([])
            for types in type_ids:
                licences_ids = request.env['licences'].search([
                    ('licences_types_id', '=', types.id), ('customer_id', '=', request.env.user.partner_id.id)
                ])
                if licences_ids:
                    context.append({
                        'name': types.licence_type,
                        'data': licences_ids
                    })
        if group_value == '2':
            context = []
            tag_ids = request.env['licences.tags'].search([])
            for tags in tag_ids:
                licences_ids = request.env['licences'].search([
                    ('licences_tags', '=', tags.id), ('customer_id', '=', request.env.user.partner_id.id)
                ])
                if licences_ids:
                    context.append({
                        'name': tags.licence_tags,
                        'data': licences_ids
                    })

        values = {
            'licences': context,
        }

        response = http.Response(template='certificates_licenses_expiry.licences_group_by_template',
                                 qcontext=values)
        return response.render()

"""This will give certificate and licence count of corresponding partners"""
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
from odoo import models, api, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    certificates_count = fields.Char(compute='total_certificates_count')
    licences_count = fields.Char(compute='total_licences_count')

    @api.depends('certificates_count')
    def total_certificates_count(self):
        """We can get the count of certificates"""
        for record in self:
            record.certificates_count = self.env[
                'certificates'].search_count([('customer_id', '=', self.id)])

    @api.depends('licences_count')
    def total_licences_count(self):
        """We can get the count of licences"""
        for record in self:
            record.licences_count = self.env[
                'licences'].search_count([('customer_id', '=', self.id)])

    def show_certificates(self):
        """We can see the certificate in tree and form view"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Certificates',
            'view_mode': 'tree,form',
            'res_model': 'certificates',
            'domain': [('customer_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def show_licences(self):
        """We can see the certificate in tree and form view"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Licences',
            'view_mode': 'tree,form',
            'res_model': 'licences',
            'domain': [('customer_id', '=', self.id)],
            'context': "{'create': False}"
        }

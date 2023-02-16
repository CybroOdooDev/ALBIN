"""This is for licence model"""
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
from datetime import date
from random import randint

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Licences(models.Model):
    """This will give all about licences such as fields etc"""
    _name = 'licences'
    _description = "Licences"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    state = fields.Selection(
        selection=[('new', 'New'), ('active', 'Active'), ('expired_soon', 'Expired Soon'), ('expired', 'Expired')],
        string="State", default='new')
    name = fields.Char(string='Name', required=True)
    licence_number = fields.Char(string="Certificate Number", readonly=True, required=True, copy=False,
                                 default='New')
    customer_id = fields.Many2one('res.partner', string="Customer", required=True)
    licences_types_id = fields.Many2one('licences.types', string="Licences Types", required=True)
    start_date = fields.Date(string="Start Date", required=True, default=date.today())
    expire_date = fields.Date(string="Expire Date", required=True, default=date.today())
    issued_by_id = fields.Many2one('res.company', string="Issued By", required=True)
    licences_tags = fields.Many2many('licences.tags', string="Tags")
    project_id = fields.Many2one('project.project', string="Project", required=True)
    task_id = fields.Many2one('project.task', string="Task", domain="[('project_id', '=', project_id)]", required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    user_id = fields.Many2one('res.users', string="Responsible User", required=True, default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', string="Company", required=True, default=lambda self: self.env.company,
                                 readonly=True)
    expire_remainder_day = fields.Integer(string="Expire Remainder Day")
    login_user_id = fields.Many2one('res.users', string='Login User', default=lambda self: self.env.user, readonly=True)
    internal_notes = fields.Text(string="Internal Notes")
    description = fields.Text(string="Description")
    achievements = fields.Text(string="Achievements")

    @api.model
    def create(self, vals):
        """This is used to get the licence number"""
        if vals.get('licence_number', 'New') == 'New':
            vals['licence_number'] = self.env['ir.sequence'].next_by_code('licences') or 'New'
        result = super(Licences, self).create(vals)
        return result

    @api.onchange('start_date', 'expire_date')
    def date(self):
        """This will give validation at the time of expired date and start date have any problem"""
        today = date.today()
        if self.start_date and self.expire_date:
            if self.start_date > self.expire_date or today > self.expire_date:
                raise ValidationError('Expire Date Is Not Valid')

    def active_licence(self):
        """It changes the state into active"""
        self.state = 'active'

    def action_active_licence(self):
        """It returns the licences tree view"""
        return {
            'name': 'Active',
            'view_mode': 'tree',
            'res_model': 'licences',
            'type': 'ir.actions.act_window',
            'domain': [('state', '=', 'active')],
            'context': "{'create': False}"
        }

    def licence_expiry_action(self):
        """This function is from scheduled action, it will send mail notification and change the state based on
               condition given below"""
        licences = self.env['licences'].search([])
        for rec in licences:
            if fields.Date.today() == fields.Date.subtract(rec.expire_date, days=rec.expire_remainder_day):
                rec.state = 'expired_soon'
            today = date.today()
            if today == rec.expire_date and rec.state != 'expired':
                email_values = {
                    'email_cc': False,
                    'auto_delete': True,
                    'recipient_ids': [],
                    'partner_ids': [],
                    'scheduled_date': False,
                    'email_to': rec.customer_id.email
                }
                template = self.env.ref('certificates_licenses_expiry.email_template_licence')
                template.send_mail(rec.id, force_send=True, email_values=email_values)
            if date.today() == rec.expire_date:
                rec.state = 'expired'

    def action_create_licence_pdf_report(self):
        """This is used to get pdf report and passes the values to template"""
        data = {
            'record1': self.name,
            'record2': self.licence_number,
            'record3': self.customer_id.name,
            'record4': self.licences_types_id.licence_type,
            'record5': self.start_date,
            'record6': self.expire_date,
            'record7': self.issued_by_id.name,
            'record8': self.project_id.name,
            'record9': self.task_id.name,
            'record10': self.user_id.name,
            'record11': self.company_id.name,
            'record12': self.internal_notes,
            'record13': self.description,
            'record14': self.achievements,
            'record15': self.expire_remainder_day,
            'record16': self.product_id.name,
            'record17': self.state
        }
        return self.env.ref('certificates_licenses_expiry.action_licences_report').report_action(None, data=data)


class LicenceType(models.Model):
    """This is licences type model, it is a sub model of the licences """
    _name = 'licences.types'
    _description = "Licence Type"
    _rec_name = 'licence_type'

    licence_type = fields.Char(string="Licence Type", required=True)


class LicenceTags(models.Model):
    """This is licences tags model, it is a sub model of the licences """
    _name = 'licences.tags'
    _description = "Licence Tag"
    _rec_name = 'licence_tags'

    def _get_default_color(self):
        """This will give the colors to the corresponding field"""
        return randint(1, 11)

    licence_tags = fields.Char(string="Licence Tag", required=True)
    color = fields.Integer(string="Color", default=_get_default_color)

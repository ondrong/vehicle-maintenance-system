# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class VmsProgram(models.Model):
    _name = 'vms.program'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _order = 'name asc'

    cycle_ids = fields.Many2many(
        'vms.cycle',
        required=True,
        string='Cycle(s)')
    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
# -*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>)
#    Copyright (C) 2015 Savoir-faire Linux
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models, _


class HrPayslipWorkedDays(models.Model):
    """Payslip Worked Days"""

    _name = 'hr.payslip.worked_days'
    _description = _(__doc__)

    name = fields.Char(
        'Description', required=True
    )
    payslip_id = fields.Many2one(
        'hr.payslip', 'Pay Slip',
        required=True,
        ondelete='cascade',
        index=True
    )
    number_of_hours = fields.Float(
        'Number of Hours'
    )
    number_of_days = fields.Float(
        'Number of Days'
    )

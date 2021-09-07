# -*- coding: utf-8 -*-

from odoo.exceptions import UserError
from odoo import models, fields, _, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_note = fields.Char(string='Sale Note')

    def _prepare_invoice(self):
        inv_vals = super(SaleOrder, self)._prepare_invoice()
        inv_vals.update({
            'sale_note': self.sale_note
        })
        return inv_vals

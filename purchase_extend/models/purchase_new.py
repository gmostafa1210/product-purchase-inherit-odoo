from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseNew(models.Model):
    _inherit = 'purchase.order'

    dealer = fields.Many2one('dealer.wiki', string='Dealer Name')


class PurchaseLineNew(models.Model):
    _inherit = 'purchase.order.line'

    brand_id = fields.Many2one('product.wiki', string='Brand', readonly=True, related='product_id.product_brand')
    discount = fields.Float(string='Discount', store=True)

    def _prepare_compute_all_values(self):
        compute_all_values = super(PurchaseLineNew, self)._prepare_compute_all_values()
        compute_all_values.update({
            'price_unit': (self.price_unit * (1.0 - self.discount / 100.0)),
            'discount': self.discount,
        })
        return compute_all_values
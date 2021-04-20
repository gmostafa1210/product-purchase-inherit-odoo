from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseNew(models.Model):
    _inherit = 'purchase.order'

    dealer = fields.Many2one('dealer.wiki', string='Dealer Name')
    
class PurchaseLineNew(models.Model):
    _inherit = 'purchase.order.line'

    brand_id = fields.Many2one('product.wiki', string='Brand')
    @api.onchange('product_id')
    def onchange_test(self):
        if self.product_id:
            self.brand_id = self.product_id.product_brand.id

    # def write(self, values):
    #     values['brand_id'] = self.product_id.product_brand.id
    #     return super(PurchaseLineNew, self).write(values)

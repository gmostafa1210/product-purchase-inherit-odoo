from odoo import models, fields, api


class ProductUnderBarcode(models.Model):
    _inherit = 'product.template'

    product_brand = fields.Many2one('product.wiki', string='Product Brand')
    dealer = fields.Many2one('dealer.wiki', string='Dealer Name')


 
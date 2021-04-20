from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductInfo(models.Model):
    _name = 'product.wiki'
    _description = 'Product Brand'
    _rec_name = 'pname'

    pname = fields.Char(string='Product Brand')

class DealerInfo(models.Model):
    _name = 'dealer.wiki'
    _description = 'Dealer Name'
    _rec_name = 'dname'

    dname = fields.Char(string='Dealer Name')


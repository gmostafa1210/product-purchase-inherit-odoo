from odoo import models, fields, api, _
from odoo.exceptions import UserError
import dateutil.parser

class PurchaseFilter(models.TransientModel):
    _name = 'purchase.filter'
    _description ='Purchase Filter'

    date_from = fields.Date(string="From")
    date_to = fields.Date(string="To")

    # is_true = fields.Boolean(string="Want to Filter")

    def get_purchase_filter(self):
        q_list = []
        d_list = []

        # if self.is_true:
        #     product_ids = self.env['purchase.order.line'].search([('qty_received','>',0),('qty_invoiced','<', qty_received)])
        
        product_ids = self.env['purchase.order.line'].search([])
        for i in product_ids:
            if i.qty_received > 0 and i.qty_invoiced < i.qty_received:
                q_list.append(i.order_id.id)
        
        product_date_ids = self.env['purchase.order'].search([('date_approve','>=',self.date_from),('date_approve','<=',self.date_to)])
     
        for j in product_date_ids:
            d_list.append(j.id)
            
        q_list_as_set = set(q_list)
        intersection = q_list_as_set.intersection(d_list)
        my_list = list(intersection)
                
        return {
            'name': 'Filtered Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'tree,form',
            'domain': [('id','in',my_list)]
        }
        
         

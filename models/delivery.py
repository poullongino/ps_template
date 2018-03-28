from odoo import models, fields, api

class Delivery(models.Model):
    "Adding PO Number on the Delivery Form View"

    _inherit = 'stock.picking'

    po_num = fields.Char('PO N°', required = True, store = True)
    order_name = fields.Char('Order Name')




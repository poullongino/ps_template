from odoo import models, api, fields

class Orders(models.Model):
    "Adding Purchase Order Number on the Sales Order Form View"

    _inherit = 'sale.order'

    po_num = fields.Char('PO N°')
    order_name = fields.Char('Order Name', required = True)
    esd = fields.Char('ESD')

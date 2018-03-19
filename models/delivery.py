from odoo import models, fields, api

class Delivery(models.Model):
    "Adding PO Number on the Delivery Form View"

    _inherit = 'stock.picking'

    po_num_id = fields.Many2one('sale.order', default=lambda self: self.env['sale.order'].search([['po_num', '=', True]]))
    po_no = fields.Char(related = 'po_num_id.po_num', store = True)





from odoo import models, fields, api

class Delivery(models.Model):
    "Adding PO Number on the Delivery Form View"

    _inherit = 'stock.picking'

    # po_num_ids = fields.Many2one(comodel_name = 'account.invoice', delegate = True)
    po_number = fields.Char('PO N°', compute = '_get_po')
    d_order_name = fields.Char('Order Name', compute = '_get_po')
    esd = fields.Char('ESD')


    @api.depends('move_lines')
    def _get_po(self):
       po_number = move_lines.po_num

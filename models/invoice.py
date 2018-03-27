from odoo import fields, api, models

class Invoice(models.Model):
    "Adding PO Number on the Invoice"

    _inherit = 'account.invoice'

    order_name = fields.Char('Order Name')
    po_number_id = fields.Many2one('sale.order', default = lambda self: self.env['sale.order'].search([['po_num', '=', True]]))
    po_number = fields.Char(related = 'po_number_id.po_num', store = True)
    esd = fields.Text()


from odoo import fields, api, models

class Invoice(models.Model):
    "Adding PO Number on the Invoice"

    _inherit = 'account.invoice'

    po_number = fields.Char('PO N°', compute='_get_po')
    i_order_name = fields.Char('Order Name', compute='_get_name')
    esd = fields.Char('ESD')

    api.depends('invoice_line_ids')
    def _get_po(self):
        for rec in self:
            invoice_lines = rec.invoice_line_ids
            sale_orders = []
            for inv_line in invoice_lines:
                for so in inv_line.sale_line_ids:
                    if so.order_id.po_num:
                        sale_orders.append(so.order_id.po_num)

            rec['po_number'] = ','.join(list(set(sale_orders)))

    api.depends('invoice_line_ids')
    def _get_name(self):
        for rec in self:
            invoice_lines = rec.invoice_line_ids
            sale_orders = []
            for inv_line in invoice_lines:
                for so in inv_line.sale_line_ids:
                    if so.order_id.po_num:
                        sale_orders.append(so.order_id.order_name)

            rec['i_order_name'] = ','.join(list(set(sale_orders)))

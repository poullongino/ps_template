from odoo import models, api, fields

class Quotation(models.Model):
    "Adding fields to Quotation Form View"

    _inherit = 'sale.order'

    order_name = fields.Char('Order Name', required = True)
from odoo import models, fields, api

class Company(models.Model):
    "Modifying Res Company to Include VRN"

    _inherit = 'res.company'

    vrn_num = fields.Char('VRN', required = True)
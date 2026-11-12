from odoo import fields, models


class Bahan(models.Model):
    _inherit = "product.template"

    x_kritis = fields.Boolean(string="Bahan Kritis")
    x_stok_minimum = fields.Float(string="Stok Minimum")

    def tambahBahan(self):
        pass

    def aturStokMinimum(self):
        pass

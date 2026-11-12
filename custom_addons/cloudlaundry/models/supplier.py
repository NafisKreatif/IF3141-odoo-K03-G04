from odoo import fields, models


class Supplier(models.Model):
    _inherit = "res.partner"

    x_narahubung = fields.Char(string="Narahubung")

    def tambahSupplier(self):
        pass

    def ubahSupplier(self):
        pass


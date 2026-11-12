from odoo import fields, models


class Cabang(models.Model):
    _inherit = "stock.warehouse"

    x_alamat = fields.Char(string="Alamat")
    x_ukuran = fields.Char(string="Ukuran")

    def tambahCabang(self):
        pass

    def ubahCabang(self):
        pass
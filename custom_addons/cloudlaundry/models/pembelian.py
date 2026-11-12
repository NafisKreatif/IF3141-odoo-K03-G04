from odoo import fields, models


class Supplier(models.Model):
    _inherit = "res.partner"

    x_narahubung = fields.Char(string="Narahubung")

    def tambahSupplier(self):
        pass

    def ubahSupplier(self):
        pass


class PesananPembelian(models.Model):
    _inherit = "purchase.order"

    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")

    def buatPO(self):
        pass

    def konfirmasiPO(self):
        pass

    def terimaBarang(self):
        pass

    def rekapPembelian(self):
        pass


class DetailPembelian(models.Model):
    _inherit = "purchase.order.line"

    def tambahItem(self):
        pass

    def riwayatHarga(self):
        pass

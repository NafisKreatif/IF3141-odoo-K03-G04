from odoo import fields, models


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

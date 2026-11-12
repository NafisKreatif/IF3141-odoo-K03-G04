from odoo import fields, models


class StokCabang(models.Model):
    _inherit = "stock.quant"

    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")

    def perbaruiSaldo(self):
        pass

    def cekStokMinimum(self):
        pass

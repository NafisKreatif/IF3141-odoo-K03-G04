from odoo import fields, models


class Bahan(models.Model):
    _inherit = "product.template"

    x_kritis = fields.Boolean(string="Bahan Kritis")
    x_stok_minimum = fields.Float(string="Stok Minimum")

    def tambahBahan(self):
        pass

    def aturStokMinimum(self):
        pass


class StokCabang(models.Model):
    _inherit = "stock.quant"

    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")

    def perbaruiSaldo(self):
        pass

    def cekStokMinimum(self):
        pass


class PenyesuaianStok(models.Model):
    _inherit = "stock.move"

    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")
    x_id_pemeriksa = fields.Many2one("hr.employee", string="Pemeriksa")
    x_jenis_penyesuaian = fields.Selection(
        [("mingguan", "Mingguan"), ("bulanan", "Bulanan")],
        string="Jenis Penyesuaian",
    )
    x_stok_sistem = fields.Float(string="Stok Sistem")
    x_stok_fisik = fields.Float(string="Stok Fisik")
    x_selisih = fields.Float(string="Selisih")
    x_tanggal_penyesuaian = fields.Date(string="Tanggal Penyesuaian")

    def catatHitungFisik(self):
        pass

    def hitungSelisih(self):
        pass

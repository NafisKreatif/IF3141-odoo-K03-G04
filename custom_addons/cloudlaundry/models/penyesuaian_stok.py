from odoo import fields, models


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

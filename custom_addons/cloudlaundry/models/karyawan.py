from odoo import fields, models


class Karyawan(models.Model):
    _inherit = "hr.employee"

    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")

    def tambahKaryawan(self):
        pass

    def ubahKaryawan(self):
        pass

    def daftarHadirHariIni(self):
        pass

from odoo import fields, models


class Pesanan(models.Model):
    _inherit = "sale.order"

    x_id_admin = fields.Many2one("res.users", string="Admin Pencatat")
    x_tipe = fields.Selection(
        [("pickup", "Pickup"), ("walk_in", "Walk-in")],
        string="Tipe Pesanan",
        default="walk_in",
        required=True,
    )
    x_tahap = fields.Selection(
        [
            ("diterima", "Diterima"),
            ("dicuci", "Dicuci"),
            ("dikeringkan", "Dikeringkan"),
            ("disetrika", "Disetrika"),
            ("dikemas", "Dikemas"),
            ("siap_antar", "Siap Antar"),
            ("selesai", "Selesai"),
        ],
        string="Tahap Pesanan",
        default="diterima",
        required=True,
        tracking=True,
    )
    x_status_bayar = fields.Selection(
        [("belum_lunas", "Belum Lunas"), ("lunas", "Lunas")],
        string="Status Pembayaran",
        default="belum_lunas",
        required=True,
        tracking=True,
    )
    x_waktu_diterima = fields.Datetime(string="Waktu Diterima")
    x_perkiraan_selesai = fields.Datetime(string="Perkiraan Selesai")
    x_token_portal = fields.Char(string="Token Portal", copy=False, index=True)

    def buatPesanan(self):
        pass

    def hitungTagihan(self):
        pass

    def perbaruiTahap(self):
        pass

    def terbitkanNota(self):
        pass

    def buatTautanStatus(self):
        pass

    def tampilkanStatusPortal(self):
        pass

    def daftarBelumLunas(self):
        pass

    def tandaiLunas(self):
        pass

    def rekapPenjualan(self):
        pass

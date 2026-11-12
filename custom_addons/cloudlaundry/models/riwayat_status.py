from odoo import fields, models


class RiwayatStatus(models.Model):
    _name = "cloudlaundry.riwayat_status"
    _description = "Riwayat Status Pesanan"
    _order = "x_waktu desc, id desc"

    x_id_pesanan = fields.Many2one(
        "sale.order",
        string="Pesanan",
        required=True,
        ondelete="cascade",
        index=True,
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
        string="Tahap",
        required=True,
    )
    x_id_karyawan = fields.Many2one("hr.employee", string="Karyawan")
    x_waktu = fields.Datetime(string="Waktu", required=True, default=fields.Datetime.now)

    def catatPerubahan(self):
        pass

    def riwayatPesanan(self):
        pass

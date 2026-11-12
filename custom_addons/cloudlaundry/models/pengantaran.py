from odoo import fields, models


class Pengantaran(models.Model):
    _name = "cloudlaundry.pengantaran"
    _description = "Pengantaran Pesanan"
    _order = "x_jadwal, id"

    x_id_pesanan = fields.Many2one(
        "sale.order",
        string="Pesanan",
        required=True,
        ondelete="cascade",
        index=True,
    )
    x_id_kurir = fields.Many2one("hr.employee", string="Kurir")
    x_jenis = fields.Selection(
        [("jemput", "Jemput"), ("antar", "Antar")],
        string="Jenis",
        required=True,
    )
    x_alamat = fields.Char(string="Alamat")
    x_jadwal = fields.Datetime(string="Jadwal")
    x_status = fields.Selection(
        [
            ("dijadwalkan", "Dijadwalkan"),
            ("dijemput", "Dijemput"),
            ("dalam_perjalanan", "Dalam Perjalanan"),
            ("diterima", "Diterima Pelanggan"),
        ],
        string="Status",
        default="dijadwalkan",
        required=True,
    )
    x_waktu_update = fields.Datetime(string="Waktu Update")

    def jadwalkan(self):
        pass

    def perbaruiStatus(self):
        pass

    def daftarHarian(self):
        pass

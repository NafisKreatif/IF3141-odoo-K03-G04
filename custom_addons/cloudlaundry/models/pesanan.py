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


class DetailPesanan(models.Model):
    _inherit = "sale.order.line"

    def tambahItem(self):
        pass

    def hitungSubtotal(self):
        pass


class FotoBarang(models.Model):
    _inherit = "ir.attachment"

    x_id_pesanan = fields.Many2one(
        "sale.order",
        string="Pesanan",
        ondelete="cascade",
        index=True,
    )

    def unggahFoto(self):
        pass

    def tampilkanFoto(self):
        pass


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


class Pembayaran(models.Model):
    _name = "cloudlaundry.pembayaran"
    _description = "Pembayaran Pesanan"
    _order = "x_waktu desc, id desc"

    x_id_pesanan = fields.Many2one(
        "sale.order",
        string="Pesanan",
        required=True,
        ondelete="cascade",
        index=True,
    )
    x_metode = fields.Selection(
        [("qris", "QRIS"), ("tunai", "Tunai")],
        string="Metode",
        required=True,
    )
    x_nominal = fields.Monetary(
        string="Nominal",
        required=True,
        currency_field="x_mata_uang_id",
    )
    x_mata_uang_id = fields.Many2one(
        "res.currency",
        string="Mata Uang",
        required=True,
        default=lambda self: self.env.company.currency_id,
    )
    x_ref_gateway = fields.Char(string="Referensi Gateway", index=True)
    x_status = fields.Selection(
        [
            ("menunggu", "Menunggu"),
            ("berhasil", "Berhasil"),
            ("ditolak", "Ditolak"),
        ],
        string="Status",
        default="menunggu",
        required=True,
    )
    x_waktu = fields.Datetime(string="Waktu")

    _sql_constraints = [
        (
            "x_pembayaran_ref_gateway_uniq",
            "unique(x_ref_gateway)",
            "Referensi gateway harus unik.",
        ),
    ]

    def buatTagihanQRIS(self):
        pass

    def verifikasiNotifikasi(self):
        pass

    def catatTunai(self):
        pass

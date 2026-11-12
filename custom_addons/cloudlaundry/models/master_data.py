from odoo import fields, models


class Cabang(models.Model):
    _inherit = "stock.warehouse"

    x_alamat = fields.Char(string="Alamat")
    x_ukuran = fields.Char(string="Ukuran")

    def tambahCabang(self):
        pass

    def ubahCabang(self):
        pass


class Pelanggan(models.Model):
    _inherit = "res.partner"

    x_alamat_jemput = fields.Char(string="Alamat Jemput")

    def tambahPelanggan(self):
        pass

    def ubahPelanggan(self):
        pass

    def cekDuplikasi(self):
        pass


class Layanan(models.Model):
    _inherit = "product.template"

    x_jenis_layanan = fields.Selection(
        [
            ("reguler", "Reguler"),
            ("express", "Express"),
            ("kilat", "Kilat"),
            ("satuan", "Satuan"),
            ("langganan", "Langganan"),
        ],
        string="Jenis Layanan",
    )
    x_satuan_harga = fields.Selection(
        [("kg", "Kg"), ("pcs", "Pcs")],
        string="Satuan Harga",
    )
    x_durasi_jam = fields.Float(string="Durasi (Jam)")

    def tambahLayanan(self):
        pass

    def ubahTarif(self):
        pass

    def ambilTarif(self):
        pass


class Karyawan(models.Model):
    _inherit = "hr.employee"

    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")

    def tambahKaryawan(self):
        pass

    def ubahKaryawan(self):
        pass

    def daftarHadirHariIni(self):
        pass


class AkunPengguna(models.Model):
    _inherit = "res.users"

    x_id_karyawan = fields.Many2one(
        "hr.employee",
        string="Karyawan",
        ondelete="set null",
        index=True,
    )
    x_peran = fields.Selection(
        [
            ("owner", "Owner"),
            ("area_manager", "Area Manager"),
            ("kepala_store", "Kepala Store"),
            ("hr", "HR"),
            ("finance", "Finance"),
            ("admin", "Admin"),
            ("staf_operasional", "Staf Operasional"),
            ("kurir", "Kurir"),
            ("administrator_sistem", "Administrator Sistem"),
        ],
        string="Peran CloudLaundry",
    )
    x_terakhir_login = fields.Datetime(string="Terakhir Login")

    _sql_constraints = [
        (
            "x_akun_pengguna_karyawan_uniq",
            "unique(x_id_karyawan)",
            "Satu karyawan hanya dapat ditautkan ke satu akun pengguna.",
        ),
    ]

    def buatAkun(self):
        pass

    def aturPeran(self):
        pass

    def nonaktifkan(self):
        pass

    def resetSandi(self):
        pass

    def catatLog(self):
        pass

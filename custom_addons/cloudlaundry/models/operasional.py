from odoo import fields, models


class Tugas(models.Model):
    _inherit = "project.task"

    x_jenis_cloudlaundry = fields.Selection(
        [("operasional", "Operasional"), ("komplain", "Komplain")],
        string="Jenis Tugas CloudLaundry",
        index=True,
    )
    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")
    x_id_pic = fields.Many2one("hr.employee", string="PIC")
    x_id_pesanan = fields.Many2one("sale.order", string="Pesanan")
    x_tanggal = fields.Date(string="Tanggal")
    x_tahap = fields.Selection(
        [
            ("cuci", "Cuci"),
            ("kering", "Kering"),
            ("setrika", "Setrika"),
            ("kemas", "Kemas"),
        ],
        string="Tahap Tugas",
    )
    x_jadwal_mulai = fields.Datetime(string="Jadwal Mulai")
    x_jadwal_selesai = fields.Datetime(string="Jadwal Selesai")
    x_status = fields.Selection(
        [
            ("belum_mulai", "Belum Mulai"),
            ("dikerjakan", "Dikerjakan"),
            ("selesai", "Selesai"),
        ],
        string="Status Tugas",
        default="belum_mulai",
    )

    def buatTugas(self):
        pass

    def ubahStatus(self):
        pass

    def cekTertunda(self):
        pass

    def cekDobel(self):
        pass


class Kehadiran(models.Model):
    _inherit = "hr.attendance"

    x_id_cabang = fields.Many2one("stock.warehouse", string="Cabang")

    def checkIn(self):
        pass

    def checkOut(self):
        pass

    def rekapPeriode(self):
        pass

    def eksporRekap(self):
        pass


class KasusKomplain(models.Model):
    _inherit = "project.task"

    x_status_komplain = fields.Selection(
        [
            ("baru", "Baru"),
            ("ditanggapi", "Ditanggapi"),
            ("dalam_penanganan", "Dalam Penanganan"),
            ("cuci_ulang", "Cuci Ulang"),
            ("selesai", "Selesai"),
        ],
        string="Status Komplain",
        default="baru",
    )
    x_id_pesanan = fields.Many2one(
        "sale.order",
        string="Pesanan Komplain",
        ondelete="set null",
        index=True,
    )
    x_id_pic_komplain = fields.Many2one("hr.employee", string="PIC Komplain")
    x_id_pencatat = fields.Many2one("res.users", string="Pencatat")
    x_lampiran_ids = fields.Many2many(
        "ir.attachment",
        "cloudlaundry_komplain_attachment_rel",
        "task_id",
        "attachment_id",
        string="Lampiran Komplain",
    )
    x_waktu_dicatat = fields.Datetime(string="Waktu Dicatat")
    x_tenggat_tanggapan = fields.Datetime(string="Tenggat Tanggapan")
    x_tenggat_selesai = fields.Datetime(string="Tenggat Selesai")
    x_hasil_penyelesaian = fields.Text(string="Hasil Penyelesaian")
    x_terlambat = fields.Boolean(string="Terlambat")

    def buatKasus(self):
        pass

    def tetapkanPIC(self):
        pass

    def perbaruiStatus(self):
        pass

    def cekTerlambat(self):
        pass

    def rekapKomplain(self):
        pass

from odoo import fields, models


class Tugas(models.Model):
    _inherit = "project.task"

    x_jenis_cloudlaundry = fields.Selection(
        [("operasional", "Operasional"), ("komplain", "Komplain")],
        string="Jenis Tugas CloudLaundry",
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
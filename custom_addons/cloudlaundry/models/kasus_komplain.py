from odoo import fields, models


class KasusKomplain(models.Model):
    _inherit = "project.task"

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
    x_status_komplain = fields.Selection(
        [
            ("baru", "Baru"),
            ("ditanggapi", "Ditanggapi"),
            ("dalam_penanganan", "Dalam Penanganan"),
            ("cuci_ulang", "Cuci Ulang"),
            ("selesai", "Selesai"),
        ],
        string="Status Komplain",
    )
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

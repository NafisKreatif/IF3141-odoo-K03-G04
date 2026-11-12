from odoo import fields, models


class Pelanggan(models.Model):
    _inherit = "res.partner"

    x_no_whatsapp = fields.Char(string="No. WhatsApp", index=True)
    x_alamat_jemput = fields.Char(string="Alamat Jemput")

    _sql_constraints = [
        (
            "x_pelanggan_no_whatsapp_uniq",
            "unique(x_no_whatsapp)",
            "Nomor WhatsApp pelanggan harus unik.",
        ),
    ]

    def tambahPelanggan(self):
        pass

    def ubahPelanggan(self):
        pass

    def cekDuplikasi(self):
        pass

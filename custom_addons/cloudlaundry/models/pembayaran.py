from odoo import fields, models


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

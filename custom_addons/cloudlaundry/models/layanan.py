from odoo import fields, models

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

from odoo import fields, models


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

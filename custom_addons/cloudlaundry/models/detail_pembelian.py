from odoo import fields, models


class DetailPembelian(models.Model):
    _inherit = "purchase.order.line"

    def tambahItem(self):
        pass

    def riwayatHarga(self):
        pass

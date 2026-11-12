from odoo import fields, models


class DetailPesanan(models.Model):
    _inherit = "sale.order.line"

    def tambahItem(self):
        pass

    def hitungSubtotal(self):
        pass

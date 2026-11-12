from odoo import fields, models


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

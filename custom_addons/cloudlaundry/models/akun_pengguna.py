from odoo import fields, models


class AkunPengguna(models.Model):
    _inherit = "res.users"

    x_id_karyawan = fields.Many2one(
        "hr.employee",
        string="Karyawan",
        ondelete="set null",
        index=True,
    )
    x_peran = fields.Selection(
        [
            ("owner", "Owner"),
            ("area_manager", "Area Manager"),
            ("kepala_store", "Kepala Store"),
            ("hr", "HR"),
            ("finance", "Finance"),
            ("admin", "Admin"),
            ("staf_operasional", "Staf Operasional"),
            ("kurir", "Kurir"),
            ("administrator_sistem", "Administrator Sistem"),
        ],
        string="Peran CloudLaundry",
    )
    x_terakhir_login = fields.Datetime(string="Terakhir Login")

    _sql_constraints = [
        (
            "x_akun_pengguna_karyawan_uniq",
            "unique(x_id_karyawan)",
            "Satu karyawan hanya dapat ditautkan ke satu akun pengguna.",
        ),
    ]

    def buatAkun(self):
        pass

    def aturPeran(self):
        pass

    def nonaktifkan(self):
        pass

    def resetSandi(self):
        pass

    def catatLog(self):
        pass

{
    "name": "CloudLaundry",
    "summary": "Model inti sistem CloudLaundry",
    "version": "17.0.1.0.0",
    "license": "LGPL-3",
    "author": "IF3141",
    "category": "Services",
    "depends": [
        "sale_management",
        "sale_stock",
        "hr",
        "hr_attendance",
        "project",
        "purchase_stock",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
}

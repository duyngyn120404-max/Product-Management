from odoo import fields, models


class ProductManagementBrand(models.Model):
    _name = "product.management.brand"
    _description = "Product Management Brand"
    _order = "sequence, name"

    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)

    _name_unique = models.Constraint(
        "unique(name)",
        "The brand name must be unique.",
    )
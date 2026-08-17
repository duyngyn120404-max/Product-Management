from odoo import fields, models

class ProductManagementCategory(models.Model):
    _name = "product.management.category"
    _description = "Product Management Category"
    _order = "sequence, name"

    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    parent_id = fields.Many2one(
        "product.management.category", 
        string="Parent Category",
        ondelete="restrict"
    )

    field_ids = fields.One2many(
        "product.management.category.field",
        "category_id",
        string="Fields",
    )

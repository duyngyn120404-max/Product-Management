from odoo import fields, models

class ProductManagementCategoryField(models.Model):
    _name = "product.management.category.field"
    _description = "Product Management Category Field"
    _order = "category_id, sequence, name"

    name = fields.Char(required=True)
    category_id = fields.Many2one(
        "product.management.category",
        string="Category",
        required=True,
        ondelete="cascade"
    )
    field_type = fields.Selection(
        [
            ("char", "Char"),
            ("text", "Text"),
            ("integer", "Integer"),
            ("float", "Decimal"),
            ("boolean", "Boolean"),
            ("date", "Date"),
            ("datetime", "Datetime"),
            ("selection", "Selection"),
        ],
        required = True,
        default="char",
    )
    required = fields.Boolean(default=False)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    help = fields.Text(string="Help", help="Help text for this field, displayed in the form view.")
    option_ids = fields.One2many(
        "product.management.category.field.option",
        "field_id",
        string="Options",
    )

class ProductManagementCategoryFieldOption(models.Model):
    _name = "product.management.category.field.option"
    _description = "Product Management Category Field Option"
    _order = "field_id, sequence, name"

    name = fields.Char(required=True)
    field_id = fields.Many2one(
        "product.management.category.field",
        string="Field",
        required=True,
        ondelete="cascade"
    )
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
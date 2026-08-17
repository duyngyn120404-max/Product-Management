from odoo import api, fields, models

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

    def _sync_products_for_categories(self, categories=None):
        categories = categories or self.mapped("category_id")
        if not categories:
            return

        products = self.env["product.management.product"].search([
            ("category_id", "in", categories.ids)
        ])
        products._sync_field_values_with_category()

    @api.model_create_multi
    def create(self, vals_list):
        fields = super().create(vals_list)
        fields._sync_products_for_categories()
        return fields


    def write(self, vals):
        categories_before = self.mapped("category_id")

        result = super().write(vals)

        sync_fields = {"category_id", "active", "sequence", "name", "field_type", "required"}
        if sync_fields & set(vals):
            categories_after = self.mapped("category_id")
            self._sync_products_for_categories(categories_before | categories_after)

        return result

    def unlink(self):
        categories = self.mapped("category_id")

        field_values = self.env["product.management.product.field.value"].search([
            ("field_id", "in", self.ids)
        ])
        field_values.unlink()

        result = super().unlink()
        self._sync_products_for_categories(categories)
        return result

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
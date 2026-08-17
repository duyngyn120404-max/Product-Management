from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ProductManagementProduct(models.Model):
    _name = "product.management.product"
    _description = "Product Management Product"
    _order = "sequence, name"

    default_code = fields.Char(string="Internal Reference")
    name = fields.Char(required=True)
    category_id = fields.Many2one(
        "product.management.category",
        string="Category",
        required=True,
        ondelete="restrict",
    )
    brand_id = fields.Many2one(
        "product.management.brand",
        string="Brand",
        ondelete="restrict",
    )
    list_price = fields.Float(default=0.0)
    qty_available = fields.Integer(default=0)
    stock_status = fields.Selection(
        [
            ("in_stock", "In Stock"),
            ("low_stock", "Low Stock"),
            ("out_of_stock", "Out of Stock"),
        ],
        default="in_stock",
        required=True,
    )
    product_status = fields.Selection(
        [
            ("draft", "Draft"),
            ("available", "Available"),
            ("discontinued", "Discontinued"),
        ],
        default="draft",
        required=True,
    )
    image_1920 = fields.Image()
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)

    field_value_ids = fields.One2many(
        "product.management.product.field.value",
        "product_id",
        string="Specifications",
    )

    @api.model_create_multi
    def create(self, vals_list):
        products = super().create(vals_list)
        products._sync_field_values_with_category()
        return products

    def write(self, vals):
        result = super().write(vals)
        if "category_id" in vals:
            self._sync_field_values_with_category()
        return result

    @api.onchange("category_id")
    def _onchange_category_id(self):
        self._sync_field_values_with_category()

    def _has_required_dynamic_value(self, value):
        if value.field_type == "char":
            return bool(value.value_char)
        if value.field_type == "text":
            return bool(value.value_text)
        if value.field_type == "integer":
            return value.value_integer is not False
        if value.field_type == "float":
            return value.value_float is not False
        if value.field_type == "boolean":
            return True
        if value.field_type == "date":
            return bool(value.value_date)
        if value.field_type == "datetime":
            return bool(value.value_datetime)
        if value.field_type == "selection":
            return bool(value.option_id)
        return False         

    @api.constrains("field_value_ids")
    def _check_required_field_values(self):
        for product in self:
            for value in product.field_value_ids:
                if not value.required:
                    continue

                has_value = self._has_required_dynamic_value(value)

                '''The following code is commented out because it was replaced by the _has_required_dynamic_value method (a stronger val method).
                has_value = any([
                    value.value_char,
                    value.value_text,
                    value.value_integer,
                    value.value_float,
                    value.value_boolean,
                    value.value_date,
                    value.value_datetime,
                    value.option_id,
                ])
                '''

                if not has_value:
                    raise ValidationError(
                        f"{value.field_id.name} is required for category {product.category_id.name}."
                    )
                

    def _get_active_category_fields(self):
        self.ensure_one()
        if not self.category_id:
            return self.env["product.management.category.field"]
        return self.category_id.field_ids.filtered(lambda f: f.active)

    def _sync_field_values_with_category(self):
        for product in self:
            if not product.category_id:
                product.field_value_ids = [(5, 0, 0)]
                continue

            category_fields = product._get_active_category_fields()
            existing_values_by_field = {
                value.field_id.id: value
                for value in product.field_value_ids
            }

            commands = []

            for field in category_fields:
                if field.id in existing_values_by_field:
                    continue

                commands.append((0, 0, {"field_id": field.id}))

            obsolete_values = product.field_value_ids.filtered(
                lambda value: value.field_id not in category_fields
            )

            for value in obsolete_values:
                commands.append((2, value.id))

            if commands:
                product.field_value_ids = commands
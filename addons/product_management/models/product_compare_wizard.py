from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductManagementCompareWizard(models.TransientModel):
    _name = "product.management.compare.wizard"
    _description = "Product Management Compare Wizard"


    product_name_1 = fields.Char(string="Product 1", readonly=True)
    product_name_2 = fields.Char(string="Product 2", readonly=True)
    product_name_3 = fields.Char(string="Product 3", readonly=True)
    product_name_4 = fields.Char(string="Product 4", readonly=True)

    image_1 = fields.Image(string="Image 1", readonly=True)
    image_2 = fields.Image(string="Image 2", readonly=True)
    image_3 = fields.Image(string="Image 3", readonly=True)
    image_4 = fields.Image(string="Image 4", readonly=True)

    product_ids = fields.Many2many(
        "product.management.product",
        "pm_compare_product_rel",
        "wizard_id",
        "product_id",
        string="Products",
        readonly=True,
    )

    category_id = fields.Many2one(
        "product.management.category",
        string="Category",
        readonly=True,
    )

    show_default_code = fields.Boolean(string="Product Code", default=True)
    show_brand = fields.Boolean(string="Brand", default=True)
    show_list_price = fields.Boolean(string="Price", default=True)
    show_qty_available = fields.Boolean(string="Quantity", default=True)
    show_stock_status = fields.Boolean(string="Stock Status", default=True)
    show_product_status = fields.Boolean(string="Product Status", default=True)

    dynamic_field_ids = fields.Many2many(
        "product.management.category.field",
        "pm_compare_field_rel",
        "wizard_id",
        "field_id",
        string="Specifications",
        domain="[('category_id', '=', category_id), ('active', '=', True)]",
    )

    result_line_ids = fields.One2many(
        "product.management.compare.result.line",
        "wizard_id",
        string="Comparison",
        readonly=True,
    ) 

    product_count = fields.Integer(
        string="Product Count",
        compute = "_compute_product_count"
    )

    def _set_product_previews(self):
        for wizard in self:
            products = wizard.product_ids[:4]

            preview_values = {
                "product_name_1": False,
                "product_name_2": False,
                "product_name_3": False,
                "product_name_4": False,
                "image_1": False,
                "image_2": False,
                "image_3": False,
                "image_4": False,
            }

            for index, product in enumerate(products, start=1):
                preview_values[f"product_name_{index}"] = product.name
                preview_values[f"image_{index}"] = product.image_1920

            wizard.update(preview_values)

    @api.depends("product_ids")
    def _compute_product_count(self):
        for wizard in self:
            wizard.product_count = len(wizard.product_ids)

    @api.onchange(
        "show_default_code",
        "show_brand",
        "show_list_price",
        "show_qty_available",
        "show_stock_status",
        "show_product_status",
        "dynamic_field_ids",
    )
    def _onchange_compare_criteria(self):
        self._rebuild_result_lines()
   

    def _add_common_line(self, commands, sequence, name, products, getter):
        values = {
            "sequence": sequence,
            "criterion_name": name,
        }

        for index, product in enumerate(products[:4], start=1):
            values[f"value_{index}"] = getter(product) or "-"

        commands.append((0, 0, values))

    def _format_dynamic_value(self, field_value):
        if not field_value:
            return "-"

        if field_value.field_type == "char":
            return field_value.value_char or "-"
        if field_value.field_type == "text":
            return field_value.value_text or "-"
        if field_value.field_type == "integer":
            return str(field_value.value_integer)
        if field_value.field_type == "float":
            return str(field_value.value_float)
        if field_value.field_type == "boolean":
            return "Yes" if field_value.value_boolean else "No"
        if field_value.field_type == "date":
            return str(field_value.value_date) if field_value.value_date else "-"
        if field_value.field_type == "datetime":
            return str(field_value.value_datetime) if field_value.value_datetime else "-"
        if field_value.field_type == "selection":
            return field_value.option_id.name or "-"

        return "-"

    def _rebuild_result_lines(self):
        for wizard in self:
            products = wizard.product_ids

            commands = [(5, 0, 0)]
            sequence = 10

            if wizard.show_default_code:
                wizard._add_common_line(
                    commands, sequence, "Product Code", products,
                    lambda product: product.default_code
                )
                sequence += 10

            if wizard.show_brand:
                wizard._add_common_line(
                    commands, sequence, "Brand", products,
                    lambda product: product.brand_id.name
                )
                sequence += 10

            if wizard.show_list_price:
                wizard._add_common_line(
                    commands, sequence, "Price", products,
                    lambda product: str(product.list_price)
                )
                sequence += 10

            if wizard.show_qty_available:
                wizard._add_common_line(
                    commands, sequence, "Quantity", products,
                    lambda product: str(product.qty_available)
                )
                sequence += 10

            if wizard.show_stock_status:
                wizard._add_common_line(
                    commands, sequence, "Stock Status", products,
                    lambda product: dict(product._fields["stock_status"].selection).get(product.stock_status)
                )
                sequence += 10

            if wizard.show_product_status:
                wizard._add_common_line(
                    commands, sequence, "Product Status", products,
                    lambda product: dict(product._fields["product_status"].selection).get(product.product_status)
                )
                sequence += 10

            for field in wizard.dynamic_field_ids.sorted("sequence"):
                field_id = field._origin.id or field.id

                values = {
                    "sequence": sequence,
                    "criterion_name": field.name,
                }

                for index, product in enumerate(products[:4], start=1):
                    field_value = product.field_value_ids.filtered(
                        lambda value: value.field_id.id == field_id
                    )[:1]
                    values[f"value_{index}"] = wizard._format_dynamic_value(field_value)

                commands.append((0, 0, values))
                sequence += 10

            wizard.result_line_ids = commands    

class ProductManagementCompareResultLine(models.TransientModel):
    _name = "product.management.compare.result.line"
    _description = "Product Management Compare Result Line"
    _order = "sequence, id"

    wizard_id = fields.Many2one(
        "product.management.compare.wizard",
        required=True,
        ondelete="cascade",
    )

    sequence = fields.Integer(default=10)
    criterion_name = fields.Char(string="Criterion", readonly=True)

    value_1 = fields.Char(string="Product 1")
    value_2 = fields.Char(string="Product 2")
    value_3 = fields.Char(string="Product 3")
    value_4 = fields.Char(string="Product 4")

    product_count = fields.Integer(
        related="wizard_id.product_count"
    )

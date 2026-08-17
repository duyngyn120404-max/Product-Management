from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ProductManagementProductFieldValue(models.Model):
    _name = "product.management.product.field.value"
    _description = "Product Management Product Field Value"
    _order = "sequence, field_id"

    product_id = fields.Many2one(
        "product.management.product",
        string="Product",
        required=True,
        ondelete="cascade",
    )

    field_id = fields.Many2one(
        "product.management.category.field",
        string="Field",
        required=True,
        ondelete="restrict",
    )
    sequence = fields.Integer(related="field_id.sequence", store=True)
    field_type = fields.Selection(related="field_id.field_type", store=True)
    required = fields.Boolean(related="field_id.required", store=True)
    help = fields.Text(related="field_id.help", store=True)

    value_char = fields.Char(string="Text")
    value_text = fields.Text(string="Long Text")
    value_integer = fields.Integer(string="Integer")
    value_float = fields.Float(string="Decimal")
    value_boolean = fields.Boolean(string="Boolean")
    value_date = fields.Date(string="Date")
    value_datetime = fields.Datetime(string="Datetime")
    option_id = fields.Many2one(
        "product.management.category.field.option",
        string="Option",
        ondelete="restrict",
    )

    @api.constrains("field_id", "option_id")
    def _check_option_belongs_to_field(self):
        for value in self:
            if not value.option_id:
                continue

            if value.option_id.field_id != value.field_id:
                raise ValidationError(
                    "The selected option must belong to the selected field."
                )
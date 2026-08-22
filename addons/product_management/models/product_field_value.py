from odoo import api, fields, models

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

    display_value = fields.Char(
        string="Value",
        compute="_compute_display_value",
    )

    @api.depends(
        "field_type",
        "value_char",
        "value_text",
        "value_integer",
        "value_float",
        "value_boolean",
        "value_date",
        "value_datetime",
        "option_id",
    )
    def _compute_display_value(self):
        for record in self:
            if record.field_type == "char":
                record.display_value = record.value_char or "-"
            elif record.field_type == "text":
                record.display_value = record.value_text or "-"
            elif record.field_type == "integer":
                record.display_value = str(record.value_integer) if record.value_integer is not False else "-"
            elif record.field_type == "float":
                record.display_value = str(record.value_float) if record.value_float is not False else "-"
            elif record.field_type == "boolean":
                record.display_value = "Yes" if record.value_boolean else "No"
            elif record.field_type == "date":
                record.display_value = str(record.value_date) if record.value_date else "-"
            elif record.field_type == "datetime":
                record.display_value = str(record.value_datetime) if record.value_datetime else "-"
            elif record.field_type == "selection":
                record.display_value = record.option_id.name or "-"
            else:
                record.display_value = "-"
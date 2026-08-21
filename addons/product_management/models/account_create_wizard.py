from odoo import fields, models
from odoo.exceptions import ValidationError


class ProductManagementAccountCreateWizard(models.TransientModel):
    _name = "product.management.account.create.wizard"
    _description = "Product Management Account Create Wizard"

    name = fields.Char(required=True)
    login = fields.Char(string="Email/Login", required=True)
    email = fields.Char()
    active = fields.Boolean(default=True)

    def action_create_viewer_account(self):
        self.ensure_one()

        existing_user = self.env["res.users"].sudo().search(
            [("login", "=", self.login)],
            limit=1,
        )
        if existing_user:
            raise ValidationError("A user with this login already exists.")

        viewer_group = self.env.ref("product_management.group_product_management_viewer")
        user = self.env["res.users"].sudo().create(
            {
                "name": self.name,
                "login": self.login,
                "email": self.email or self.login,
                "active": self.active,
                "group_ids": [(6, 0, [viewer_group.id])],
            }
        )

        return {
            "type": "ir.actions.act_window",
            "name": "Account",
            "res_model": "res.users",
            "res_id": user.id,
            "view_mode": "form",
            "views": [
                (
                    self.env.ref(
                        "product_management.view_product_management_account_form"
                    ).id,
                    "form",
                )
            ],
            "target": "current",
        }

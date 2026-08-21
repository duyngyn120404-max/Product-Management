from odoo import fields, models
from odoo.exceptions import ValidationError


class ProductManagementEditWizard(models.TransientModel):
    _name = "product.management.account.edit.wizard"
    _description = "Product Management Account Edit Wizard"

    user_id = fields.Many2one(
        "res.users",
        required=True,
        readonly=True,
    )

    role = fields.Selection(
        [
            ("viewer", "Viewer"),
            ("admin", "Admin"),
        ],
        required=True,
        default="viewer",
    )

    name = fields.Char(required=True)
    login = fields.Char(string="Email/Login", required=True)
    email = fields.Char()
    active = fields.Boolean()

    def action_update_account(self):
        self.ensure_one()

        existing_user = self.env["res.users"].sudo().search([
            ("login", "=", self.login),
            ("id", "!=", self.user_id.id),
        ], limit=1)

        if existing_user:
            raise ValidationError("A user with this login already exists")

        self._check_product_management_role_change()

        self.user_id.sudo().write({
            "name": self.name,
            "login": self.login,
            "email": self.email or self.login,
            "active": self.active,
            "group_ids": self._get_group_commands_for_role(),
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Account",
            "res_model": "res.users",
            "res_id": self.user_id.id,
            "view_mode": "form",
            "views": [(self.env.ref("product_management.view_product_management_account_form").id, "form")],
            "target": "current",
        }

    def _get_user_product_management_role(self, user):
        admin_group = self.env.ref("product_management.group_product_management_admin")
        if admin_group in user.group_ids:
            return "admin"

        return "viewer"

    def _check_product_management_role_change(self):
        self.ensure_one()

        viewer_group = self.env.ref("product_management.group_product_management_viewer")
        admin_group = self.env.ref("product_management.group_product_management_admin")
        product_groups = viewer_group | admin_group

        user = self.user_id.sudo()

        system_group = self.env.ref("base.group_system")
        if system_group in user.all_group_ids and user.id != self.env.user.id:
            raise ValidationError(
                "You cannot edit an Odoo System Administrator."
            )

        if not user.all_group_ids & product_groups:
            raise ValidationError("you can only manage Product Management accounts")

        is_current_admin = admin_group in user.group_ids
        is_downgrade = is_current_admin and self.role == "viewer"

        if is_downgrade and user.id == self.env.user.id:
            raise ValidationError(
                "You cannot downgrade your own Product Management Admin role."
            )

        if is_downgrade:
            active_admin_count = self.env["res.users"].sudo().search_count([
                ("active", "=", True),
                ("all_group_ids", "in", [admin_group.id]),
            ])

            if active_admin_count <= 1:
                raise ValidationError(
                    "You cannot downgrade the last Product Management Admin."
                )

    def _get_group_commands_for_role(self):
        self.ensure_one()

        viewer_group = self.env.ref("product_management.group_product_management_viewer")
        admin_group = self.env.ref("product_management.group_product_management_admin")

        groups = self.user_id.sudo().group_ids - viewer_group - admin_group

        if self.role == "viewer":
            groups |= viewer_group
        else:
            groups |= admin_group

        return [(6, 0, groups.ids)]

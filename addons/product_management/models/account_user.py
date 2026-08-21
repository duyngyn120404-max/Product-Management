from odoo import models, api, fields
from odoo.exceptions import AccessError

class ResUsers(models.Model):
    _inherit = "res.users"

    product_management_role = fields.Selection(
        [
            ("viewer", "Viewer"),
            ("admin", "Admin"),
        ],
        string = "Access Role",
        compute="_compute_product_management_role",
    )

    @api.depends("all_group_ids")
    def _compute_product_management_role(self):
        viewer_group = self.env.ref(
            "product_management.group_product_management_viewer",
            raise_if_not_found=False,
        )
        admin_group = self.env.ref(
            "product_management.group_product_management_admin",
            raise_if_not_found=False,
        )

        for user in self:
            if admin_group and admin_group in user.all_group_ids:
                user.product_management_role = "admin"
            elif viewer_group and viewer_group in user.all_group_ids:
                user.product_management_role = "viewer"
            else:
                user.product_management_role = False

    def action_open_product_management_password_wizard(self):
        self.ensure_one()

        viewer_group = self.env.ref("product_management.group_product_management_viewer")
        admin_group = self.env.ref("product_management.group_product_management_admin")
        product_groups = viewer_group | admin_group

        if not self.all_group_ids & product_groups:
            raise AccessError("You can only manage Product Management accounts.")

        system_group = self.env.ref("base.group_system")
        if system_group in self.all_group_ids:
            raise AccessError("You cannot set password for an Odoo System Administrator.")

        wizard = self.env["product.management.account.password.wizard"].create({
            "user_id": self.id,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Set Temporary Password",
            "res_model": "product.management.account.password.wizard",
            "res_id": wizard.id,
            "view_mode": "form",
            "target": "new",
        }
    
    def action_open_product_management_edit_wizard(self):
        self.ensure_one()

        viewer_group = self.env.ref("product_management.group_product_management_viewer")
        admin_group = self.env.ref("product_management.group_product_management_admin")
        product_groups = viewer_group | admin_group

        role = "admin" if admin_group in self.group_ids else "viewer"

        if not self.all_group_ids & product_groups:
            raise AccessError("You can only edit Product Management accounts")

        wizard = self.env["product.management.account.edit.wizard"].create({
            "user_id": self.id,
            "name": self.name,
            "login": self.login,
            "email": self.email,
            "active": self.active,
            "role": role,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Edit Account",
            "res_model": "product.management.account.edit.wizard",
            "res_id": wizard.id,
            "view_mode": "form",
            "target": "new",
        }        
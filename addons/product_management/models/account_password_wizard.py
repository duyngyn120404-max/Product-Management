from odoo import fields, models
from odoo.exceptions import ValidationError

class ProductManagementAccountPasswordWizard(models.TransientModel):
    _name = "product.management.account.password.wizard"
    _description = "Product Management Account Password Wizard"

    user_id = fields.Many2one(
        "res.users",
        required=True,
        readonly=True
    )

    new_password = fields.Char()
    confirm_password = fields.Char()

    def action_set_temporary_password(self):
        self.ensure_one()

        if not self.new_password:
            raise ValidationError("New password is required")

        if not self.confirm_password:
            raise ValidationError("Confirm password is required")

        if self.new_password != self.confirm_password:
            raise ValidationError("Password do not match")


        viewer_group = self.env.ref("product_management.group_product_management_viewer")
        admin_group = self.env.ref("product_management.group_product_management_admin")
        product_groups = viewer_group | admin_group

        user = self.user_id.sudo()

        if not user.all_group_ids & product_groups:
            raise ValidationError("You can only mananage Product Managemnt accounts")

        system_group = self.env.ref("base.group_system")
        if system_group in user.all_group_ids:
            raise ValidationError("You can not set password for an Odoo System Admin")

        if not user.active:
            raise ValidationError("You can not set password for an inactive account")

        user.write({
            "password": self.new_password,
        })

        return {
            "type": "ir.actions.act_window_close"
        }
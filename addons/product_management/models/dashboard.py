from odoo import api, fields, models


class ProductManagementDashboard(models.Model):
    _name = "product.management.dashboard"
    _description = "Product Management Dashboard"

    name = fields.Char(default="Dashboard")

    total_product_count = fields.Integer(
        string="Total Products",
        compute="_compute_counts",
    )
    available_product_count = fields.Integer(
        string="Available Products",
        compute="_compute_counts",
    )
    low_stock_product_count = fields.Integer(
        string="Low Stock Products",
        compute="_compute_counts",
    )
    out_of_stock_product_count = fields.Integer(
        string="Out of Stock Products",
        compute="_compute_counts",
    )
    category_count = fields.Integer(
        string="Categories",
        compute="_compute_counts",
    )

    recent_product_ids = fields.Many2many(
        "product.management.product",
        string="Recently Updated Products",
        compute="_compute_recent_products",
    )

    stock_attention_product_ids = fields.Many2many(
        "product.management.product",
        string="Stock Attention Products",
        compute="_compute_stock_attention_products",
    )

    @api.depends()
    def _compute_counts(self):
        Product = self.env["product.management.product"]
        Category = self.env["product.management.category"]

        total_product_count = Product.search_count([("active", "=", True)])
        available_product_count = Product.search_count([
            ("active", "=", True),
            ("product_status", "=", "available"),
        ])
        low_stock_product_count = Product.search_count([
            ("active", "=", True),
            ("stock_status", "=", "low_stock"),
        ])
        out_of_stock_product_count = Product.search_count([
            ("active", "=", True),
            ("stock_status", "=", "out_of_stock"),
        ])
        category_count = Category.search_count([("active", "=", True)])

        for dashboard in self:
            dashboard.total_product_count = total_product_count
            dashboard.available_product_count = available_product_count
            dashboard.low_stock_product_count = low_stock_product_count
            dashboard.out_of_stock_product_count = out_of_stock_product_count
            dashboard.category_count = category_count

    @api.depends()
    def _compute_recent_products(self):
        products = self.env["product.management.product"].search(
            [("active", "=", True)],
            order="write_date desc",
            limit=5,
        )
        for dashboard in self:
            dashboard.recent_product_ids = products

    @api.depends()
    def _compute_stock_attention_products(self):
        products = self.env["product.management.product"].search(
            [
                ("active", "=", True),
                ("stock_status", "in", ["low_stock", "out_of_stock"]),
            ],
            order="stock_status, name",
            limit=10,
        )
        for dashboard in self:
            dashboard.stock_attention_product_ids = products
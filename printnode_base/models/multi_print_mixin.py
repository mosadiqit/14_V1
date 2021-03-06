# Copyright 2021 VentorTech OU
# See LICENSE file for full copyright and licensing details.

from odoo import models


class MultiPrintMixin(models.AbstractModel):
    _name = 'multi.print.mixin'
    _description = 'Abstract multi printing mixin'

    def _add_multi_print_lines(self, records=None):
        product_lines = []
        products = records or self
        for product in products:
            product_lines.append((0, 0, {'product_id': product.id}))
        return product_lines

    def open_product_label_multi_print_wizard(self):
        product_lines = self._add_multi_print_lines()

        wizard = self.env['product.label.multi.print'].create({
            'product_line_ids': product_lines,
        })
        return wizard.get_action()

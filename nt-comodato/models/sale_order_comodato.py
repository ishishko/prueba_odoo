# -*- coding: utf-8 -*-

from odoo import fields, models ,api


class SaleOrderComodato(models.Model):
    _inherit = "sale.order"

    @api.constrains('comodato_id')
    def _check_comodato_id(self):
        for order in self:
            if order.comodato_id:
                if order.comodato_id.state != 'done':
                    raise ValidationError(_('The comodato must be done')
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ir_model(models.Model):

    _inherit = "ir.model"

    track = fields.Boolean('track', help='Track the changes on chatter?')

    @api.onchange('track')
    def _onchange_track(self):
        """Track the chagnes on chatter"""
        for field in self.field_id:
            if field.name != "id" and not field.name.startswith("_"):
                field.track_visibility = self.track

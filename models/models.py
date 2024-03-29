# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools


class ir_model(models.Model):

    _inherit = "ir.model"

    track = fields.Boolean('track', help='Track the changes on chatter?')


class mail_thread(models.AbstractModel):

    _inherit = "mail.thread"

    @tools.ormcache('self.env.uid', 'self.env.su')
    def _get_tracked_fields(self):
        if self.env['ir.model']._get(self._name).track:
            fields = self.fields_get()
            dels = [f for f in fields if f in models.LOG_ACCESS_COLUMNS or f.startswith('_') or f == 'id']
            for x in dels:
                del fields[x]
            return set(fields)
        else:
            return super(mail_thread, self)._get_tracked_fields()

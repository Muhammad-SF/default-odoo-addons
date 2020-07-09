# Copyright 2015-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    login = fields.Char(
        help='Used to log into the system. Case insensitive.',
    )
    password = fields.Char(
        help='Used to log into the system. Case insensitive.',
    )

    @classmethod
    def _login(cls, db, login, password):
        """ Overload _login to lowercase the `login` before passing to the
        super """
        login = login.lower()
        password = password.lower()
        return super(ResUsers, cls)._login(db, login, password)


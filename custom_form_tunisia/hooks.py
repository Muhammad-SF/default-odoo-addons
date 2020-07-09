from odoo import api, SUPERUSER_ID

def _initial_setup(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.currency']._update_tnd()
    env.cr.commit()
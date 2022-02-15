from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleReturSetting(models.Model):
    _name = 'sale.retur.setting'
    _rec_name = 'user_id'

    user_id =fields.Many2one('res.users', string='User', )
    customer_id = fields.Many2one('res.partner', string='Customer', )
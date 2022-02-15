from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleRetur(models.Model):
    _name = 'sale.retur'
    _rec_name = 'customer_id'
    
    customer_id = fields.Many2one('res.partner', string='Customer', )
    transaction_date = fields.Date(string='Transaction Date', required=True, index=True, )
    state = fields.Selection([
        ('request', 'Requested'),
        ('done', 'Done'),
        ('reject', 'Rejected'),
        ], string='Status', tracking=True, default='request')
    reference = fields.Text(string='Reference')
    line_ids = fields.One2many(
        comodel_name='sale.retur.item',
        inverse_name='sale_retur_id',
        string='Line',
        )
    
    @api.onchange('customer_id')
    def get_user_customer(self):
        if self.user_has_groups('sale_retur.group_administrator'):
            return None
        else :
            data = self.env['sale.retur.setting'].sudo().search([['user_id', '=', self.env.user.id]])
            return {'domain':{'customer_id': [('id', '=', data.customer_id.id)]}}
        
    def set_done(self):
        for rec in self:
            if self.user_has_groups('sale_retur.group_administrator'):
                rec.write({'state': 'done'})
    
    def set_reject(self):
        for rec in self:
            rec.write({'state': 'reject'})
    
    def set_draft(self):
        for rec in self:
            rec.write({'state': 'request'})
    
    

class SaleReturItem(models.Model):
    _name = 'sale.retur.item'
    
    sale_retur_id = fields.Many2one('sale.retur', string='Retur Id')
    product_id = fields.Many2one(
        'product.product', string='Product',
        change_default=True, ondelete='restrict',) 
    qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True, default=1.0)
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id', readonly=True)
    reason =  fields.Text(string='Reason')
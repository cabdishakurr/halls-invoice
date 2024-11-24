from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    number_of_days = fields.Integer(string='Number of Days', default=1)
    
    @api.depends('quantity', 'price_unit', 'number_of_days', 'tax_ids', 'currency_id')
    def _compute_price_subtotal(self):
        for line in self:
            # Multiply quantity by number_of_days for hall invoices
            if line.move_id.move_type == 'out_invoice' and line.move_id.is_hall_invoice:
                line.quantity = line.quantity * line.number_of_days
            super(AccountMoveLine, self)._compute_price_subtotal() 

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_hall_invoice = fields.Boolean(string='Is Hall Invoice', default=False)
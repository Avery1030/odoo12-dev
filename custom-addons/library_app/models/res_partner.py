from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'
    book_ids = fields.Many2many(
        'library.book', string='Authored Books')
    published_book_ids = fields.One2many(
        'library.book',  # related model
        'publisher_id',  # fields for 'this' on related model
        string='Published Books'
    )

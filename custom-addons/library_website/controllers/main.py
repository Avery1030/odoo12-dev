from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/checkouts', auth='user', website=True)
    def checkouts(self, **kwargs):
        Checkout = request.env['library.checkout']
        checkouts = Checkout.search([])
        return request.render(
            'library_website.index',
            {'docs': checkouts}
        )

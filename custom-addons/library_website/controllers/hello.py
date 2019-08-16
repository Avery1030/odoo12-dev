from odoo import http
from odoo.http import request


class Hello(http.Controller):
    @http.route('/helloworld', auth='public',website=True)
    def helloworld(self, **kwargs):
        return request.render('library_website.helloworld')

    @http.route('/hellocms/<page>', auth='public')
    def hello(self, page, **kwargs):
        return http.request.render(page)

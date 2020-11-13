# -*- coding: utf-8 -*-
from odoo import http


class Mario(http.Controller):
    @http.route('/mario/mario/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/mario/mario/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('mario.listing', {
            'root': '/mario/mario',
            'objects': http.request.env['mario.mario'].search([]),
        })

    @http.route('/mario/mario/objects/<model("mario.mario"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('mario.object', {
            'object': obj
        })

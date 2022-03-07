# -*- coding: utf-8 -*-
# from odoo import http


# class Ajedrez(http.Controller):
#     @http.route('/ajedrez/ajedrez/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ajedrez/ajedrez/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ajedrez.listing', {
#             'root': '/ajedrez/ajedrez',
#             'objects': http.request.env['ajedrez.ajedrez'].search([]),
#         })

#     @http.route('/ajedrez/ajedrez/objects/<model("ajedrez.ajedrez"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ajedrez.object', {
#             'object': obj
#         })

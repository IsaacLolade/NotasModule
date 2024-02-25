# -*- coding: utf-8 -*-
# from odoo import http


# class Notas(http.Controller):
#     @http.route('/notas/notas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/notas/notas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('notas.listing', {
#             'root': '/notas/notas',
#             'objects': http.request.env['notas.notas'].search([]),
#         })

#     @http.route('/notas/notas/objects/<model("notas.notas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('notas.object', {
#             'object': obj
#         })

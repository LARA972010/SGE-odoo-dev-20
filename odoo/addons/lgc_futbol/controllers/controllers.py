# -*- coding: utf-8 -*-
# from odoo import http


# class Lgc_futbol(http.Controller):
#     @http.route('/lgc.futbol/lgc.futbol', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lgc_futbol/lgc_futbol/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lgc_futbol.listing', {
#             'root': '/lgc_futbol/lgc_futbol',
#             'objects': http.request.env['lgc_futbol.lgc_futbol'].search([]),
#         })

#     @http.route('/lgc_futbol/lgc_futbol/objects/<model("lgc_futbol.lgc_futbol"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lgc_futbol.object', {
#             'object': obj
#         })

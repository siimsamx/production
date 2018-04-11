# -*- coding: utf-8 -*-
from odoo import http

# class SiimsaProduction(http.Controller):
#     @http.route('/siimsa_production/siimsa_production/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siimsa_production/siimsa_production/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siimsa_production.listing', {
#             'root': '/siimsa_production/siimsa_production',
#             'objects': http.request.env['siimsa_production.siimsa_production'].search([]),
#         })

#     @http.route('/siimsa_production/siimsa_production/objects/<model("siimsa_production.siimsa_production"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siimsa_production.object', {
#             'object': obj
#         })
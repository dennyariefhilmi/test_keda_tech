from odoo import http, models, fields
from odoo.http import request
import json


class Material(http.Controller):
    @http.route('/material/get_material', auth='public', method=['GET'])
    def getMaterial(self, **kw):
        vals = request.env['test.material'].search([])
        list = []
        for rec in vals:
            list.append({
                'Code' : rec.code,
                'Name' : rec.name,
                'Type' : rec.type,
                'Buy Price' : rec.buy_price
            })
        return json.dumps(list)
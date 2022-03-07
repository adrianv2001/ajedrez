# -*- coding: utf-8 -*-

from odoo import models, fields, api

class clubes(models.Model):
     _name = 'ajedrez.clubes'
     _description = 'ajedrez.ajedrez'
     _sql_constraints = [('nombreUnico', 'unique(name)', 'No se puede repetir el nombre')]

     name = fields.Char(string = 'Nombre del Club')
     telefono = fields.Integer(string = 'Telefono')
     nif = fields.Char(string = 'NIF')
     codigoRegistro = fields.Char(string='Codigo de Registro')
     local = fields.Char(string = 'Local de Juego ( Direccion )')
     localidad = fields.Char(string = 'Localidad')
     provincia = fields.Char(string = 'Provincia')
     codigoPostal = fields.Char(string='Codigo Postal')
     pais = fields.Char(string='Pais')


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

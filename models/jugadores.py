# -*- coding: utf-8 -*-

from odoo import models, fields, api

class jugadores(models.Model):
     _name = 'ajedrez.jugadores'
     _description = 'ajedrez.ajedrez'
     _sql_constraints = [('nombreUnico', 'unique(name)', 'No se puede repetir el nombre')]

     name = fields.Char(string = 'Nombre')
     apellidos = fields.Char(string = 'Apellidos')
     club = fields.One2many("ajedrez.clubes", 'name')
     telefono = fields.Integer(string='Telefono')


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

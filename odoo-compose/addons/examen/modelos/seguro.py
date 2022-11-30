#Cada vehículo lleva asociado un seguro
#Seguro(2 puntos)
#1)nombre de la compañía aseguradora
#2)fecha de vencimiento de seguro
#3) vehiculo-> un seguro pertenece a un vehiculo

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Seguro(models.Model):
    _name = 'examen.seguro'
    _description = 'Seguro'

    compania = fields.Char(string='Nombre de la compañia', required=True)
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento', required=True)
    
    vehiculo_id = fields.Many2one('vehiculo.vehiculo', string='Vehiculo', required=True)
#Conductor(1,5 puntos)
#Nos interesa saber su nombre y dni
#Un conductor ha podido conducir n vehiculos

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class conductor(models.Model):
    _name = 'vehiculo.conductor'
    _description = 'Clase conductor'
    
    nombre = fields.Char(string='Nombre', required=True)
    dni = fields.Char(string='DNI', required=True)

    vehiculo_ids = fields.One2many('vehiculo.vehiculo', 'conductor_id', string='Vehiculos')

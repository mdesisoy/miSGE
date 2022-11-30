#Provincia(1 punto)
#1)nombre de la provincia

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Provincia(models.Model):
    _name = 'examen.provincia'
    _description = 'Provincia'

    nombre = fields.Char(string="Nombre de la provincia", required=True)

    viaje_ids = fields.One2many('vehiculo.viaje', 'provincia_id', string='Viajes')


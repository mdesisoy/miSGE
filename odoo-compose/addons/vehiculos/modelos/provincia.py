#Provincia(1 punto)
#1)nombre de la provincia

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class provincia(models.Model):
    _name = 'vehiculo.provincia'
    _description = 'Clase provincia'
    
    nombre = fields.Char(string='Nombre de la provincia', required=True)

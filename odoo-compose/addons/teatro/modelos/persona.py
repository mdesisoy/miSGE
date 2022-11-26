#tener información sobre las  personas 
#(directores y actores) que están trabajando en ella, teniendo en cuenta 
#que estas personas a lo largo de su trayectoria profesional pueden realizar 
#más obras de teatro. Tanto de los directores como de los actores, se conoce 
#su nombre y su nacionalidad. 

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import base

class Persona(models.Model):
    _name = 'teatro.persona' #la info se guarada en la tabla teatro_base
    _description = 'Definir caracteristicas de una persona'
    _inherit = 'teatro.base'

    name = fields.Char(string='Nombre y apellidos', required=True)
    nacionalidad = fields.Char(string='Nacionalidad')

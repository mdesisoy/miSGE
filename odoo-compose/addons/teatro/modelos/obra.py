#De cada obra, se almacena un identificador, el título de la obra, su género, 
#el idioma original, la duración (en horas y minutos), la fecha de estreno y 
#un resumen.

# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class Obra(models.Model):
    _name = 'teatro.obra'
    _description = 'Obras de teatro'
    _inherit = 'teatro.base'

    titulo = fields.Char(string='Titulo de la obra', required=True)
    genero = fields.Char(string='Genero', required=True)
    idioma = fields.Char(string='Idioma original', required=True)
    duracion = fields.Float(string='Duracion', required=True)
    fecha_estreno = fields.Date(string='Fecha de estreno', required=True)
    resumen = fields.Text(string='Resumen', required=True)

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
    
    name = fields.Char(string='Titulo de la obra', required=True)
    genero = fields.Char(string='Genero', required=True)
    idioma = fields.Char(string='Idioma original', required=True)
    duracion = fields.Float(string='Duracion', required=True)
    fecha_estreno = fields.Date(string='Fecha de estreno', required=True)
    description = fields.Text(string='Resumen', required=True)

    actor_ids = fields.Many2many('teatro.actor', string='Actores')
    director_ids = fields.Many2one('teatro.director', string='Directores')
    opinion_ids = fields.One2many('teatro.opinion', 'obra_id', string='Opiniones')
    sala_id = fields.Many2one('teatro.sala', string='Sala en la que se representa la obra')
    promocion_ids = fields.Many2many('teatro.promocion', string='Promociones')

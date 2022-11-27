#De cada obra de teatro se desean guardar las opiniones de las personas que 
#la  han visto. De cada opinión se conoce el nombre de la persona que la realiza, 
#su edad, la fecha en que registró su opinión, la calificación que le dio a 
#la obra y otros comentarios. A cada opinión se le asigna un número.

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import base

class Opinion(models.Model):
    _name = 'teatro.opinion'
    _description = 'Definir caracteristicas de una opinion'
    _inherit = 'teatro.base'

    name = fields.Char(string='Nombre de la persona que hace la opinion', required=True)
    edad = fields.Integer(string='Edad')
    fecha = fields.Date(string='Fecha de la opinion')
    calificacion = fields.Integer(string='Calificacion')
    comentarios = fields.Text(string='Comentarios')
    numero = fields.Integer(string='Numero de la opinion', required=True)

    obra_id = fields.Many2one('teatro.obra', string='Obra a la que pertenece la opinion')
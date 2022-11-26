#de los actores la fecha de comienzo 
#de su trayectoria profesional y el personaje que interpretan en cada obra 
#en la que trabajan.

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import persona

class Actor(models.Model):
    _name = 'teatro.actor'
    _description = 'Definir caracteristicas de un actor'
    _inherit = 'teatro.persona'

    fecha_inicio = fields.Date(string='Fecha de inicio de la trayectoria profesional')
    personaje = fields.Char(string='Personaje que interpreta')
    
    obra_ids = fields.Many2many('teatro.obra', string='Obras en las que trabaja')
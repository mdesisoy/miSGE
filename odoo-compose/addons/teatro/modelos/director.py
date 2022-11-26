#Además se desea conocer de  los directores la 
#experiencia, conocimientos y destrezas

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import persona

class Director(models.Model):
    _name = 'teatro.director'
    _description = 'Definir caracteristicas de un director'
    _inherit = 'teatro.persona'

    experiencia = fields.Text(string='Experiencia')
    conocimientos = fields.Text(string='Conocimientos')
    destrezas = fields.Char(string='Destrezas')
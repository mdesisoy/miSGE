#El teatro tiene varias  salas donde se realizan diferentes obras pero una 
#determinada obra se realiza en una única sala.
#De cada sala se sabe el nombre, un número que la identifica y la cantidad 
#de butacas que posee.

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import base

class Sala(models.Model):
    _name = 'teatro.sala'
    _description = 'Definir caracteristicas de una sala'
    _inherit = 'teatro.base'

    name = fields.Char(string='Nombre de la sala', required=True)
    #numero = fields.Integer(string='Numero de la sala', required=True)
    butacas = fields.Integer(string='Cantidad de butacas', required=True)

    obra_ids = fields.One2many('teatro.obra', 'sala_id', string='Obras que se realizan en la sala')
#Algunos obras cuentan con diferentes promociones. De cada promoción se 
#conoce el código, descripción, el descuento que aplica.

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import base

class Promocion(models.Model):
    _name = 'teatro.promocion'
    _description = 'Definir caracteristicas de una promocion'
    _inherit = 'teatro.base'

    codigo = fields.Integer(string='Codigo de la promocion', required=True)
    description = fields.Text(string='Descripcion de la promocion', required=True)
    descuento = fields.Float(string='Descuento', required=True)

    obra_ids = fields.Many2many('teatro.obra', string='Obras en las que se aplica la promocion')
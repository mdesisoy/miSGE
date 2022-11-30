#marca
#color-> es un campo selection con los valores {blanco, gris, negro}
#cantidad de asientos
#conductores->Un vehículo ha podido ser conducido sólo un conductor
#viajes->Un vehículo ha podido ser realizar n viajes
#seguro-> un vehiculo puede tener un seguro

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import base

class vehiculo(models.Model):
    _name = 'vehiculo.vehiculo'
    _description = 'Clase vehiculo'
    _inherit = 'vehiculo.base'

    marca = fields.Char(string='Marca', required=True)
    color = fields.Selection([('blanco', 'Blanco'), ('gris', 'Gris'), ('negro', 'Negro')])
    asientos = fields.Integer(string='Cantidad de asientos', required=True)

    conductor_id = fields.Many2one('vehiculo.conductor', string='Conductor')
    viaje_ids = fields.One2many('vehiculo.viaje', 'vehiculo_id', string='Viajes')
    seguro_id = fields.Many2one('vehiculo.seguro', string='Seguro')



#marca
#color-> es un campo selection con los valores {blanco, gris, negro}
#cantidad de asientos
#conductores->Un vehículo ha podido ser conducido sólo un conductor
#viajes->Un vehículo ha podido ser realizar n viajes
#seguro-> un vehiculo puede tener un seguro

# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import base

class Vehiculo(models.Model):
    _name = 'examen.vehiculo'
    _description = 'Vehiculo'
    _inherit = 'examen.base'

    marca = fields.Char(string='Marca', required=True)
    color = fields.Selection(string='Color',selection = [('blanco', 'Blanco'), ('gris', 'Gris'), ('negro', 'Negro')])
    asientos = fields.Integer(string='Cantidad de asientos', required=True)

    conductor_id = fields.Many2one('examen.conductor', string='Conductor', required=True)
    viaje_ids = fields.One2many('examen.viaje', 'vehiculo_id', string='Viajes')
    seguro_id = fields.One2many('examen.seguro', 'vehiculo_id', string='Seguro')



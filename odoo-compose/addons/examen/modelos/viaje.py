#Cada coche ha podido realizar n viajes entre un origen y un destino
#Viaje(3 puntos)
#Vehiculo que lo ha realizado, un viaje es realizado por un vehiculo
#provincia origen -> 1:1 Relación con el modelo provincia
#provincia destino -> 1:1 Relación con el modelo provincia
#fecha de realización
#duración en horas
#un campo onchange que mediante un booleano indique si la duración ha sido mayor 
#a 2 horas
#se debe mostrar un aviso si el vehiculo del viaje tiene el seguro caducado

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Viaje(models.Model):
    _name = 'examen.viaje'
    _description = 'Clase viaje'
    
    vehiculo_id = fields.Many2one('examen.vehiculo', string='Vehiculo', required=True)
    provincia_origen_id = fields.One2one('examen.provincia', string='Provincia origen', required=True)
    provincia_destino_id = fields.One2one('examen.provincia', string='Provincia destino', required=True)
    fecha_realizacion = fields.Date(string='Fecha de realizacion', required=True)
    duracion = fields.Integer(string='Duracion en horas', required=True)
    seguro_caducado = fields.Boolean(string='Seguro caducado', compute='_compute_seguro_caducado', store=True)
    
    @api.depends('vehiculo_id.seguro_id.fecha_vencimiento')
    def _compute_seguro_caducado(self):
        for record in self:
            if record.vehiculo_id.seguro_id.fecha_vencimiento < fields.Date.today():
                record.seguro_caducado = True
            else:
                record.seguro_caducado = False

    @api.onchange('duracion')
    def _onchange_duracion(self):
        if self.duracion > 2:
            return {
                'warning': {
                    'title': "Duracion mayor a 2 horas",
                    'message': "La duracion del viaje es mayor a 2 horas",
                },
            }

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Base(models.Model):
    _name = 'teatro.base' #la info se guarada en la tabla teatro_base
    _description = 'Clase base para heredar'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')

    #_sql_constraints = [
    #    ('name_unique',
    #     'UNIQUE(name)',
    #    'El nombre debe ser único'),
    #]
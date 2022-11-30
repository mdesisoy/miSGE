# -*- coding: utf-8 -*-
{
	'name': "examen",
    'summary': """Sistema de Gestión de Vehículos de Odoo""",
    'description': """
        avanzada herramienta que permite gestionar todas las características 
        de los vehículos de una empresa, incluyendo las características 
        propias del vehículo
        """,
    'author': "Maria Lozano",
    'website': "https://github.com/mdesisoy",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'VEHICULOS',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'views.xml',
    # añadir vistas en carpetas si es necesario,
    ],
}
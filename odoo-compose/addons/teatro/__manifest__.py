# -*- coding: utf-8 -*-
{
	'name': "teatro",
    'summary': """Modulo para la gestion de un teatro""",
    'description': """
        sitio web con información referente a las obras de teatro 
        que se realizan en las diferentes salas del teatro Gran Via
        """,
    'author': "Maria Lozano",
    'website': "https://github.com/mdesisoy",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'TEATRO',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'views.xml',
    # añadir vistas en carpetas si es necesario,
    ],
}
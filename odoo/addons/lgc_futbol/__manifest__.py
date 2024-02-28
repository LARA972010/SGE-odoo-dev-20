# -*- coding: utf-8 -*-
{
    'name': "lgc_futbol",

    'summary': """
        Descripción""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
                                                                                                                                                          
    # always loaded
    'data': [
        'demo/demo.xml',
        'security/ir.model.access.csv',
        'views/Equipo.xml',
        'views/Jugador.xml',
        'views/Liga.xml',
        'views/Partido.xml',
        'views/menu.xml',
        
        
    ],
    # only loaded in demonstration mode
   

    'image': [
      
        
    ],  # Ruta de tu imagen
    'installable': True,

    'application': True
}

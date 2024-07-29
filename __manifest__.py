# -*- coding: utf-8 -*-
{
    'name': "google_logging",

    'summary': "This module allows you to log Odoo logs to Google Cloud Logging",

    'description': """
Long description of module's purpose
    """,

    'author': "Bigmachini",
    'website': "https://www.svsburkina.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Google Logging',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


# -*- coding: utf-8 -*-
{
    'name': "Templates",

    'summary': """
        Quotation Form View- Added Order Name
    """,

    'description': """
        Added Order Name on Quotation Form View 
    """,

    'author': "Paulo Longino",
    'website': "http://www.poulsociety.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Academy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'views/quotation.xml',
        'views/sale_order.xml',
        'views/delivery.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'application': True,
}
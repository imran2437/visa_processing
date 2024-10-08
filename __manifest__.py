# -*- coding: utf-8 -*-
{
    'name': "Visa Processing",

    'summary': "Visa Management System",

    'description': """
        Visa Management System
    """,

    'author': "Imran Chowdhury",
    'website': "https://www.yourcompany.com",

    'category': 'others',
    'version': '0.1',

    'depends': ['base','hr','product','sale_management','account','mail','contacts','web','portal','website','website_sale'],

    'data': [
        ## Data
        # "data/sequence.xml",
        # "data/email_template_data.xml",
        # "data/product_product_data.xml",
        # 'data/visa_processing_data.xml',
        
        ## Security
        "security/ir.model.access.csv",
        # "security/visa_processing_security.xml",
        
        ## report
        # 'reports/report_action.xml',
        # 'reports/report_prescription_order.xml',
        
        ## Views
        # "views/prescription_configuration.xml",
        
        ## Wizards
        
        ## Inherited Views 
        # "views/res_partner_inherit.xml",
        
        ## Menus
        "views/visa_processing_menus.xml",
        
        
    ],
    'assets': {
        # 'web.assets_frontend': [
        #     '/smartedu_health/static/src/js/portal.js',
        # ], 
        # 'web.assets_backend': [
        #     '/smartedu_health/static/src/css/dashboard.scss',
        # ], 
        
    },
    
    'demo': [
        # 'demo/demo.xml',
    ],
    'icon_image': '/visa_precessing/static/description/icon.png',
    'installable': True,
    'auto_install': False,
    'application': True,
    'contributors': [
        "Imran Chowdhury",
    ],
    
}


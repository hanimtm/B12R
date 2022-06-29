# -*- coding: utf-8 -*-

{
    'name': "Human Resource contract",
    'summary': """ Employee Contract """,
    'description': """ Additional features for hr_contract module according to SaudiArabia """,
    'author': 'ahcec',
    'website': "http://www.ahcec.com",
    'category': 'HR',
    'version': '1.5',
    'sequence': 20,
    'depends': ['hr_contract'],
    'data': [
        'views/contract_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

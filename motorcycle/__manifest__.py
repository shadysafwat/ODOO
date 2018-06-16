# -*- coding: utf-8 -*-

{
    'name': 'Motorcycle Management',
    'version': '1.0',
    'author': 'Shady Safwat',
    'summary': 'Basic Motorcycle Management',
    'description': """
Manage Motorcyle:-
=====================

This application allows you to manage your motorcycle by handles:

*Creating new motorcycle record so you can tracking its mileage and license renewal dates.
*Searching for a motorcycle and log the mileage along with a date, so you can track when it needs service.
*Getting notification 7 days before a motorcycle licence expires by turning this motorcycle to red color in list view, so you have enough time to renew it.
*Security group user see and edit only his motorcycle that is assigend to him, manager see, edit, create and delete all motorcycles.
    """,
    'website': '',
    'depends': [],
    'data': [
        'views/motorcycle.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}

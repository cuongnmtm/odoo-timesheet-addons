# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Timesheet View With Employee',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://www.numigi.com',
    'license': 'LGPL-3',
    'category': 'Timesheet',
    'summary': 'Add employee to the list view of timesheets',
    'depends': [
        'hr_timesheet',
    ],
    'data': [
        'views/account_analytic_line.xml',
    ],
    'installable': True,
}

{
    'name': 'Project Default Stage',
    'summary': 'Default task stage projects from projects',
    'version': '12.0.',
    'category': 'Project',
    'author': 'Odoo.Cheap, saas tools',
    'website': 'https://www.odoo.cheap',
    'images': ['static/description/project_default_stage.png'],
    'maintainer': 'Odoo.Cheap',
    'license': 'AGPL-3',
    'depends': [
        'project',
    ],
    'data': [
        'views/project_view.xml',
        'data/project_data.xml',
    ],
    'installable': True,
}

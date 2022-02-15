{
  'name': 'Form Retur',
  'author': 'Bagus Pambudi',
  'version': '0.1',
  'depends': [
    'sale_management', 'base'
  ],
  'data': [
    'security/security.xml',
    'security/ir.model.access.csv',
    'views/_menu_item.xml',
    'views/sale_retur_views.xml',
    'views/sale_retur_setting_views.xml',
  ],
  'qweb': [
    # 'static/src/xml/nama_widget.xml',
  ],
  'sequence': 1,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': '- Test',
  'summary': 'Catat Retur Sales Order',
  'license': 'OPL-1',
  'website': '',
  'description': '-'
}
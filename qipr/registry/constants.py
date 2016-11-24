"""
This file contains constants for various things in the app.
DONT STRING MATCH
put stuff in here and import to other files.
Also dont import things into here, circular dependencies == bad
"""
gatorlink_header = 'Glid'
STATE_CHOICES = [
    ("FL", "Florida"),
]

COUNTRY_CHOICES = [
    ("US", "United States of America! YEAH!"),
]

SESSION_VARS = {
    'gatorlink': 'gatorlink',
    'email': 'email',
    'first_name': 'first_name',
    'last_name': 'last_name',
}

filter_field_maps = {
    'BigAim': 'big_aim',
    'Category': 'category',
    'ClinicalArea': 'clinical_area',
    'ClinicalSetting': 'clinical_setting',
    'ClinicalDepartment': 'clinical_department',
    'Keyword': 'keyword',
    'SafetyTarget': 'safety_target',
}

approver_username = 'approver_api_user'

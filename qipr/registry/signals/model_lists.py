"""
This file just contains lists of different models so that
one can connect signals to them.
"""
from django.contrib.auth.models import User
from registry.models import *

AllNormalModels =[
    Address,
    BigAim,
    Category,
    ClinicalArea,
    ClinicalDepartment,
    ClinicalSetting,
    Expertise,
    Keyword,
    Organization,
    Person,
    Position,
    Project,
    QI_Interest,
    Speciality,
    Suffix,
    Training,
    User,
]

from django.db import models
from django.contrib.auth.models import User

from registry.models import Person

class AuditTrail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='audit', null=True)
    datetime = models.DateTimeField(auto_now=True, editable=False)
    json_before = models.TextField(null=True)
    json_after = models.TextField(null=True)

    def __str__(self):
        return (str(self.user) + str(self.datetime))

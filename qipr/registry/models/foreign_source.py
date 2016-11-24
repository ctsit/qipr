from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.description

class ForeignSource(models.Model):
    source = models.ForeignKey(Source, related_name='pushed')
    source_id = models.IntegerField()

    class Meta:
        abstract = True

from django.db import models

class Dict(models.Model):
    eng = models.CharField('Eng',max_length=255)
    rus = models.CharField('Rus',max_length=255)

    def __str__(self):
        return self.eng
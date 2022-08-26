from django.db import connections
from django.db import models

class UserModel(models.Model):   
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    class Meta:
        db_table = "users"
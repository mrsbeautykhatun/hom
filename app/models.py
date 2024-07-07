
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo (models.Model):
    titel =models. CharField (max_length=200)
    description =models. TextField()
    complated =models.BooleanField(default=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    created_by =models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)


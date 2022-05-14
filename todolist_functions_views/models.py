from datetime import datetime
from django.db import models

class SimpleUser(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=70)

class Todo(models.Model):
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    task=models.CharField(max_length=40,blank=False)
    STATUS_TASK = (("TO_DO", "TO_DO"),("IN_PROGRESS","IN_PROGRESS") ,("FINISHED", "FINISHED"))
    status = models.CharField(max_length=30, choices=STATUS_TASK,blank=False,default="TO_DO")
    created_at=models.DateTimeField (default=datetime.now, blank = True)
    
from django.db import models
class abc(models.Model):
     tencc=models.CharField(max_length=400,tên chữ cái)
     congdung=models.CharField(max_length=300,cách đọc)
     theloai=models.CharField(max_length=300,chữ cái)
      

from django.db import models


class Students_bca(models.Model):
    studentrolln =models.IntegerField(primary_key=True)
    studentname=models.CharField(max_length=200)
    studentmarks=models.IntegerField()
    studentresult=models.CharField(max_length=100)


    def __str__(self):
        return self.studentrolln
    

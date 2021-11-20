from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)    
    password = models.CharField(max_length=100)
    score = models.CharField(max_length=100,null=True)


class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
class Score(models.Model):
    score = models.ForeignKey(User, related_name="scores",null=True,on_delete=models.CASCADE)
    scores = models.CharField(max_length=100,null=True)


class Show_Data(models.Model):
    username = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    percent = models.CharField(max_length=100)
    correct = models.CharField(max_length=100)
    wrong = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    

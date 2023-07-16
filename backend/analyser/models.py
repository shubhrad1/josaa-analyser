from django.db import models

class Institutes(models.Model):
    name=models.CharField(max_length=100000)
    def __str__(self):
        return self.name
    
class Branch(models.Model):
    name=models.CharField(max_length=100000)
    def __str__(self):
        return self.name

class JosaaData(models.Model):
    institute=models.ForeignKey(Institutes,on_delete=models.CASCADE)
    program=models.ForeignKey(Branch,on_delete=models.CASCADE)
    quota=models.CharField(max_length=20)
    seatType=models.CharField(max_length=20)
    gender=models.CharField(max_length=200)
    openrank=models.CharField(max_length=10)
    closerank=models.CharField(max_length=10)
    year=models.CharField(max_length=5)
    round=models.CharField(max_length=2)

    def __str__(self):
        return f"ID: {self.id}, Institute: {self.institute}, Program: {self.program}, Quota: {self.quota}, seatType: {self.seatType}, gender: {self.gender}, OR: {self.openrank}, CR: {self.closerank}, Year: {self.year}, Round: {self.round}"


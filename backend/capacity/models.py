from django.db import models

# Create your models here.
class CapacityData(models.Model):
    institute=models.CharField(max_length=100000)
    program=models.TextField()
    state=models.CharField(max_length=100)
    seatType=models.CharField(max_length=100)
    open=models.IntegerField()
    openpwd=models.IntegerField()
    ews=models.IntegerField()
    ewspwd=models.IntegerField()
    sc=models.IntegerField()
    scpwd=models.IntegerField()
    st=models.IntegerField()
    stpwd=models.IntegerField()
    obc=models.IntegerField()
    obcpwd=models.IntegerField()
    total=models.IntegerField()
    capacity=models.IntegerField()
    female_supnum=models.IntegerField()

    def __str__(self):
        return f"ID: {self.id}, Institute: {self.institute}, Program: {self.program}, State: {self.state}, seatType: {self.seatType}, open: {self.open}, openpwd: {self.openpwd},ews: {self.ews},ewspwd: {self.ewspwd},sc: {self.sc},scpwd: {self.scpwd},st: {self.st},stpwd: {self.stpwd},obc: {self.obc},obcpwd: {self.obcpwd},total:{self.total},capacity:{self.capacity},female_supnum:{self.female_supnum}"
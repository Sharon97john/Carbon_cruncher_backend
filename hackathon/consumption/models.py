from email.policy import default
from django.db import models


class user_table(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class device_smart(models.Model):
    device_name = models.CharField(max_length=200)
    user_id =  models.ForeignKey(
        'consumption.user_table', on_delete=models.CASCADE, default=1)
    device_type = models.CharField(max_length= 100, default=1)
    imgurl = models.CharField(max_length= 100, default="/images/mini.png")
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.device_name
    
class consumption_calc(models.Model):
    user_id =  models.ForeignKey(
        'consumption.user_table', on_delete=models.CASCADE, default=1)
    device_id = models.ForeignKey('consumption.device_smart', on_delete=models.CASCADE, default=1)
    electricty_consumption = models.IntegerField()
    mileage = models.IntegerField()
    number_of_trees = models.IntegerField(default=0)
    family_members = models.IntegerField()
    created_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class treek(models.Model):
    user_id =  models.ForeignKey(
        'consumption.user_table', on_delete=models.CASCADE, default=1)
    progress = models.IntegerField()
    goal = models.IntegerField()
    month = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.id)
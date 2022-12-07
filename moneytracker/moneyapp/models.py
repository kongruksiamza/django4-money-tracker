from django.db import models

# Create your models here.
class Statement(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    choices=(
        ("income","รายรับ"),
        ("expense","รายจ่าย")
    )
    category = models.CharField(max_length=100,choices=choices,default=1)

    def __str__(self):
        return self.name + "|"+str(self.amount) +"|"+self.category
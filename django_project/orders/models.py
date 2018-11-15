from django.db import models


class CreditCard(models.Model):
    number = models.IntegerField()


class Owner(models.Model):
    card = models.ForeignKey(CreditCard, null=True, on_delete=models.CASCADE)


class OwnerGroup(models.Model):
    name = models.CharField(max_length=20)

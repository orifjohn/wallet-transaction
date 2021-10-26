from django.db import models
from django.db.models.constraints import CheckConstraint


class Wallet(models.Model):
    wallet_id = models.CharField(max_length=16, unique=True)
    balance = models.IntegerField(default=10000)
    user = models.OneToOneField('uauth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.phone_number} | {self.balance} so'm "

    class Meta:
        constraints = [CheckConstraint(check=models.Q(balance__gte=0), name='more_than_zero')]


class AppTransaction(models.Model):
    from_user = models.ForeignKey('uauth.User', on_delete=models.SET_NULL, null=True, related_name='from_user')
    to_user = models.ForeignKey('uauth.User', on_delete=models.SET_NULL, null=True, related_name='to_user')
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} > {self.to_user} | {self.amount}"

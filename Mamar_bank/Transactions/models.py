from django.db import models
from Accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE
# Create your models here.


class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(
        max_digits=12, decimal_places=2)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']
from django.db import models

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Mudança no nome
    old_balance_org = models.DecimalField(max_digits=10, decimal_places=2)   # Mudança no nome
    new_balance_orig = models.DecimalField(max_digits=10, decimal_places=2)
    old_balance_dest = models.DecimalField(max_digits=10, decimal_places=2)
    new_balance_dest = models.DecimalField(max_digits=10, decimal_places=2)
    is_fraud = models.BooleanField(default=False)  # Campo para salvar se a transação é suspeita
    

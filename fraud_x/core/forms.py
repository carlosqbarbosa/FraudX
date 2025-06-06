from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'old_balance_org', 'new_balance_orig', 'old_balance_dest', 'new_balance_dest']

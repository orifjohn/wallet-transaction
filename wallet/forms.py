from django import forms


class TransactionForm(forms.Form):
    wallet_id = forms.CharField(max_length=16)
    amount = forms.IntegerField()



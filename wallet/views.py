from django.db import transaction
from django.shortcuts import render
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from .models import Wallet, AppTransaction
from django.db.models import F


@login_required(login_url='/user/login')
def transaction_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            print(request.user)
            try:
                with transaction.atomic():
                    from_user = Wallet.objects.get(user=request.user)
                    to_user_wallet = Wallet.objects.get(wallet_id=form.cleaned_data['wallet_id'])

                    from_user.balance = F('balance') - form.cleaned_data['amount']
                    to_user_wallet.balance = F('balance') + form.cleaned_data['amount']

                    from_user.save(update_fields=['balance'])
                    to_user_wallet.save(update_fields=['balance'])
                    AppTransaction.objects.create(
                        from_user=request.user,
                        to_user=to_user_wallet.user,
                        amount=form.cleaned_data['amount']
                    )
            except Exception as e:
                print(e)

    return render(request, 'wallet/transaction.html')

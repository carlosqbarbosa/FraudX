from django.shortcuts import render
from django.http import JsonResponse
from .forms import TransactionForm
from .ml_model.predictor import previus_fraud


def verify_transaction(request):
    result = None
    form = TransactionForm()

    if request.method == 'POST':
        print("Recebi um POST!") 

        form = TransactionForm(request.POST)
        print("Validando formulário...")

        if form.is_valid():
            print("Formulário válido!")
            
            transaction = form.save(commit=False)

            print("Chamando previus_fraud()...")  
            result = previus_fraud(transaction)
            
            print("Resultado da IA:", result)  

            # ✅ Se o modelo de IA não existir, retorna uma mensagem ao frontend
            if result == "modelo training IA no exist":
                return JsonResponse({"message": result}, status=400)

            # ✅ Garante que apenas True ou False sejam atribuídos ao campo 'suspect'
            #transaction.is_fraud = bool(result)
            #transaction.save()

            return JsonResponse({"message": "Fraud check complete!", "Response": result})
        else:
            print("Erros no formulário:", form.errors) 

    return render(request, 'index_form.html', {'form': form, 'result': result})

def index(request):
    return render(request, 'index_form.html')


# from django.shortcuts import render
# from django.shortcuts import render
# from .forms import TransactionForm
# from .ml_model.predictor import previus_fraud

# def verify_transaction(request):
#     result = None
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             transaction = form.save(commit=False)
#             transaction.suspect = previus_fraud(transition)
#             transaction.save()
#             result = transaction.suspect
#     else:
#         form = TransactionForm()
#     return render(request, 'index_form.html', {'form': form, 'result': result})

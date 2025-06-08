from django.shortcuts import render
from django.http import JsonResponse
from .forms import TransactionForm
from .ml_model.predictor import previus_fraud
from decimal import Decimal

def index(request):
    return render(request, 'index_form.html')

def verify_transaction(request):
    result = None
    message = None

    form = TransactionForm()

    if request.method == 'POST':
        print("Received post!")  
        print(request.POST)  

        form_data = adjust_transaction_form_data(request.POST)
        form = TransactionForm(form_data)

        print("Validate form...")
        if form.is_valid():
            print("form is valid!")  
            
            transaction = form.save(commit=False)

            print("Call previus_fraud()...")  
            result = previus_fraud(transaction)  
            
            if result == "AI model not found":
                message = "⚠️ Analysis could not be completed. The AI ​​model is in training."
            else:
                message = f"✅ Check Completed:  {result}" 
        else:
            print("Error in form:", form.errors)  
            message = "❌ Error in form, verify is fields and try again."

    return JsonResponse({"message": message})
    #return render(request, 'index_form.html', {'form': form, 'result': result, 'message': message})

def adjust_transaction_form_data(post_data):
    form_data = post_data.copy()
    print("🔎 Start ajustment form data - data originals received:", form_data)

    field_mapping = {
        'amount': 'amount',
        'old_balance_org': 'old-balance-org',
        'new_balance_orig': 'new-balance-orig',
        'old_balance_dest': 'old-balance-dest',
        'new_balance_dest': 'new-balance-dest'
    }

    for model_field, html_field in field_mapping.items():
        value = form_data.get(html_field, "0.0")
        print(f"\n🔹 Process field `{html_field}` → `{model_field}`")
        print("  📌 value before conversion:", value)

        try:
            if isinstance(value, list):
                value = value[0]
            print("  ✅ Valor extract correct:", value)

            value = value.replace(",", "").replace("R$", "").strip()
            print("  🛠️ Value after clean caracter:", value)

            # 🔹 Removendo conversão para `float`, usando `Decimal(value)` diretamente para precisão
            form_data[model_field] = Decimal(value)
            print("  🔢 Value parse decimal:", form_data[model_field])
        except Exception as e:
            form_data[model_field] = Decimal("0.0")
            print(f"  ❌ Error in conversion `{html_field}` → `{model_field}`:", e)

    print("\n✅ Finish adjustment form - data adjust :", form_data)
    return form_data

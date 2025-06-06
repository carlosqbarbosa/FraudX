import os
import joblib
from django.conf import settings
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler

model_path = os.path.join(settings.BASE_DIR, 'core', 'ml_model', 'modelo_rf.pkl')

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None  # Define como None para evitar erros

def previus_fraud(transaction):
    print("Entrou no método")  

    if model is None:
        return "AI model not found"

    print("O arquivo existe, montando variáveis")  

    transaction_type = str(transaction.transaction_type).strip().upper() if transaction.transaction_type else "UNKNOWN"
    print(f"Transaction Type: {transaction_type}")  

    try:
        amount = float(transaction.amount) if transaction.amount else 0.0
        old_balance_org = float(transaction.old_balance_org) if transaction.old_balance_org else 0.0
        new_balance_orig = float(transaction.new_balance_orig) if transaction.new_balance_orig else 0.0
        old_balance_dest = float(transaction.old_balance_dest) if transaction.old_balance_dest else 0.0
        new_balance_dest = float(transaction.new_balance_dest) if transaction.new_balance_dest else 0.0
    except ValueError as e:
        error_message = f"Error converting transaction values: {str(e)}"
        print(error_message)  # Exibir erro para debug
        return "Un error iniesperd currace, try contact Administrator"  # Retornar erro para o usuário

    print(f"Amount: {amount}")
    print(f"Old Balance Origem: {old_balance_org}")  
    print(f"New Balance Origem: {new_balance_orig}")  
    print(f"Old Balance Destino: {old_balance_dest}")  
    print(f"New Balance Destino: {new_balance_dest}")  

    # Definir os valores booleanos (1 para ativo, 0 para inativo)
    type_cash_out = 1 if transaction_type == "CASH-OUT" else 0
    type_debit = 1 if transaction_type == "DEBIT" else 0
    type_payment = 1 if transaction_type == "PAYMENT" else 0
    type_transfer = 1 if transaction_type == "TRANSFER" else 0

    print(f"type_CASH_OUT: {type_cash_out}, type_DEBIT: {type_debit}, type_PAYMENT: {type_payment}, type_TRANSFER: {type_transfer}")

    # Criando o DataFrame com os valores corretos
    data_input = pd.DataFrame([[amount, old_balance_org, new_balance_orig, old_balance_dest, new_balance_dest, 
                                type_cash_out, type_debit, type_payment, type_transfer]],
                    columns=['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 
                             'type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER'])

    print("Iniciando modelo predict")  
    if hasattr(model, "feature_names_in_"):
        print(model.feature_names_in_)  

    predict = model.predict(data_input)
    probability_array = model.predict_proba(data_input)[0]
    probability = probability_array[1 if predict[0] else 0] * 100

    print(f"Probability: {probability:.2f}%")  
    predict_str = 'Transaction is Fraud' if predict[0] == 1 else 'Transaction No Fraud'

    result = f"{predict_str}, Probability: {round(probability, 2)}%"
    return result
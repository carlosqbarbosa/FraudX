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
        return "modelo training IA no exist"  # Retornando mensagem clara

    print("O arquivo existe, montanod variaveis")  

    transaction_type = str(transaction.transaction_type)
    print("transaction_type " + transaction_type) 

    amount = 18627.02#float(transaction.amount)
    print(f"amount: {amount}")

    old_balance_org =  18627.02#float(transaction.old_balance_org)
    print(f"old_balance_org: {old_balance_org}") 

    new_balance_orig =  0.0#float(transaction.new_balance_orig)
    print(f"new_balance_orig: {new_balance_orig}") 

    old_balance_dest =  147251.58#float(transaction.old_balance_dest)
    print(f"old_balance_dest: {old_balance_dest}") 

    new_balance_dest =  165878.6#float(transaction.new_balance_dest)
    print(f"new_balance_dest: {new_balance_dest}")  

    data_input = pd.DataFrame([[amount, old_balance_org, new_balance_orig, old_balance_dest, new_balance_dest, 1, 0,0,0]],
                    columns=['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest','type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT','type_TRANSFER' ])
    
    #print("Escalonando dados") 
    #scaler = StandardScaler()
    #scaler.fit(data_input)
    #data_input_scaled = scaler.transform(data_input)
    #print("Fim do escalonaento dos dados") 

    print("Iniciando modelo predict") 
    print(model.feature_names_in_)
    predict = model.predict(data_input)

    print("predict", predict)

    probability_array = model.predict_proba(data_input)[0]
    probability = probability_array[1 if predict[0] else 0] * 100

    print(f"probability: {probability:.2f}")

    predict_str = 'Fraud' if predict[0] == 1 else 'No Fraud'

    result = 'Result: ' + predict_str + " Probability: " + str(round(float(probability), 2))
    #result = bool(model.predict(input_data)[0])
    return result

# import os
# import joblib  # ou use pickle se seu modelo foi salvo com pickle
# from django.conf import settings

# # Caminho para o modelo
# modelo_path = os.path.join(settings.BASE_DIR, 'core', 'ml_model', 'name_from_model.lib') #altear para o nome do modelo treinado
# modelo = joblib.load(modelo_path)

# def previus_fraud(transition):
#     input_data = [[
#         transition.value_transition,
#         transition.hour_transition,
#         transition.suspect
#         #hash(transacao.tipo_cartao) % 1000,
#         #hash(transacao.localizacao) % 1000,
#         #transacao.horario.hour * 60 + transacao.horario.minute
#     ]]
#     return bool(modelo.predict(input_data)[0])

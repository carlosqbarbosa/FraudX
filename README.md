
#  FraudX - Sistema de Detecção de Fraudes em Transações Financeiras

FraudX é uma aplicação web desenvolvida em Django que utiliza Machine Learning (Random Forest) para detectar fraudes em transações bancárias com base em variáveis como saldo, tipo de transação e inconsistências nos valores.

---

##  Funcionalidades

-  Interface web para simulação de transações.
-  Verificação automática de fraude com base em um modelo Random Forest.
-  Extração de features como:
  - Diferença entre saldo antigo e novo.
  - Validação se os valores batem com a transação.
-  Treinamento e uso de modelo salvo (`ml_model/fraude_model.pkl`).

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Django
- Scikit-learn
- Pandas
- Joblib

---

## ⚙ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/carlosqbarbosa/FraudX.git
cd FraudX/fraud_x
````

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r ../requirements.txt
```

### 4. Execute as migrações do Django

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Rode o servidor

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  Estrutura do Projeto

```
fraud_x/
├── core/                # Aplicação principal
│   ├── templates/       # HTMLs do frontend
│   ├── static/          # Arquivos estáticos
│   ├── views.py         # Lógica de verificação
│   ├── models.py        # (se utilizado)
│   ├── forms.py         # Formulário da transação
│   └── ml_model/
│       └── fraude_model.pkl  # Modelo treinado
├── fraud_x/             # Configurações do Django
│   ├── settings.py
│   └── urls.py
├── db.sqlite3           # Banco de dados local
├── manage.py            # Entrypoint do Django
└── requirements.txt     # Dependências do projeto
```

---

##  Modelo de Machine Learning

O modelo foi treinado com base em:

* Random Forest Classifier
* Dados balanceados contendo transações fraudulentas e não fraudulentas
* Features derivadas:

  * `org_diff_ok`
  * `dest_diff_ok`

---


##  Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

```


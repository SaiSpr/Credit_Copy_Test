import streamlit as st
import json
import requests as re
import numpy as np
# import streamlit.components.v1 as components
import joblib
import xgboost
import pandas as pd
from sklearn.model_selection import train_test_split


st.title("Credit Card Probability Web App")

st.image("image.jpg")

st.write("""
## About
Having poor or no credit history makes it difficult for many people to get loans. However, unreliable lenders frequently take advantage of this group.

**By offering a satisfying and secure borrowing experience, Home Credit aims to increase financial inclusion for the unbanked population. Home Credit uses a range of alternative data sources, including as telecom and transactional information, to estimate their clients' repayment capacities in order to ensure that this underserved demographic has a favourable lending experience.**       
""")


# st.sidebar.header('Enter the details below')
# # 
# first_name = st.sidebar.text_input("""Input first name """)
# last_name = st.sidebar.text_input("""Input last name""")
# name_contract_type = st.sidebar.number_input("Contract product type (Cash loan, consumer loan [POS]) of the previous application: Type 0 for a cash loan or 1 for a revolving loan",min_value=0, max_value=3)
# children_count = st.sidebar.number_input("how many children do you have?",min_value=0, max_value=11)
# fam_members = st.sidebar.number_input("how many family members do you have",min_value=0, max_value=15)
 
     
# amt_credit_sum = st.sidebar.number_input("What is the amount of credit you want?",min_value=0, max_value=110000)
# DAYS_INSTALMENT_delay = st.sidebar.number_input("""delay since your last credit?""",min_value=-1000, max_value=10)
# amt_income_total= st.sidebar.number_input("""Income per year?""",min_value=0, max_value=11000000)
# region_rating= st.sidebar.number_input("""region rating from 1 to 3 """,min_value=1, max_value=3)
# bureau_year= st.sidebar.number_input("""bureau_year : Number of enquiries to Credit Bureau about the client one day year (excluding last 3 months before application)""",min_value=0, max_value=20)



# if st.button("Detection Result"):
#      values = {
#      "name_contract_type": name_contract_type,
#      "children_count": children_count,
#      "fam_members": fam_members,
#      "region_rating": region_rating,
#      "amt_income_total": amt_income_total,
#      "DAYS_INSTALMENT_delay": DAYS_INSTALMENT_delay,
#      "amt_credit_sum": amt_credit_sum,
#      "bureau_year":bureau_year
#      }

#      st.write(f"""### These are the transaction details:\n
#      First Name: {first_name}
#      Last Name: {last_name}
#      1. name_contract_type: {name_contract_type}\n
#      2. children_count: {children_count}\n
#      3. amt_income_total: {amt_income_total}$\n
#      4. fam_members: {fam_members}\n
#      5. region_rating: {region_rating}\n
#      6. DAYS_INSTALMENT_delay: {DAYS_INSTALMENT_delay}\n
#      7. amt_credit_sum: {amt_credit_sum}\n
#      8. bureau_year: {bureau_year}
#                """)

   
   
#      res = re.post(f"https://creditcopytest-production.up.railway.app/predict",json=values)
#      json_str = json.dumps(res.json())
#      resp = json.loads(json_str)
    
    
    
#      if first_name=='' or last_name == '':
#          st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
#      else:
#          st.write(f"{resp[0]}")
    
    

    
    
    
    
    
    
    
    
    
#Chargement des données
@st.cache
def load_data(file_name):
    data = joblib.load(file_name)
    return data
df = load_data("data_customers.pkl")

# Chargement du modèle
@st.cache(hash_funcs={'xgboost.sklearn.XGBClassifier': id})
def load_model(file_name):
    model = joblib.load(file_name)
    return model

XGBoost_model = load_model("best_model_XGBoost_pickle.pkl")


#Mise en place des filtres
st.sidebar.title('Filtres')
# Filtre 1 GENDER
option1 = st.sidebar.selectbox('Sexe :',("Tous", "Homme", "Femme"))
sexe_filter = 1 if option1 == "Homme" else 0 if option1 == "Femme" else 2

# Filtre 2 NAME_CONTRACT_TYPE
option2 = st.sidebar.selectbox('Type de contrat :',("Tous", "Revolving loans", "Cash loans"))
contract_filter = 0 if option2 == "Revolving loans" else 1 if option2 == "Cash loans" else 2

# Filtre 3 AGE
max_age = round(max(-df['DAYS_BIRTH'])/365)
min_age = round(min(-df['DAYS_BIRTH'])/365)
min_slider, max_slider = st.sidebar.slider('Tranche d\'age', min_age, max_age, (min_age,max_age))

#Création du sous groupe de clients
df_group = df[["SK_ID_CURR", "NAME_CONTRACT_TYPE"
                  , "CODE_GENDER", "AMT_INCOME_TOTAL"
                  ,"CNT_CHILDREN","DAYS_BIRTH"
                  ,"SCORE","TARGET"]]
df_group = df_group[(df_group["DAYS_BIRTH"] < -min_slider*365) & (df_group["DAYS_BIRTH"] > -max_slider*365)]
df_group = df_group[df_group["CODE_GENDER"] != sexe_filter]
df_group = df_group[df_group["NAME_CONTRACT_TYPE"] != contract_filter]


#Sélection du client à étudier
st.sidebar.title('Sélectionnez un client')


# Filtre FINAL SK_ID_CURR
list_id = df_group['SK_ID_CURR'].unique().tolist()
id_customer = st.sidebar.selectbox('ID du client  :', list_id)
count_customers = df_group.shape[0]
# st.sidebar.write('Nombre de clients correspondant à vos filtres :', count_customers)
st.sidebar.write(count_customers, 'clients correspondant à vos filtres')













# values = {
#      "id_customer": id_customer
#      }



# res = re.post(f"https://creditcopytest-production.up.railway.app/predict",json=values)
# json_str = json.dumps(res.json())
# resp = json.loads(json_str)
    











 
 
 
 
 
 
 
 


#Affichage des informations du client unique
df_customer = df[["SK_ID_CURR", "NAME_CONTRACT_TYPE"
                  , "CODE_GENDER", "AMT_INCOME_TOTAL"
                  ,"CNT_CHILDREN","DAYS_BIRTH"
                  ,"SCORE","TARGET"]]
df_customer = df_customer[df_customer['SK_ID_CURR'] == id_customer]


date = "Non renseigné" if len(df_customer['DAYS_BIRTH']) == 0 else round(-df_customer['DAYS_BIRTH'].item()/365)
name_type_contract = "Revolving loans" if df_customer["NAME_CONTRACT_TYPE"].item() == 1 else "Cash loans"
code_gender = "Femme" if df_customer["CODE_GENDER"].item() == 1 else "Homme"
cnt_children = df_customer["CNT_CHILDREN"].item()
amt_income_total = str(int(df_customer["AMT_INCOME_TOTAL"].item())) + " $"
score = str(round(df_customer["SCORE"].item()*100)) + "%"
target = "Non Eligible" if df_customer["TARGET"].item() == 1 else "Eligible"


st.write("ID client :", id_customer)
st.write("Sexe :", code_gender)
st.write("Age : " + str(date) + " ans")
st.write("Type de contrat :", name_type_contract)
st.write("Nombre d'enfants :", cnt_children)
st.write("Revenu total :", amt_income_total)
st.write("Probabilité de défaut :", score)
st.write("Statut du client :", target)

if target == "Eligible":
    st.write("Customer is eligible for loan")
else:
    st.write("Customer is not eligible for loan")
  
st.title('Model Summary')
st.image("waterfall_plot.png", caption='Result Summary')

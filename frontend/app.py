# import streamlit as st
# import json
# import requests as re

# st.title("Credit Card Fraud Detection Web App")

# st.image("image.jpg")

# st.write("""
# ## About
# By offering a satisfying and secure borrowing experience, Home Credit aims to increase financial inclusion for the unbanked population. Home Credit uses a range of alternative data sources, including as telecom and transactional information, to estimate their clients' repayment capacities in order to ensure that this underserved demographic has a favourable lending experience.**
# """) 


# st.sidebar.header('Input Features of The Transaction')

# sender_name = st.sidebar.text_input("""Input Sender ID""")
# receiver_name = st.sidebar.text_input("""Input Receiver ID""")
# step = st.sidebar.slider("""Number of Hours it took the Transaction to complete: """)
# types = st.sidebar.subheader(f"""
#                  Enter Type of Transfer Made:\n\n\n\n
#                  0 for 'Cash In' Transaction\n 
#                  1 for 'Cash Out' Transaction\n 
#                  2 for 'Debit' Transaction\n
#                  3 for 'Payment' Transaction\n  
#                  4 for 'Transfer' Transaction\n""")
# types = st.sidebar.selectbox("",(0,1,2,3,4))
# x = ''
# if types == 0:
#     x = 'Cash in'
# if types == 1:
#     x = 'Cash Out'
# if types == 2:
#     x = 'Debit'
# if types == 3:
#     x = 'Payment'
# if types == 4:
#     x =  'Transfer'
    
# amount = st.sidebar.number_input("Amount in $",min_value=0, max_value=110000)
# oldbalanceorg = st.sidebar.number_input("""Original Balance Before Transaction was made""",min_value=0, max_value=110000)
# newbalanceorg= st.sidebar.number_input("""New Balance After Transaction was made""",min_value=0, max_value=110000)
# oldbalancedest= st.sidebar.number_input("""Old Balance""",min_value=0, max_value=110000)
# newbalancedest= st.sidebar.number_input("""New Balance""",min_value=0, max_value=110000)
# isflaggedfraud = st.sidebar.selectbox("""Specify if this was flagged as Fraud by your System: """,(0,1))


# if st.button("Detection Result"):
#     values = {
#     "step": step,
#     "types": types,
#     "amount": amount,
#     "oldbalanceorig": oldbalanceorg,
#     "newbalanceorig": newbalanceorg,
#     "oldbalancedest": oldbalancedest,
#     "newbalancedest": newbalancedest,
#     "isflaggedfraud": isflaggedfraud
#     }


#     st.write(f"""### These are the transaction details:\n
#     Sender ID: {sender_name}
#     Receiver ID: {receiver_name}
#     1. Number of Hours it took to complete: {step}\n
#     2. Type of Transaction: {x}\n
#     3. Amount Sent: {amount}\n
#     4. Sender Previous Balance Before Transaction: {oldbalanceorg}\n
#     5. Sender New Balance After Transaction: {newbalanceorg}\n
#     6. Recepient Balance Before Transaction: {oldbalancedest}\n
#     7. Recepient Balance After Transaction: {newbalancedest}\n
#     8. System Flag Fraud Status: {isflaggedfraud}
#                 """)

#     res = re.post(f"http://backend.docker:8000/predict/",json=values)
#     json_str = json.dumps(res.json())
#     resp = json.loads(json_str)
    
#     if sender_name=='' or receiver_name == '':
#         st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
#     else:
#         st.write(f"""### The '{x}' transaction that took place between {sender_name} and {receiver_name} is {resp[0]}.""")
        
        
import streamlit as st
import json
import requests as re
import numpy as np
import streamlit.components.v1 as components


st.title("Credit Card Probability Web App")

st.image("image.jpg")

st.write("""
## About
Having poor or no credit history makes it difficult for many people to get loans. However, unreliable lenders frequently take advantage of this group.

**By offering a satisfying and secure borrowing experience, Home Credit aims to increase financial inclusion for the unbanked population. Home Credit uses a range of alternative data sources, including as telecom and transactional information, to estimate their clients' repayment capacities in order to ensure that this underserved demographic has a favourable lending experience.**       
""")


st.sidebar.header('Enter the details below')
# 
first_name = st.sidebar.text_input("""Input first name """)
last_name = st.sidebar.text_input("""Input last name""")
name_contract_type = st.sidebar.number_input("Contract product type (Cash loan, consumer loan [POS]) of the previous application: Type 0 for a cash loan or 1 for a revolving loan",min_value=0, max_value=3)
children_count = st.sidebar.number_input("how many children do you have?",min_value=0, max_value=11)
fam_members = st.sidebar.number_input("how many family members do you have",min_value=0, max_value=15)
 
     
amt_credit_sum = st.sidebar.number_input("What is the amount of credit you want?",min_value=0, max_value=110000)
DAYS_INSTALMENT_delay = st.sidebar.number_input("""delay since your last credit?""",min_value=-1000, max_value=10)
amt_income_total= st.sidebar.number_input("""Income per year?""",min_value=0, max_value=11000000)
region_rating= st.sidebar.number_input("""region rating from 1 to 3 """,min_value=1, max_value=3)
bureau_year= st.sidebar.number_input("""bureau_year : Number of enquiries to Credit Bureau about the client one day year (excluding last 3 months before application)""",min_value=0, max_value=20)
#




# st.sidebar.header('Input Features of The Transaction')

# sender_name = st.sidebar.text_input("""Input Sender ID""")
# receiver_name = st.sidebar.text_input("""Input Receiver ID""")
# step = st.sidebar.slider("""Number of Hours it took the Transaction to complete: """)
# types = st.sidebar.subheader(f"""
#                  Enter Type of Transfer Made:\n\n\n\n
#                  0 for 'Cash In' Transaction\n 
#                  1 for 'Cash Out' Transaction\n 
#                  2 for 'Debit' Transaction\n
#                  3 for 'Payment' Transaction\n  
#                  4 for 'Transfer' Transaction\n""")
# types = st.sidebar.selectbox("",(0,1,2,3,4))
# x = ''
# if types == 0:
#     x = 'Cash in'
# if types == 1:
#     x = 'Cash Out'
# if types == 2:
#     x = 'Debit'
# if types == 3:
#     x = 'Payment'
# if types == 4:
#     x =  'Transfer'
    
# amount = st.sidebar.number_input("Amount in $",min_value=0, max_value=110000)
# oldbalanceorg = st.sidebar.number_input("""Sender Balance Before Transaction was made""",min_value=0, max_value=110000)
# newbalanceorg= st.sidebar.number_input("""Sender Balance After Transaction was made""",min_value=0, max_value=110000)
# oldbalancedest= st.sidebar.number_input("""Recipient Balance Before Transaction was made""",min_value=0, max_value=110000)
# newbalancedest= st.sidebar.number_input("""Recipient Balance After Transaction was made""",min_value=0, max_value=110000)
# isflaggedfraud = 0
# if amount >= 200000:
#   isflaggedfraud = 1
# else:
#   isflaggedfraud = 0


if st.button("Detection Result"):
     values = {
     "name_contract_type": name_contract_type,
     "children_count": children_count,
     "fam_members": fam_members,
     "region_rating": region_rating,
     "amt_income_total": amt_income_total,
     "DAYS_INSTALMENT_delay": DAYS_INSTALMENT_delay,
     "amt_credit_sum": amt_credit_sum,
     "bureau_year":bureau_year
     }

     st.write(f"""### These are the transaction details:\n
     First Name: {first_name}
     Last Name: {last_name}
     1. name_contract_type: {name_contract_type}\n
     2. children_count: {children_count}\n
     3. amt_income_total: {amt_income_total}$\n
     4. fam_members: {fam_members}\n
     5. region_rating: {region_rating}\n
     6. DAYS_INSTALMENT_delay: {DAYS_INSTALMENT_delay}\n
     7. amt_credit_sum: {amt_credit_sum}\n
     8. bureau_year: {bureau_year}
               """)

#    if st.button("Detection Result"):
#     values = {
#     "step": step,
#     "types": types,
#     "amount": amount,
#     "oldbalanceorig": oldbalanceorg,
#     "newbalanceorig": newbalanceorg,
#     "oldbalancedest": oldbalancedest,
#     "newbalancedest": newbalancedest,
#     "isflaggedfraud": isflaggedfraud
#     }
   
   
   
     res = re.post(f"https://creditcopytest-production.up.railway.app/predict",json=values)
     json_str = json.dumps(res.json())
     resp = json.loads(json_str)
    
    
    
     if first_name=='' or last_name == '':
         st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
     else:
         st.write(f"{resp[0]}")
    
    
#     if sender_name=='' or receiver_name == '':
#         st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
#     else:
#         st.write(f"""### The '{x}' transaction that took place between {sender_name} and {receiver_name} is {resp[0]}.""")











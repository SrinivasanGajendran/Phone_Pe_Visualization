import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import main
conn = mysql.connector.connect(
    host="localhost",
    user="srini",
    password="password"
    )
# Create a cursor object
cursor = conn.cursor()
# Check if the database exists
sql = "SHOW DATABASES LIKE 'Phone_Pe'"
cursor.execute(sql)
result = cursor.fetchone()
if result:
    conn = mysql.connector.connect(
        host="localhost",
        user="srini",
        password="password",
        database="Phone_Pe"
    )
else:
    sql = "CREATE DATABASE Phone_Pe"
    cursor.execute(sql)
    conn = mysql.connector.connect(
        host="localhost",
        user="srini",
        password="password",
        database="Phone_Pe"
    )
    main.create()
cursor = conn.cursor()
st.set_page_config(page_title="Phone_Pe",page_icon=":tada",layout='wide')
header = st.container()
df = pd.read_sql_query("SELECT DISTINCT State FROM Aggregate_Transaction", conn)
with header:
    st.title("Phone_Pe Data visualization:-")
    st.subheader("Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly")
col1,col2,col3 = st.columns(3)
with col1:
    States = st.selectbox('States',(df))
with col2:
    Year = st.selectbox('Year', ('2018', '2019', '2020', '2021', '2022'))
colm1,colm2,colm3 = st.columns(3)
co1,co2,co3 = st.columns(3)

def Transaction(selected_options):
    df = pd.read_sql_query(f"""SELECT DISTINCT State,YEAR ,Type_Of_Transaction, Total, Amount FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" """, conn)
    Total = df['Total'].sum()
    No_Of_transaction = "{:,.2f}".format(Total)
    Amount = df['Amount'].sum()
    Total_Amount = "{:,.2f}".format(Amount)
    df_1 = pd.read_sql_query(f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Type_Of_Transaction = 'Recharge & bill payments' """, conn)
    df_2 = pd.read_sql_query(f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Type_Of_Transaction = 'Peer-to-peer payments' """, conn)
    df_3 = pd.read_sql_query(f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Type_Of_Transaction = 'Merchant payments' """, conn)
    df_4 = pd.read_sql_query(f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Type_Of_Transaction = 'Financial Services' """, conn)
    df_5 = pd.read_sql_query(f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Type_Of_Transaction = 'Others' """, conn)
    Recharge = "{:,.2f}".format(df_1['Total'].sum())
    Peer = "{:,.2f}".format(df_2['Total'].sum())
    Merchant = "{:,.2f}".format(df_3['Total'].sum())
    Financial = "{:,.2f}".format(df_4['Total'].sum())
    Others = "{:,.2f}".format(df_5['Total'].sum())
    with col1:
        st.subheader("All Phone_Pe Transactions:")
        st.subheader("Total Payment:")
        st.subheader("Recharge & bill payments :")
        st.subheader("Peer-to-peer payments : ")
        st.subheader("Merchant payments : ")
        st.subheader("Financial Services : ")
        st.subheader("Others : ")
    with col2:
       st.subheader(No_Of_transaction)
       st.subheader(Total_Amount)
       st.subheader(Recharge)
       st.subheader(Peer)
       st.subheader(Merchant)
       st.subheader(Financial)
       st.subheader(Others)


def User(selected_options):
    df = pd.read_sql_query(f"""SELECT Registered_Users FROM Aggregate_User WHERE State = "{States}" AND Year= "{Year}" """,conn)
    Registered_Users = "{:,.2f}".format(df['Registered_Users'].sum())
    with col1:
        st.subheader(f"Total_Users:")
    with col2:
        st.subheader(Registered_Users)
    with col3:
        df = pd.read_sql_query(f"""SELECT DISTINCT State,YEAR ,Type_Of_Transaction, Total, Amount FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" """,conn)
        fig = px.pie(df,values='Total',names='Type_Of_Transaction',title = 'Overall Transactions')
        st.write(fig)

def format_value(value):
    if value >= 10000000:
        return "{:,.2f} crore".format(value / 10000000)
    else:
        return "{:,.2f} lakh".format(value / 100000)

def district(selected_options):
    df = pd.read_sql_query(f""" SELECT DISTINCT District, Count FROM Top_Transaction_District WHERE State = "{States}" AND Year = "{Year}" """,conn)
    district = df['District'].unique()
    emp = []
    with colm1:
            st.subheader("Top Transaction (Districts)")
            for element in district:
                df_1 = pd.read_sql_query(f""" SELECT Amount FROM Top_Transaction_District WHERE State = "{States}" AND Year = "{Year}" AND District = "{element}" """,conn)
                amount = df_1['Amount'].sum()
                emp.append({'District': element, 'Amount': format_value(amount)})
            st.markdown("""
            <style>
            table {
            background-color: lightblue;
            }
            </style>
            """, unsafe_allow_html=True)
            st.table(emp)
    with colm2:
        fig = px.bar(emp, x='District', y='Amount', title='Transactions')
        st.write(fig)
    emp1 = []
    with colm1:
            st.subheader("Top User (Districts)")
            for element1 in district:
                df2 = pd.read_sql_query(f""" SELECT Registered_Users FROM Top_User_District WHERE State = "{States}" AND Year = "{Year}" AND District = "{element1}" """,conn)
                Registered_Users = "{:,.2f}".format(df2['Registered_Users'].sum())
                emp1.append({'District': element1, 'Registered_Users': Registered_Users})
            st.table(emp1)
    with colm2:
        fig = px.bar(emp1, x='District', y='Registered_Users', title='Users')
        st.write(fig)

with col3 :
    st.write('\n')
    st.write('\n')
    if st.button('Submit'):
        selected_options= [States,Year]
        Transaction(selected_options)
        User(selected_options)
        district(selected_options)

conn.commit()
cursor.close()
conn.close()



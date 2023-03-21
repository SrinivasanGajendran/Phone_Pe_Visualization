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
sql = "SHOW DATABASES LIKE 'testing'"
cursor.execute(sql)
result = cursor.fetchone()
if result:
    conn = mysql.connector.connect(
        host="localhost",
        user="srini",
        password="password",
        database="testing"
    )
else:
    sql = "CREATE DATABASE testing"
    cursor.execute(sql)
    conn = mysql.connector.connect(
        host="localhost",
        user="srini",
        password="password",
        database="testing"
    )
    main.create()
st.set_page_config(page_title="Phone_Pe",page_icon=":tada",layout='wide')
header = st.container()
df = pd.read_sql_query("SELECT DISTINCT State FROM aggregate_transaction", conn)
with header:
    st.title("Phone_Pe Data visualization:-")
    st.subheader("Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly")


col1,col2,col3 = st.columns(3)
colm1,colm2 = st.columns(2)
with col1:
    States = st.selectbox('States', (df))

with col2:
    Year = st.selectbox('Year', ('2018', '2019', '2020', '2021', '2022'))

with col3:
    Quarter = st.selectbox('Quarter', ('1', '2', '3', '4'))
co1,co2,co3 = st.columns(3)
c1,c2 = st.columns(2)

def transaction():
    df = pd.read_sql_query(
        f"""SELECT DISTINCT State,YEAR,Quarter,Type_Of_Transaction, Total, Amount FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}, Quarter = {Quarter}" """,
        conn)
    Total = df['Total'].sum()
    No_Of_transaction = "{:,.2f}".format(Total)
    Amount = df['Amount'].sum()
    Total_Amount = "{:,.2f}".format(Amount)
    df_1 = pd.read_sql_query(
        f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Quarter = "{Quarter} " AND Type_Of_Transaction = 'Recharge & bill payments' """,
        conn)
    df_2 = pd.read_sql_query(
        f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Quarter = "{Quarter}" AND Type_Of_Transaction = 'Peer-to-peer payments' """,
        conn)
    df_3 = pd.read_sql_query(
        f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Quarter = "{Quarter}" AND Type_Of_Transaction = 'Merchant payments' """,
        conn)
    df_4 = pd.read_sql_query(
        f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Quarter = "{Quarter}" AND Type_Of_Transaction = 'Financial Services' """,
        conn)
    df_5 = pd.read_sql_query(
        f"""SELECT Total FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" AND Quarter = "{Quarter}" AND Type_Of_Transaction = 'Others' """,
        conn)
    Recharge = "{:,.2f}".format(df_1['Total'].sum())
    Peer = "{:,.2f}".format(df_2['Total'].sum())
    Merchant = "{:,.2f}".format(df_3['Total'].sum())
    Financial = "{:,.2f}".format(df_4['Total'].sum())
    Others = "{:,.2f}".format(df_5['Total'].sum())
    with co1:
        st.subheader("All Phone_Pe Transactions:")
        st.subheader("Total Payment:")
        st.subheader("Recharge & bill payments :")
        st.subheader("Peer-to-peer payments : ")
        st.subheader("Merchant payments : ")
        st.subheader("Financial Services : ")
        st.subheader("Others : ")
    with co2:
        st.subheader(f"₹ {No_Of_transaction}")
        st.subheader(f"₹ {Total_Amount}")
        st.subheader(f"₹ {Recharge}")
        st.subheader(f"₹ {Peer}")
        st.subheader(f"₹ {Merchant}")
        st.subheader(f"₹ {Financial}")
        st.subheader(f"₹ {Others}")

    with colm1:
        st.title(f"Transaction details of {States} in {Year}-Q{Quarter}:-")
        st.write()

def user():
    df = pd.read_sql_query(
        f"""SELECT Registered_Users FROM Aggregate_User WHERE State = "{States}" AND Year= "{Year}" AND Quarter={Quarter} """, conn)
    Registered_Users = "{:,.2f}".format(df['Registered_Users'].sum())
    with co1:
        st.subheader(f"Registered_Users in {Year} Q{Quarter} :")
    with co2:
        st.subheader(Registered_Users)
    with co3:
        df = pd.read_sql_query(
            f"""SELECT DISTINCT State,YEAR ,Type_Of_Transaction, Total, Amount FROM Aggregate_Transaction WHERE State = "{States}" AND YEAR = "{Year}" """,
            conn)
        fig = px.pie(df, values='Total', names='Type_Of_Transaction')
        st.write(fig)

def Top_District():
    st.header(f"Top Users District Wise:")
    df6 = pd.read_sql_query(
        f"""SELECT DISTRICT,Registered_User FROM Top_User_Districts WHERE STATE= "{States}" AND YEAR = "{Year}" AND QUARTER= "{Quarter}" """,
        conn)
    st.write(df6)


def Top_Users():

        st.header("Top Users Pincode Wise:")
        df7 = pd.read_sql_query(f"""SELECT PINCODES,Registered_User FROM Top_User_Pincode WHERE STATE= "{States}" AND YEAR = "{Year}" AND QUARTER= "{Quarter}" """,
        conn)
        st.write(df7)

def display():
    with c1:
        tab1, tab2,tab3 = st.tabs(['Districts', 'Pincodes','Graph'])
        with co1:
            with tab1:
                Top_District()

            with tab2:
                Top_Users()
            with tab3:
                df6 = pd.read_sql_query(
                    f"""SELECT DISTRICT,Registered_User FROM Top_User_Districts WHERE STATE= "{States}" AND YEAR = "{Year}" AND QUARTER= "{Quarter}" """,
                    conn)

                st.bar_chart(df6, x="DISTRICT", y="Registered_User", width=200)
                st.write()
                df7 = pd.read_sql_query(
                    f"""SELECT PINCODES,Registered_User FROM Top_User_Pincode WHERE STATE= "{States}" AND YEAR = "{Year}" AND QUARTER= "{Quarter}" """,
                    conn)
                st.bar_chart(df7, x="PINCODES", y="Registered_User", width=200)
                st.write()


with col3:
    if st.button('Submit'):
        user()
        transaction()
        display()






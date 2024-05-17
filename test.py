import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
import datetime

color_map = {'FinishedSuccess': 'blue', 'FinishedFail': 'red', 'Skipped': 'yellow','Error': 'purple','Reset': 'orange'}
    
def prod(df, start_date, end_date):
    st.subheader("за неделю prod")
    df = df[(df['start'] >= start_date) & (df['start'] <= end_date)]
    fig = px.timeline(df, x_start="start", x_end="end", y="AppName",color = 'Status',color_discrete_map=color_map)
    fig.update_layout(width=800, height=1600)
    st.plotly_chart(fig)
        
def dev(df, start_date, end_date):
    st.subheader("за неделю dev")
    df = df[(df['start'] >= start_date) & (df['start'] <= end_date)]
    fig = px.timeline(df, x_start="start", x_end="end", y="AppName",color = 'Status',color_discrete_map=color_map)
    fig.update_layout(width=800, height=1600)
    st.plotly_chart(fig)
        
def main():
    st.sidebar.title("Навигация")
    pages = {
        "Prod": prod,
        "Dev": dev
    }
    selection = st.sidebar.radio("Переключиться на:", list(pages.keys()))
    page = pages[selection]
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=today.weekday())
    start_date = st.sidebar.date_input('Выберите начальную дату',value=start_date)
    end_date = st.sidebar.date_input('Выберите конечную дату',value=today)

    # Преобразование в объекты datetime
    start_date = datetime.datetime.combine(start_date, datetime.time())
    end_date = datetime.datetime.combine(end_date, datetime.time())

    df6 = pd.read_excel('logs_prod.xlsx')
    df7 = pd.read_excel('logs_dev.xlsx')

    page(df6 if selection == "Prod" else df7, start_date, end_date)

if __name__ == "__main__":
    main()

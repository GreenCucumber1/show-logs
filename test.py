import streamlit as st
import pandas as pd
import plotly
import plotly.express as px


def main():
    df6 = pd.read_excel('df5.xlsx')
    df6 = df6[df6['start'] >= '2024-03-18']
    df7 = pd.read_excel('df7.xlsx')
    df7 = df7[df7['start'] >= '2024-03-25']
    color_map = {'FinishedSuccess': 'blue', 'FinishedFail': 'red', 'Skipped': 'yellow','Error': 'purple','Reset': 'orange'}
    
    def prod():
        st.subheader("за неделю prod")
        fig = px.timeline(df6, x_start="start", x_end="end", y="AppName",color = 'Status',color_discrete_map=color_map)
        fig.update_layout(width=800, height=1600)
        st.plotly_chart(fig)
        
    def dev():
        st.subheader("за неделю dev")
        fig = px.timeline(df7, x_start="start", x_end="end", y="AppName",color = 'Status',color_discrete_map=color_map)
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
        page()


if __name__ == "__main__":
    main()

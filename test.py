import streamlit as st
import pandas as pd
import plotly
import plotly.express as px


def main():
      # график timeline за неделю
    st.subheader("за неделю")
    df6 = pd.read_excel('df5.xlsx')
    df6 = df6[df6['start'] >= '2024-03-18']
    color_map = {'FinishedSuccess': 'blue', 'FinishedFail': 'red', 'Skipped': 'yellow','Error': 'purple','Reset': 'orange'}
    fig = px.timeline(df6, x_start="start", x_end="end", y="AppName",color = 'Status',color_discrete_map=color_map)
    fig.update_layout(width=800, height=1600)
    st.plotly_chart(fig)
if __name__ == "__main__":
    main()

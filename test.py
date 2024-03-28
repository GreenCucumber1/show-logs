import streamlit as st
import pandas as pd
import plotly
import plotly.express as px


def main():
    
    # Загрузка данных
    df1 = pd.read_excel('df1.xlsx')    

    df2 = pd.read_excel('df2.xlsx')    
    # Фильтрация данных по дате
    new_df = pd.concat([df1, df2])
    new_df0 = new_df[new_df['Time1'] >= '2024-03-18']
    new_df_one_day = new_df[new_df['Time1'] >= '2024-03-25']

    st.title('full days')
    

    
    # Загрузка изображения
    image_path = 'my_plot.png'
    st.image(image_path, use_column_width=True)

    st.title('one day')
    st.write("blue - FinishedSuccess")
    st.write("light-blue - FinishedFail")
    st.write("red - Skipped")
    # Вывод графика
    fig = px.line(new_df_one_day, x="AppName", y="Time1", color='Status', symbol="a")
    fig.update_layout(width=3000, height=800)
    fig.update_layout(showlegend=False)
    #fig.update_layout(legend=dict(x =1,y=-1)) 

    st.plotly_chart(fig)
    
    # график timeline за день
    st.subheader("за день")
    df5 = pd.read_excel('df5.xlsx')
    df5 = df5[df5['start'] >= '2024-03-25']
    color_map = {'FinishedSuccess': 'blue', 'FinishedFail': 'red', 'Skipped': 'yellow'}

    fig = px.timeline(df5, x_start="start", x_end="end", y="AppName",color = 'Status',color_discrete_map=color_map)
    fig.update_layout(width=1000, height=1600)
    st.plotly_chart(fig)

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

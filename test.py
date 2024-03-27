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
    st.write("blue - FinishedSuccess")
    st.write("green - Skipped")
    st.write("red - FinishedFail")
    
    # Загрузка изображения
    image_path = 'my_plot.png'
    st.image(image_path, use_column_width=True)

    st.title('one day')
    # Вывод графика
    fig = px.line(new_df_one_day, x="AppName", y="Time1", color='Status', symbol="a")
    fig.update_layout(width=3000, height=800)
    fig.update_layout(showlegend=False)
    #fig.update_layout(legend=dict(x =1,y=-1)) 

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

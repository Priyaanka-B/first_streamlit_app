import streamlit
streamlit.title('my new github trail')
streamlit.header('break fast menu')
streamlit.text('oats meal and juice')
streamlit.text('Chicken Biriyani')
streamlit.text('sweets and fruits')
streamlit.text('sweets and fruits')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

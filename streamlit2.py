import streamlit as st
import pandas as pd


st.title("Lets's learn states and callback functions")

if 'number_of_rows' not in st.session_state or 'type' not in st.session_state:
    st.session_state['number_of_rows'] = 5
    st.session_state['type'] = 'Categorical'

df = pd.read_csv('data/titanic.csv', sep=',')
col1, col2 = st.columns(2)

with col1:
    increment = st.button('Increment')
    if increment:
        st.session_state['number_of_rows'] += 1

with col2:
    decrement = st.button('Decrement')
    if decrement:
        st.session_state['number_of_rows'] -= 1

st.table(df.head(st.session_state['number_of_rows']))


def handle_click(new_type):
    st.session_state['type'] = new_type


def handle_change():
    if st.session_state.kind_of_column:
        st.session_state['type'] = st.session_state.kind_of_column


types = {'Categorical': ['Survived', 'Sex', 'Cabin',
                         'Embarked', 'Pclass', 'SibSp'], 'Numerical': ['Age', 'Fare']}
column = st.selectbox('Select column', types[st.session_state['type']])
st.radio('Select type of column', [
    'Categorical', 'Numerical'], key='kind_of_column', on_change=handle_change)
# type_of_column = st.radio("what kind of analysis do you want to do?", ['Categorical', 'Numerical'])
# change = st.button("change", on_click=handle_click, args=[type_of_column])

if st.session_state['type'] == 'Categorical':
    dist = pd.DataFrame(df[column].value_counts()).head(50)
    st.bar_chart(dist)
else:
    st.write(df[column].describe())

import streamlit as st
with st.form('form_input'):
    st.header('Input Form')
    col1,col2,col3=st.columns(3)
    with col1:
        name=st.text_input('Input Name')
        rating=st.slider('Choose rating',1,10,5)
    with col2:
        date=st.date_input('Please input your date of birth')
        recommended=st.radio('Would you recommended to others?',('Yes','No'))
    with col3:
        age=st.number_input('Input Your age')
        salary=st.number_input('Input your salary imagination')
    submit_button=st.form_submit_button('Submit')
if submit_button is True:
    st.write('**Name=**',name,'**rating=**',rating,'**Date=**',date,'**Recommended=**',recommended,'**Age=**',age,'**salary=**',salary)

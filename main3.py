import streamlit as st





with st.form('UsingForm'):
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        st.subheader('Multiplication')
        def multiplication(a1, a2):
            return a1 * a2
        n1 = st.number_input('The first number', key="1")
        n2 = st.number_input('The second number', key="2")
        Multiplication = st.form_submit_button('Multiplication')
        if Multiplication is True:
            st.write('Multiplication is = ' + str(multiplication(n1, n2)))
    with col2:
        st.subheader('Division')
        def division(b1, b2):
            return b1 / b2
        n1a = st.number_input('The first number', key="3")
        n2a = st.number_input('The second number', key="4")
        Division = st.form_submit_button('Division')
        if Division is True:
            st.write('Division is = ' + str(division(n1a, n2a)))
    with col3:
        st.subheader('Addition')
        def addition(n1b, n2b):
            return n1b + n2b
        n1b = st.number_input('The first number', key="5")
        n2b = st.number_input('The second number', key="6")
        Addition = st.form_submit_button('Addition')
        if Addition is True:
            st.write('Addition is = ' + str(addition(n1b, n2b)))

    with col4:
        st.subheader('Subtraction')
        def subtraction(n1c, n2c):
            return n1c - n2c
        n1c = st.number_input('The first number', key="7")
        n2c = st.number_input('The second number', key="8")
        Subtraction = st.form_submit_button('Subtraction')
        if Subtraction is True:
            st.write('Subtraction is = ' + str(subtraction(n1c, n2c)))





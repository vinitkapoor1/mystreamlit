import streamlit as st
st.set_page_config(page_title='My Streamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Form','Download'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-150x84.png')
st.title('Python Technology')
st.header('By Vinit Kapoor')
st.text('This is the learning Session on Streamlit Library')
if(mymenu=='Home'):
    st.markdown('<center><h1>Welcome to DashBoard</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=EjY2gUFVwZE')
elif(mymenu=='Form'):
    with st.form('Form Data'):
        Name=st.text_input('Enter Name')
        Address=st.text_input('Enter Address')
        DOB=st.date_input("Choose Date of birtg")
        marks=st.slider('Marks')
        k=st.form_submit_button("Submit")
        if k:
            st.write('Name=',Name,'Address=',Address,'DOB=',DOB,'marks=',marks)
elif(mymenu=='Download'):
    st.header("Download")
    st.download_button('Download Now','The file is downloaded','Python.txt')
    

import streamlit as st
st.title('MES COLLEGE MARAMPILLY')
st.header('MES COLLEGE MARAMPILLY')
st.text('welcome')
st.markdown("https://icfoss.in/")
st.success('success')
st.warning("warning")
st.error('error')
from PIL import Image    
a=Image.open("ICFOSS_logo.png")
st.image(a,width=100)
b=open("CharlieChaplin .mp4",'rb')
b1=b.read()
st.video(b1)
c=open("demo.mp3",'rb')
c1=c.read()
st.audio(c1)
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")
name=st.text_input("enter the name","enter here")
if st.button("submit"):
    st.text(name)
    st.success("success")   
st.sidebar.header("Side Bar Header")
st.sidebar.text("Hello")
import streamlit as st
import pandas as pd
import re
import math
import seaborn as sns
import matplotlib.pyplot as plt

def Reflection_Screen():
    st.header("Reflection của mỗi thành viên trong team")
    
    st.subheader("Member 1")
    st.markdown('''
- 🎖 Difficulty: 
- 🎖 Gain: 
                ''')
    
    st.subheader("Member 2")
    st.markdown('''
- 🎖 Difficulty: 
- 🎖 Gain: 
                ''')
    
    st.subheader("Member 3")
    st.markdown('''
- 🎖 Difficulty: 
- 🎖 Gain: 
                ''')
    
    st.subheader("Member 4")
    st.markdown('''
- 🎖 Difficulty: 
- 🎖 Gain: 
                ''')
    
    button = st.button("⭐️ Thanks ")
    if button:
        st.balloons()
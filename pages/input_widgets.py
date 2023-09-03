import streamlit as st

threshold_age = 18

# slider input
age = st.slider('This is slider label for `age`', min_value=0, max_value=100, step=2)

# Logic based on slider value
if age < threshold_age:
    st.write(f"Age belongs to `Children`")
else:
    st.write(f"Age belongs to `Adult`")
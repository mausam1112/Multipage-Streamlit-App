import streamlit as st

threshold_age = 18

# slider input
age = st.slider('This is slider label for `age`', min_value=0, max_value=100, step=2)

# Logic based on slider value
if age < threshold_age:
    st.write(f"Age belongs to `Children`")
else:
    st.write(f"Age belongs to `Adult`")

'-----------------------------------------'

# radio button selection
langs = ['python', 'java', 'C']
lang = st.radio("This is radio button label", options=langs)

st.write(f"selected language is `{lang}`")

'-----------------------------------------'

vehicle = st.selectbox(
    label = 'Favourite Vehicle?',
    options = ('Car', 'Bike', 'Truck', 'other')
)

st.write(f'Favourite Vehicle: {vehicle}')

'-----------------------------------------'

colors_selected = st.multiselect(
    label = 'Choose multiple colors',
    options = ['White', 'Red', 'Yellow', 'Green', 'Blue'],
    default = ['Yellow', 'Red'])

st.write('You selected:', colors_selected)


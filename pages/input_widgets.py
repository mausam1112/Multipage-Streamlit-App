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

st.write('selected colors:', colors_selected)

'-----------------------------------------'

color = st.select_slider(
    'Choose a color',
    options= ['White', 'Red', 'Yellow', 'Green', 'Blue'])
st.write('selected color: ', color)

'-----------------------------------------'

start_value, end_value = st.select_slider(
    'Select a range of color wavelength',
    options=[1, 2, 3, 4, 5, 6, 7, 8],
    value=(2, 6))
st.write('seleted between', start_value, 'and', end_value)

'-----------------------------------------'

demo_btn = st.button("click button")

if demo_btn:
    st.toast("Button is Clicked")

'-----------------------------------------'

color = st.color_picker("Choose the colors")
if color:
    st.toast(f"`{color}` is chose.")

'-----------------------------------------'

bday = st.date_input("select your birthday")
if bday:
    st.toast(f"Your birth date is {bday}")

'-----------------------------------------'

sleep_time = st.time_input("Select the time of sleep")
if sleep_time:
    st.toast(f"Your sleep time is {sleep_time}")

'-----------------------------------------'

file = st.file_uploader("Upload your file:")

if file is not None:
    st.success("File uploaded successfully.")
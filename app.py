import streamlit as st
from multiapp import MultiApp
from apps import GPdata, gpusers
# import your app modules here

app = MultiApp()

st.set_page_config(layout="wide")
st.markdown("""
# POLYGON MEGA DASH
""")

# Add all your application here
app.add_app("GPdata", GPdata.app)
app.add_app("gpusers", gpusers.app)




# The main app
app.run()
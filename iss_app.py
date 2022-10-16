import streamlit as st
import pandas as pd
import plotly.express as px
import reverse_geocoder as rg

from pinotdb import connect
from streamlit_autorefresh import st_autorefresh
from streamlit_tags import st_tags
from datetime import datetime
from app import *

st_autorefresh(interval=50, key="fizzy")

st.title("Near Real Time Location of the ISS")

now = datetime.now()
dt_string = now.strftime("%d %B %Y %H:%M:%S")
st.write(f"Last update: {dt_string}")

conn = connect(host="localhost", port="8099", path="/query/sql", scheme="http")

query = """
SELECT * 
FROM iss 
LIMIT 10
"""
curs = conn.cursor()
curs.execute(query)
df = pd.DataFrame(curs, columns=[item[0] for item in curs.description])

# location = rg.search([df['latitude'][0], df['longitude'][0]])
# city = location[0]["name"]
# state = location[0]["admin1"]

# st.write(f"Current location: {city}, {state}")

st.dataframe(df)

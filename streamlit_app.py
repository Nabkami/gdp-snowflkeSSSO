import pandas as pd
import snowflake.connector
import streamlit as st

# Verificando las claves en st.secrets
st.write("Available keys in st.secrets:", list(st.secrets.keys()))

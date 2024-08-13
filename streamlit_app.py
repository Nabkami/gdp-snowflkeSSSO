import pandas as pd
import snowflake.connector
import streamlit as st

# Snowflake Connection
def snowflake_conn():
    return snowflake.connector.connect(**st.secrets["snowflake"])

# Llamando a la función de conexión a Snowflake
conn = snowflake_conn()

# Ejecutando Consulta
query = 'SELECT 1'
# Leyendo los datos
df = pd.read_sql(query, conn)
# Mostrando los datos
st.write(df)

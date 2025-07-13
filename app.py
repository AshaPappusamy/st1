import streamlit as st

# Create the SQL connection
conn = st.connection("mysql", type="sql")

# Run a query (cached for 10 minutes)
df = conn.query("SELECT * FROM asteroids;", ttl=600)

# Display results
st.dataframe(df)

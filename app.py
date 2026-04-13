import streamlit as st
import pandas as pd
from utils.db import run_query, get_schema
from utils.llm import generate_sql
from utils.validator import is_safe_query

st.set_page_config(page_title="AI SQL Assistant", layout="wide")

st.title("🧠 AI Natural Language to SQL Assistant")

query = st.text_input("Ask your data question:")

if query:
    schema = get_schema()
    
    sql_query = generate_sql(query, schema)
    
    st.subheader("📝 Generated SQL")
    st.code(sql_query, language="sql")

    if is_safe_query(sql_query):
        try:
            df = run_query(sql_query)
            st.subheader("📊 Results")
            st.dataframe(df)

            if not df.empty:
                st.subheader("📈 Visualization")
                st.bar_chart(df.select_dtypes(include='number'))
        except Exception as e:
            st.error(f"Error executing query: {e}")
    else:
        st.error("⚠️ Unsafe query detected!")

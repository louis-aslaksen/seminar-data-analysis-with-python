import streamlit as st

# Page settings
st.set_page_config(page_title="Stock Analytics", layout="wide")

# Register pages
pages = [
    st.Page("stock_explorer.py", title="Stock Explorer", default=True),
    st.Page("pages/1_Stock_Detail.py", title="Stock Detail"),
    st.Page("pages/2_Options_Detail.py", title="Options Detail"),
]

# Run navigation
pg = st.navigation(pages, position="hidden")
pg.run()

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Contact Data Visualizer", layout="wide")
st.title("📊 Contact Data Visualizer (Excel)")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # Metrics Section
    total_companies = df['Company Name'].nunique() if 'Company Name' in df.columns else 0
    total_contacts = len(df)
    connected_calls = df[df['call'] == "Connected"].shape[0] if 'call' in df.columns else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Companies", total_companies)
    col2.metric("Total Contacts", total_contacts)
    col3.metric("Connected Calls", connected_calls)

    # --- Contact Information Overview ---
    st.subheader("📊 Contact Information Overview")

    has_email = df['Email Id'].notna().sum() if 'Email Id' in df.columns else 0
    missing_email = df['Email Id'].isna().sum() if 'Email Id' in df.columns else 0

    has_contact = df['Contact No.'].notna().sum() if 'Contact No.' in df.columns else 0
    missing_contact = df['Contact No.'].isna().sum() if 'Contact No.' in df.columns else 0

    linkedin_col = None
    for col in df.columns:
        if col.strip().lower() in ['linkedin profile', 'linkedlin profile']:
            linkedin_col = col
            break
    has_linkedin = df[linkedin_col].notna().sum() if linkedin_col else 0
    missing_linkedin = df[linkedin_col].isna().sum() if linkedin_col else 0

    status_counts = df['Call Status'].dropna().str.strip().value_counts() if 'Call Status' in df.columns else pd.Series()

    # --- Charts in Columns ---
    col4, col5, col6 = st.columns(3)

    with col4:
        fig_contact = px.bar(x=['Has Contact No.', 'Missing Contact No.'], y=[has_contact, missing_contact],
                             title='☎️ Contact Number Presence', color=['Has Contact No.', 'Missing Contact No.'],
                             color_discrete_map={'Has Contact No.': '#4CAF50', 'Missing Contact No.': '#F44336'})
        st.plotly_chart(fig_contact, use_container_width=True)

    with col5:
        fig_email = px.bar(x=['Has Email', 'Missing Email'], y=[has_email, missing_email],
                          title='📧 Email Presence', color=['Has Email', 'Missing Email'],
                          color_discrete_map={'Has Email': '#2196F3', 'Missing Email': '#FF9800'})
        st.plotly_chart(fig_email, use_container_width=True)

    with col6:
        fig_linkedin = px.bar(x=['Has LinkedIn', 'Missing LinkedIn'], y=[has_linkedin, missing_linkedin],
                             title='🔗 LinkedIn Profile Presence', color=['Has LinkedIn', 'Missing LinkedIn'],
                             color_discrete_map={'Has LinkedIn': '#0077B5', 'Missing LinkedIn': '#B0BEC5'})
        st.plotly_chart(fig_linkedin, use_container_width=True)

    col7, col8 = st.columns(2)

    with col7:
        if not status_counts.empty:
            fig_call_status = px.pie(status_counts, values=status_counts.values, names=status_counts.index,
                                      title="📞 Call Status Distribution")
            st.plotly_chart(fig_call_status, use_container_width=True)
        else:
            st.write("No Call Status Data Available")

    with col8:
        if 'Company Name' in df.columns:
            company_counts = df['Company Name'].dropna().value_counts().head(10)
            fig_company_counts = px.bar(x=company_counts.index, y=company_counts.values,
                                         title="🏢 Top 10 Companies by Contact Count",
                                         labels={'x': 'Company Name', 'y': 'Contact Count'})
            st.plotly_chart(fig_company_counts, use_container_width=True)

    # 👔 Top Job Titles
    if 'Title' in df.columns:
        st.subheader("👔 Top 10 Job Titles")
        title_counts = df['Title'].dropna().str.strip().value_counts().head(10)
        fig_title_counts = px.bar(x=title_counts.index, y=title_counts.values,
                                     title="👔 Top 10 Job Titles",
                                     labels={'x': 'Job Title', 'y': 'Count'})
        st.plotly_chart(fig_title_counts, use_container_width=True)

    # 🔎 Filtered Table by Website Status
    if 'Website Status' in df.columns:
        st.subheader("🔎 Filtered Table by Website Status")
        unique_statuses = df['Website Status'].dropna().unique()
        selected_status = st.multiselect("Select Website Status(es) to Filter", unique_statuses)
        if selected_status:
            filtered_df = df[df['Website Status'].isin(selected_status)]
            st.dataframe(filtered_df)
        else:
            st.info("Select at least one Website Status to see filtered data.")

    # 📞 Call Status by Company
    if 'Company Name' in df.columns and 'Call Status' in df.columns:
        st.subheader("📞 Call Status by Company")
        call_status_by_company = (
            df.groupby(['Company Name', 'Call Status'])
            .size()
            .unstack(fill_value=0)
            .sort_index(ascending=True)
        )
        st.dataframe(call_status_by_company)
        st.bar_chart(call_status_by_company)

    # 🏢 All Companies and Their Contact Details
    if 'Company Name' in df.columns:
        st.subheader("🏢 All Companies and Their Contact Details")
        detail_cols = ['Company Name', 'Name', 'Title', 'Email Id', 'Contact No.', 'Linkedin Profile', 'Website', 'Call Status', 'call']
        available_cols = [col for col in detail_cols if col in df.columns]
        company_details = df[available_cols].sort_values('Company Name')
        st.dataframe(company_details)

    # 📈 Company-wise Call Summary
    if 'Company Name' in df.columns and 'call' in df.columns:
        st.subheader("📈 Company-wise Call Summary")
        company_call_summary = (
            df.groupby('Company Name')['call']
            .value_counts()
            .unstack(fill_value=0)
            .sort_index(ascending=True)
        )
        st.dataframe(company_call_summary)
        st.bar_chart(company_call_summary)

else:
    st.info("Please upload an Excel file to get started.")

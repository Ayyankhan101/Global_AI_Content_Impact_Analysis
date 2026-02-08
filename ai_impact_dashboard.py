import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(
    page_title="Global AI Content Impact Dashboard",
    page_icon="🤖",
    layout="wide"
)

# Title and description
st.title("🤖 Global AI Content Impact Dashboard")
st.markdown("""
This dashboard provides insights into how artificial intelligence adoption impacts various industries and countries globally.
""")

@st.cache_data
def load_data():
    """Load the dataset"""
    df = pd.read_csv('Global_AI_Content_Impact_Dataset.csv')
    return df

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

# Country filter
countries = st.sidebar.multiselect(
    'Select Countries',
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

# Industry filter
industries = st.sidebar.multiselect(
    'Select Industries',
    options=df['Industry'].unique(),
    default=df['Industry'].unique()
)

# Year filter
years = st.sidebar.multiselect(
    'Select Years',
    options=sorted(df['Year'].unique()),
    default=sorted(df['Year'].unique())
)

# Apply filters
filtered_df = df[
    (df['Country'].isin(countries)) &
    (df['Industry'].isin(industries)) &
    (df['Year'].isin(years))
]

# Main dashboard sections
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "AI Adoption", "Economic Impact", "Social Impact", "Tools & Regulations"])

with tab1:
    st.header("Dataset Overview")
    
    # Basic metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", len(filtered_df))
    with col2:
        st.metric("Countries", filtered_df['Country'].nunique())
    with col3:
        st.metric("Industries", filtered_df['Industry'].nunique())
    with col4:
        st.metric("Years Range", f"{int(filtered_df['Year'].min())} - {int(filtered_df['Year'].max())}")
    
    # Distribution charts
    col1, col2 = st.columns(2)
    
    with col1:
        country_dist = filtered_df['Country'].value_counts().reset_index()
        country_dist.columns = ['Country', 'Count']
        fig1 = px.bar(country_dist, x='Country', y='Count', title='Records by Country')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        industry_dist = filtered_df['Industry'].value_counts().reset_index()
        industry_dist.columns = ['Industry', 'Count']
        fig2 = px.pie(industry_dist, values='Count', names='Industry', title='Records by Industry')
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.header("AI Adoption Analysis")
    
    # AI Adoption Rate by Country
    col1, col2 = st.columns(2)
    
    with col1:
        avg_adoption_country = filtered_df.groupby('Country')['AI Adoption Rate (%)'].mean().reset_index()
        fig3 = px.bar(avg_adoption_country, x='Country', y='AI Adoption Rate (%)', 
                      title='Average AI Adoption Rate by Country')
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        avg_adoption_industry = filtered_df.groupby('Industry')['AI Adoption Rate (%)'].mean().reset_index()
        fig4 = px.bar(avg_adoption_industry, x='Industry', y='AI Adoption Rate (%)', 
                      title='Average AI Adoption Rate by Industry')
        st.plotly_chart(fig4, use_container_width=True)
    
    # AI Adoption vs Year trend
    yearly_adoption = filtered_df.groupby('Year')['AI Adoption Rate (%)'].mean().reset_index()
    fig5 = px.line(yearly_adoption, x='Year', y='AI Adoption Rate (%)', 
                   title='Average AI Adoption Rate Over Time')
    st.plotly_chart(fig5, use_container_width=True)

with tab3:
    st.header("Economic Impact of AI")
    
    # Revenue increase vs AI adoption
    fig6 = px.scatter(filtered_df, x='AI Adoption Rate (%)', y='Revenue Increase Due to AI (%)',
                     color='Country', hover_data=['Industry', 'Year'],
                     title='AI Adoption Rate vs Revenue Increase')
    st.plotly_chart(fig6, use_container_width=True)
    
    # Job loss vs AI adoption
    fig7 = px.scatter(filtered_df, x='AI Adoption Rate (%)', y='Job Loss Due to AI (%)',
                     color='Country', hover_data=['Industry', 'Year'],
                     title='AI Adoption Rate vs Job Loss')
    st.plotly_chart(fig7, use_container_width=True)
    
    # Market share by country
    avg_market_share = filtered_df.groupby('Country')['Market Share of AI Companies (%)'].mean().reset_index()
    fig8 = px.bar(avg_market_share, x='Country', y='Market Share of AI Companies (%)',
                  title='Average Market Share of AI Companies by Country')
    st.plotly_chart(fig8, use_container_width=True)

with tab4:
    st.header("Social Impact of AI")
    
    # Consumer trust vs AI adoption
    fig9 = px.scatter(filtered_df, x='AI Adoption Rate (%)', y='Consumer Trust in AI (%)',
                     color='Country', hover_data=['Industry', 'Year'],
                     title='AI Adoption Rate vs Consumer Trust')
    st.plotly_chart(fig9, use_container_width=True)
    
    # Human-AI collaboration rate
    col1, col2 = st.columns(2)
    
    with col1:
        avg_collab_country = filtered_df.groupby('Country')['Human-AI Collaboration Rate (%)'].mean().reset_index()
        fig10 = px.bar(avg_collab_country, x='Country', y='Human-AI Collaboration Rate (%)',
                       title='Average Human-AI Collaboration Rate by Country')
        st.plotly_chart(fig10, use_container_width=True)
    
    with col2:
        avg_collab_industry = filtered_df.groupby('Industry')['Human-AI Collaboration Rate (%)'].mean().reset_index()
        fig11 = px.bar(avg_collab_industry, x='Industry', y='Human-AI Collaboration Rate (%)',
                       title='Average Human-AI Collaboration Rate by Industry')
        st.plotly_chart(fig11, use_container_width=True)

with tab5:
    st.header("AI Tools and Regulations")
    
    # Top AI tools used
    tool_counts = filtered_df['Top AI Tools Used'].value_counts().reset_index()
    tool_counts.columns = ['Tool', 'Count']
    fig12 = px.bar(tool_counts, x='Count', y='Tool', orientation='h',
                   title='Most Popular AI Tools')
    st.plotly_chart(fig12, use_container_width=True)
    
    # Regulation status distribution
    regulation_counts = filtered_df['Regulation Status'].value_counts().reset_index()
    regulation_counts.columns = ['Status', 'Count']
    fig13 = px.pie(regulation_counts, values='Count', names='Status',
                   title='Distribution of AI Regulation Status')
    st.plotly_chart(fig13, use_container_width=True)
    
    # AI-Generated Content Volume
    fig14 = px.scatter(filtered_df, x='AI Adoption Rate (%)', y='AI-Generated Content Volume (TBs per year)',
                      color='Country', hover_data=['Industry', 'Year'],
                      title='AI Adoption Rate vs AI-Generated Content Volume')
    st.plotly_chart(fig14, use_container_width=True)

# Detailed data view
st.header("Detailed Dataset View")
st.dataframe(filtered_df)

# Download button for filtered data
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_ai_impact_data.csv',
    mime='text/csv'
)

# Footer
st.markdown("---")
st.markdown("Dashboard created with 🤖 Global AI Content Impact Dataset | Streamlit")
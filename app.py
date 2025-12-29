import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Dashboard", layout='wide')

st.title('Sales performance Dashboard')

#loading data

@st.cache_data
def load_data():
    df=pd.read_csv('data\sales_data.csv')
    df['Date']=pd.to_datetime(df['Date'])
    return df

df= load_data()
st.header('Key Metrics')
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_revenue = df['Total'].sum()
    st.metric('Total Revenue', f'${total_revenue:,.0f}')

with col2:
    total_sales = len(df)
    st.metric('Total Sales', f'{total_sales:}')

with col3:
    avg_sales = df['Total'].mean()
    st.metric('Average sales', f'${avg_sales:,.0f}')

with col4:
    qty = df['Quantity'].sum()
    st.metric('Total Quantity', f'{qty}')

st.header('Product Revenue Visualization')

product_revenue = df.groupby('Product')['Total'].sum().sort_values(ascending=True)

fig1, ax1 = plt.subplots(figsize=(10 ,6))

sns.barplot(x=product_revenue.values, y=product_revenue.index, palette='Blues' , ax=ax1)
ax1.set_xlabel("Revenue($)")
ax1.set_ylabel('Product')
ax1.set_title('Product Revenue Visualization')
st.pyplot(fig1)

st.divider()

st.header('Monthly Trend Visualization')
df['Month'] = df['Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total'].sum()

fig2, ax2 = plt.subplots(figsize=(10, 6))
monthly_sales.plot(kind= 'line', marker='o', ax=ax2)
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')
ax2.grid(True, alpha= 0.3)
ax2.tick_params(axis= 'x', rotation=45)
st.pyplot(fig2)

st.divider()

st.header(' Regional Distribution Visualization')
reg_sales = df.groupby('Region')['Total'].sum()

fig3, ax3 = plt.subplots(figsize=(8, 8))
color = sns.color_palette('pastel')
ax3.pie(reg_sales.values, startangle = 90, colors=color, autopct= '%1.1f%%', labels=reg_sales.index)
ax3.set_title(' Regional Distribution Visualization')
st.pyplot(fig3)

st.divider()
st.header('Quantity Prduct visulization')
qty_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=True)

fig4, ax4 = plt.subplots(figsize=(10, 10))
sns.barplot(x=qty_product.values, y=qty_product.index, palette= 'Set2', ax=ax4)
ax4.set_xlabel('Quantity')
ax4.set_ylabel('Product')
plt.title('Quantity Prduct visulization')
st.pyplot(fig4)

st.divider()

st.header("Raw data")
st.dataframe(df, use_container_width=True)
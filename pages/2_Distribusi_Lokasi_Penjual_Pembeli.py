import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Perbandingan persebaran lokasi penjual dengan pembeli")

st.sidebar.success("Berikut Penjelasannya!!!")
st.sidebar.info(
    """Berdasarkan distribusi lokasi penjual, Sao Paulo memiliki jumlah penjual terbanyak dengan 694 penjual, diikuti oleh Curitiba (127 penjual) dan Rio de Janeiro (96 penjual). Sedangkan dari distribusi lokasi pembeli, Sao Paulo juga mendominasi dengan 15,540 pembeli, diikuti oleh Rio de Janeiro (6,882 pembeli) dan Belo Horizonte (2,773 pembeli). Analisis ini menunjukkan bahwa Sao Paulo menjadi pusat aktivitas perdagangan yang signifikan, baik sebagai lokasi penjual maupun pembeli. Curitiba dan Rio de Janeiro juga menonjol sebagai lokasi dengan aktivitas perdagangan yang cukup tinggi."""
)

sellers_df = pd.read_csv('pages/sellers_dataset.csv')
customers_df = pd.read_csv('pages/customers_dataset.csv')

st.header("Pertanyaan 3: Bagaimana perbandingan persebaran lokasi penjual dengan pembeli?")
st.write("Perbandingan persebaran lokasi penjual dengan pembeli dapat dilihat sebagai berikut.")

st.subheader("10 Lokasi dengan Jumlah Penjual Terbanyak")
seller_city_distribution = sellers_df['seller_city'].value_counts()
fig, ax = plt.subplots(figsize=(6, 12))
ax.barh(seller_city_distribution.head(10).sort_values().index, seller_city_distribution.head(10).sort_values().values, color='lightcoral')
ax.set_xlabel('Jumlah Penjual')
ax.set_ylabel('Kota Penjual')
for i, v in enumerate(seller_city_distribution.head(10).sort_values().values):
    ax.text(v + 1, i, str(v), color='black', ha='left', va='center')
st.pyplot(fig)

st.subheader("10 Lokasi dengan Jumlah Pembeli Terbanyak")
customer_city_distribution = customers_df['customer_city'].value_counts()
fig, ax = plt.subplots(figsize=(6, 12))
ax.barh(customer_city_distribution.head(10).sort_values().index, customer_city_distribution.head(10).sort_values().values, color='lightblue')
ax.set_xlabel('Jumlah Pembeli')
ax.set_ylabel('Kota Pembeli')
for i, v in enumerate(customer_city_distribution.head(10).sort_values().values):
    ax.text(v + 1, i, str(v), color='black', ha='left', va='center')
st.pyplot(fig)
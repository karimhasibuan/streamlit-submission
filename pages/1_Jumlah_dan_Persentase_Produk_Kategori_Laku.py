import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Kategori produk yang paling banyak laku dan paling sedikit beserta persentasenya")

products_df = pd.read_csv('pages/products_translated_dataset.csv')

st.header("Pertanyaan 1: Apa kategori produk yang paling banyak laku dan paling sedikit?")
st.write("Kategori produk yang paling banyak laku dan paling sedikit dapat dilihat sebagai berikut.")
st.subheader("10 Kategori Produk Paling Banyak Laku")
product_category_counts = products_df['product_category_name_english'].value_counts()
top_product_category = product_category_counts.head(10).sort_values()
fig, ax = plt.subplots(figsize=(9, 10))
ax.barh(top_product_category.index, top_product_category.values, color='skyblue')
ax.set_xlabel('Jumlah Penjualan')

for i, v in enumerate(top_product_category.values):
    ax.text(v + 10, i, str(v), color='black', ha='left', va='center')

st.pyplot(fig)

st.subheader("10 Kategori Produk Paling Sedikit Laku")
bottom_product_category = product_category_counts.tail(10).sort_values()
fig, ax = plt.subplots(figsize=(9, 10))
ax.barh(bottom_product_category.index, bottom_product_category.values, color='salmon')
ax.set_xlabel('Jumlah Penjualan')

for i, v in enumerate(bottom_product_category.values):
    ax.text(v + 1, i, str(v), color='black', ha='left', va='center')

st.pyplot(fig)


# Pertanyaaan ke 2
st.header("Pertanyaan 2: Bagaimana persentase kategori produk yang laku?")
st.write("Persentase kategori produk yang laku dapat dilihat sebagai berikut.")
percentage_sales = (products_df['product_category_name_english'].value_counts() / len(products_df)) * 100
fig, ax = plt.subplots(figsize=(9, 13))
ax.set_title('Persentase Penjualan untuk Setiap Kategori Produk')
ax.barh(percentage_sales.sort_values().index, percentage_sales.sort_values().values, color='lightgreen')
ax.set_xlabel('Persentase Penjualan')
ax.set_ylabel('Product Category')
for i, v in enumerate(percentage_sales.sort_values().values):
    ax.text(v + 0.5, i, f'{v:.2f}%', color='black', ha='left', va='center')
st.pyplot(fig)
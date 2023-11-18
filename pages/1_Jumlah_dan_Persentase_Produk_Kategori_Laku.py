import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Kategori produk yang paling banyak laku dan paling sedikit beserta persentasenya")

st.sidebar.success("Berikut Penjelasannya!!!")
st.sidebar.info(
    """Dari data penjualan, dapat disimpulkan bahwa 10 kategori produk yang paling banyak laku secara berturut adalah "bed_bath_table", "sports_leisure", "furniture_decor", "health_beauty", "housewares", "auto", "computers_accessories", "toys", "watches_gifts", dan "telephony". Kategori-kategori ini menunjukkan popularitas tinggi dengan jumlah penjualan tertinggi, memainkan peran signifikan dalam kontribusi total penjualan. Di sisi lain, 10 kategori produk yang paling sedikit laku adalah "fashion_sport", "flowers", "diapers_and_hygiene", "la_cuisine", "furniture_mattress_and_upholstery", "tablets_printing_image", "fashion_childrens_clothes", "home_comfort_2", "security_and_services", dan "cds_dvds_musicals"."""
)
st.sidebar.info(
    """Kategori produk "bed_bath_table" mendominasi dengan persentase penjualan sekitar 9.37%, diikuti oleh "sports_leisure" dan "furniture_decor" dengan persentase masing-masing sekitar 8.87% dan 8.22%. Sebaliknya, kategori-kategori seperti "tablets_printing_image", "fashion_childrens_clothes", "home_comfort_2", "security_and_services", dan "cds_dvds_musicals" memiliki kontribusi penjualan yang relatif rendah, masing-masing di bawah 0.03%."""
)

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
import streamlit as st
import pandas as pd


st.set_page_config(page_title="Home", page_icon=":bar_chart:", layout="wide")

st.title("Brazilian E-Commerce Dashboard - Dicoding Submission")
st.write("Author: Karimuddin Hakim Hasibuan")

st.sidebar.title("Additional Information")
page_options = ["Jumlah dan Persentase Produk Kategori Laku", "Distribusi Lokasi Penjual Pembeli", "Produk Kategori Laku dengan Review"]

products_df = pd.read_csv('pages/products_translated_dataset.csv')
sellers_df = pd.read_csv('pages/sellers_dataset.csv')
customers_df = pd.read_csv('pages/customers_dataset.csv')
items_reviews_df = pd.read_csv('pages/items_products_reviews.csv')

st.sidebar.markdown("[Link to Full Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")
st.sidebar.markdown("[Link to Dicoding Class](https://www.dicoding.com/academies/555/tutorials/31230)")

st.write("Pada dashboard ini menampilkan visualisasi dari dataset Brazilian E-Commerce yang diambil dari Kaggle.")
st.write("Berikut pertanyaan yang divisualisasikan:")
st.write("- Apa kategori produk yang paling banyak laku dan paling sedikit?")
st.write("- Bagaimana persentase kategori produk yang laku?")
st.write("- Bagaimana perbandingan persebaran lokasi penjual dengan pembeli?")
st.write("- Bagaimana perbandingan antara jumlah kategori produk yang laku dengan review score-nya?")

st.write("Untuk melihat hasil visualisasinya silahkan pilih menu di sidebar.")

st.header("Berikut dataset yang digunakan:")
st.subheader("Produk Dataset")
st.dataframe(products_df.head())

st.subheader("Penjual Dataset")
st.dataframe(sellers_df.head())
st.subheader("Pembeli Dataset")
st.dataframe(customers_df.head())

st.subheader("Product Item Review Dataset")
st.dataframe(items_reviews_df.head())


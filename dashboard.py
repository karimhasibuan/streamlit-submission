import streamlit as st
import pandas as pd


st.set_page_config(page_title="Home", page_icon=":bar_chart:", layout="wide")

st.title("Brazilian E-Commerce Dashboard - Dicoding Submission")
st.write("Author: Karimuddin Hakim Hasibuan")

st.sidebar.title("Additional Information")
st.sidebar.markdown("[Link to Full Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")
st.sidebar.markdown("[Link to Dicoding Class](https://www.dicoding.com/academies/555/tutorials/31230)")

st.write("Pada dashboard ini menampilkan visualisasi dari dataset Brazilian E-Commerce yang diambil dari Kaggle.")
st.write("Berikut pertanyaan yang divisualisasikan:")
st.write("- Apa kategori produk yang paling banyak laku dan paling sedikit?")
st.write("- Bagaimana persentase kategori produk yang laku?")
st.write("- Bagaimana perbandingan persebaran lokasi penjual dengan pembeli?")
st.write("- Bagaimana perbandingan antara jumlah kategori produk yang laku dengan review score-nya?")

st.write("Untuk melihat hasil visualisasinya silahkan pilih menu di sidebar.")



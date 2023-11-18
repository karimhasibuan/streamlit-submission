import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Perbandingan antara jumlah kategori produk yang laku dengan review score")

st.sidebar.success("Berikut Penjelasannya!!!")
st.sidebar.info(
    """Visualisasi jumlah produk berdasarkan review score untuk beberapa kategori produk, terlihat bahwa kategori "health_beauty", "bed_bath_table", dan "sports_leisure" memiliki jumlah produk yang paling tinggi yang mendapatkan rating 5.
    Khususnya, kategori "health_beauty" menonjol dengan total 5858 produk yang mendapat rating 5 meskipun bukan sebagai kategori produk dengan angka penjualan tertinggi.Kemudian diikuti oleh "bed_bath_table" dengan 5785 produk dan "sports_leisure" dengan 5121 produk.
    Hal ini menunjukkan bahwa produk-produk dalam kategori tersebut mendapat penerimaan yang tinggi dari pelanggan, termanifestasi dalam jumlah besar produk yang mendapat rating tertinggi."""
)

items_reviews_df = pd.read_csv('pages/items_products_reviews.csv')

st.header("Pertanyaan 4: Bagaimana perbandingan antara jumlah kategori produk yang laku dengan review score-nya?")

st.write("Perbandingan antara jumlah kategori produk yang laku dengan review score dapat dilihat sebagai berikut.")
category_review_counts = items_reviews_df.groupby(['product_category_name_english', 'review_score']).size().unstack(fill_value=0)

category_review_counts_sorted = category_review_counts.sort_values(by=5, ascending=False)

category_review_counts_sorted['Total Products'] = category_review_counts_sorted.sum(axis=1)

fig, ax = plt.subplots(figsize=(12, 50))
sns.heatmap(category_review_counts_sorted, cmap='Blues', annot=True, fmt='g', linewidths=.5, cbar_kws={'label': 'Total Products'})
ax.set_title('Perbandingan Jumlah Kategori Produk yang Laku dengan Review Score')
ax.set_xlabel('Review Score')
ax.set_ylabel('Product Category')

st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Perbandingan antara jumlah kategori produk yang laku dengan review score")

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


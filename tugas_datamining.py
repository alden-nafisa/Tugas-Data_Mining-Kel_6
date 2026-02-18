import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# BAGIAN 1: DATA PREPARATION (PERSIAPAN)
# ==========================================
print("=== MULAI PROSES DATA MINING ===")

# 1. Memuat Data
# Pastikan nama file sesuai dengan yang kamu download
df = pd.read_csv('ecommerce_sales_analysis.csv') 

# 2. Cek Kualitas Data (Data Cleaning)
print("\n[1] Pengecekan Missing Value:")
print(df.isnull().sum()) # Harusnya 0 semua jika bersih

print("\n[2] Pengecekan Duplikasi:")
print(f"Jumlah baris duplikat: {df.duplicated().sum()}")

# ==========================================
# BAGIAN 2: FEATURE ENGINEERING (PENGOLAHAN)
# ==========================================

# Kita butuh data 'Total Penjualan Setahun', tapi datanya terpisah per bulan.
# Jadi kita jumlahkan kolom sales_month_1 sampai 12.
list_bulan = [f'sales_month_{i}' for i in range(1, 13)]
df['total_sales'] = df[list_bulan].sum(axis=1)

print("\n[3] Transformasi Data Selesai.")
print("Kolom baru 'total_sales' berhasil ditambahkan.")

# ==========================================
# BAGIAN 3: STATISTIK DESKRIPTIF
# ==========================================
print("\n[4] Statistik Ringkasan (Mean, Min, Max):")
# Kita ambil kolom numerik utama saja
statistik = df[['price', 'review_score', 'total_sales']].describe()
print(statistik)

print("\n[5] Mencari Modus (Nilai Terbanyak Muncul):")
print(df[['price', 'review_score']].mode().iloc[0])

# ==========================================
# BAGIAN 4: VISUALISASI DATA (MEMBUAT GRAFIK)
# ==========================================
print("\n[6] Sedang membuat grafik... Silakan cek folder kamu setelah ini.")

# Mengatur gaya grafik biar cantik
sns.set(style="whitegrid")

# --- GRAFIK 1: HISTOGRAM HARGA ---
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=20, kde=True, color='skyblue')
plt.title('Distribusi Harga Produk (Histogram)')
plt.xlabel('Harga ($)')
plt.ylabel('Frekuensi')
plt.savefig('grafik_1_histogram_harga.png') # Simpan jadi file gambar
print("-> Grafik 1 tersimpan: grafik_1_histogram_harga.png")
# plt.show() # Hapus tanda pagar jika ingin melihat langsung popup window

# --- GRAFIK 2: SCATTER PLOT (HARGA VS PENJUALAN) ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='total_sales', data=df, hue='category', alpha=0.7)
plt.title('Hubungan Harga vs Total Penjualan (Scatter Plot)')
plt.xlabel('Harga ($)')
plt.ylabel('Total Unit Terjual')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('grafik_2_scatter_plot.png')
print("-> Grafik 2 tersimpan: grafik_2_scatter_plot.png")

# --- GRAFIK 3: BOXPLOT (REVIEW SCORE) ---
plt.figure(figsize=(12, 6))
sns.boxplot(x='category', y='review_score', data=df, palette="Set3")
plt.title('Sebaran Review Score per Kategori (Boxplot)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafik_3_boxplot_review.png')
print("-> Grafik 3 tersimpan: grafik_3_boxplot_review.png")

print("\n=== SELESAI! ===")
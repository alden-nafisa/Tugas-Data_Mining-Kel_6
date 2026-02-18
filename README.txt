README - Petunjuk Instalasi dan Menjalankan `tugas_datamining.py`

Ringkasan Proyek
- Skrip `tugas_datamining.py` melakukan persiapan data, transformasi (menjumlahkan penjualan bulanan menjadi `total_sales`), menampilkan statistik deskriptif, dan menyimpan tiga grafik (histogram harga, scatter price vs total_sales, boxplot review score per kategori).

Sumber Dataset
- Dataset yang digunakan (file CSV) berasal dari:
  https://www.kaggle.com/datasets/sidramazam/e-commerce-sales-performance-analysis

Prasyarat
- Python 3.8+ terinstal (direkomendasikan 3.10+).
- Ruang kerja/proyek di: D:\\ngoding\\Data_Mining\\Tugas-Data_Mining-Kel_6
- File `ecommerce_sales_analysis.csv` berada di folder proyek.

Instalasi dan Persiapan (Windows PowerShell)
1. Buat virtual environment (jika belum):

```powershell
python -m venv .venv
```

2. Aktifkan venv:

```powershell
& .\.venv\\Scripts\\Activate.ps1
```

3. Upgrade `pip` di dalam venv:

```powershell
& .\\.venv\\Scripts\\python.exe -m pip install --upgrade pip
```

4. Install dependensi:

```powershell
& .\\.venv\\Scripts\\python.exe -m pip install pandas matplotlib seaborn
```

Verifikasi Instalasi

```powershell
& .\\.venv\\Scripts\\python.exe -m pip --version
& .\\.venv\\Scripts\\python.exe -c "import pandas,matplotlib,seaborn; print(pandas.__version__, matplotlib.__version__, seaborn.__version__)"
```

Menjalankan Skrip

```powershell
& .\\.venv\\Scripts\\python.exe tugas_datamining.py
```

Output yang Diharapkan
- Pesan progres di terminal (cek missing values, statistik, dll.).
- File gambar yang dihasilkan:
  - grafik_1_histogram_harga.png
  - grafik_2_scatter_plot.png
  - grafik_3_boxplot_review.png

Struktur File (ringkas)
- `tugas_datamining.py` : skrip utama.
- `ecommerce_sales_analysis.csv` : dataset input (harus ada di folder yang sama).
- `README.txt` : panduan ini.
- `grafik_*.png` : file output grafik setelah menjalankan skrip.

Input yang Diharapkan
- CSV harus memiliki kolom berikut minimal:
  - `sales_month_1` ... `sales_month_12` (atau setara)
  - `price` (numerik)
  - `review_score` (numerik)
  - `category` (kategorikal, untuk pewarnaan pada plot)

Catatan penting:
- Jika ada missing value pada kolom bulan, penjumlahan `total_sales` dapat menghasilkan NaN — pertimbangkan `fillna(0)` untuk kolom bulan jika sesuai.

Troubleshooting & FAQ
- Error "Fatal error in launcher: Unable to create process ..." : gunakan `python -m pip` atau jalankan pip lewat interpreter venv (lihat perintah di atas). Penyebab biasanya venv dipindah atau launcher pip berisi path absolut lama.
- Jika venv rusak atau `python.exe` hilang dalam `.venv`, buat ulang venv:

```powershell
Remove-Item -Recurse -Force .\\.venv
python -m venv .venv
& .\\.venv\\Scripts\\Activate.ps1
& .\\.venv\\Scripts\\python.exe -m pip install --upgrade pip
& .\\.venv\\Scripts\\python.exe -m pip install pandas matplotlib seaborn
```

- Jika `pd.read_csv('ecommerce_sales_analysis.csv')` error: pastikan file ada di folder proyek dan format CSV (delimiter/encoding) sesuai.

Konfigurasi & Opsi
- Untuk mengubah path CSV, edit variabel path langsung di `tugas_datamining.py` atau tambahkan argumen command-line.
- Untuk kualitas gambar, Anda dapat menambahkan `dpi=` dan `bbox_inches='tight'` pada `plt.savefig()` di skrip.

Kontribusi
- Jika ingin menambahkan fitur: buat branch baru, tambahkan perubahan, dan uji secara lokal. Misalnya: validasi kolom, opsi CLI, atau ekspor hasil ke CSV.

Lisensi & Kontak
- Tentukan lisensi proyek (mis. MIT) jika ingin membagikan. Jika butuh bantuan, beri tahu saya melalui chat ini.

Butuh bantuan lain?
- Saya bisa membantu memodifikasi `tugas_datamining.py` (mis. validasi kolom, menambahkan `plt.close()` setelah `savefig()`, atau opsi CLI) dan menjalankan verifikasi. Beri tahu yang mau dikerjakan.

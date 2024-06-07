import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data_pembelian = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Jumlah Pembelian': [500, 300, 800, 1200, 700, 400, 1000, 600, 1500, 900, 1100, 1300],
    'Total Harga Pembelian': [75000, 42000, 120000, 180000, 105000, 60000, 150000, 90000, 225000, 135000, 165000, 195000]
}

data_persediaan = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Persediaan Awal': [1000, 1200, 1100, 1700, 1900, 1500, 1300, 1800, 1400, 2100, 1700, 2000],
    'Persediaan Akhir': [1200, 1100, 1700, 1900, 1500, 1300, 1800, 1400, 2100, 1700, 2000, 2200]
}

data_penjualan = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Jumlah Penjualan': [300, 400, 400, 500, 1100, 600, 500, 1000, 800, 1300, 600, 1100],
    'Total Pendapatan': [45000, 60000, 60000, 75000, 165000, 90000, 75000, 150000, 120000, 195000, 90000, 165000]
}

# Convert to DataFrame
df_pembelian = pd.DataFrame(data_pembelian)
df_persediaan = pd.DataFrame(data_persediaan)
df_penjualan = pd.DataFrame(data_penjualan)

# Scatterplot: Jumlah Pembelian vs Total Harga Pembelian
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Jumlah Pembelian', y='Total Harga Pembelian', data=df_pembelian, hue='Bulan', palette='tab10')
plt.title('Scatterplot Jumlah Pembelian vs Total Harga Pembelian')
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Total Harga Pembelian')
plt.legend(loc='best')
plt.show()

# Pie Chart: Persentase Jumlah Pembelian per Bulan
plt.figure(figsize=(8, 8))
plt.pie(df_pembelian['Jumlah Pembelian'], labels=df_pembelian['Bulan'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('tab10'))
plt.title('Persentase Jumlah Pembelian per Bulan')
plt.axis('equal')
plt.show()

# Bar Chart: Jumlah Penjualan per Bulan
plt.figure(figsize=(12, 6))
sns.barplot(x='Bulan', y='Jumlah Penjualan', data=df_penjualan, palette='tab10')
plt.title('Jumlah Penjualan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import statsmodels.api as sm

# Data
data_pembelian = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Jumlah Pembelian': [500, 300, 800, 1200, 700, 400, 1000, 600, 1500, 900, 1100, 1300],
    'Total Harga Pembelian': [75000, 42000, 120000, 180000, 105000, 60000, 150000, 90000, 225000, 135000, 165000, 195000]
}

# Convert to DataFrame
df_pembelian = pd.DataFrame(data_pembelian)

# Korelasi Pearson
correlation, p_value = pearsonr(df_pembelian['Jumlah Pembelian'], df_pembelian['Total Harga Pembelian'])
print(f'Korelasi Pearson: {correlation}, p-value: {p_value}')

# Analisis Regresi Linear
X = df_pembelian['Jumlah Pembelian']
y = df_pembelian['Total Harga Pembelian']
X = sm.add_constant(X)  # menambahkan konstanta

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Menampilkan hasil regresi
print(model.summary())

# Visualisasi scatterplot dengan garis regresi
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Jumlah Pembelian', y='Total Harga Pembelian', data=df_pembelian, hue='Bulan', palette='tab10')
plt.plot(df_pembelian['Jumlah Pembelian'], predictions, color='red', linewidth=2, label='Garis Regresi')
plt.title('Scatterplot Jumlah Pembelian vs Total Harga Pembelian dengan Garis Regresi')
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Total Harga Pembelian')
plt.legend(loc='best')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import statsmodels.api as sm

# Data
data_pembelian = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Jumlah Pembelian': [500, 300, 800, 1200, 700, 400, 1000, 600, 1500, 900, 1100, 1300],
    'Total Harga Pembelian': [75000, 42000, 120000, 180000, 105000, 60000, 150000, 90000, 225000, 135000, 165000, 195000]
}

data_penjualan = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Jumlah Penjualan': [300, 400, 400, 500, 1100, 600, 500, 1000, 800, 1300, 600, 1100],
    'Total Pendapatan': [45000, 60000, 60000, 75000, 165000, 90000, 75000, 150000, 120000, 195000, 90000, 165000]
}

# Convert to DataFrame
df_pembelian = pd.DataFrame(data_pembelian)
df_penjualan = pd.DataFrame(data_penjualan)

# Analisis Regresi Linear antara Jumlah Pembelian dan Total Harga Pembelian
X = df_pembelian['Jumlah Pembelian']
y = df_pembelian['Total Harga Pembelian']
X = sm.add_constant(X)  # menambahkan konstanta

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Menghitung target penjualan yang meningkat 20%
df_penjualan['Target Penjualan'] = df_penjualan['Jumlah Penjualan'] * 1.2

# Menggunakan model regresi untuk memprediksi jumlah pembelian yang diperlukan
target_pembelian = (df_penjualan['Target Penjualan'] - model.params['const']) / model.params['Jumlah Pembelian']

# Menyusun DataFrame untuk hasil proyeksi
df_proyeksi = pd.DataFrame({
    'Bulan': df_penjualan['Bulan'],
    'Target Penjualan': df_penjualan['Target Penjualan'],
    'Prediksi Jumlah Pembelian': target_pembelian
})

# Visualisasi Proyeksi Jumlah Pembelian
plt.figure(figsize=(12, 6))
sns.barplot(x='Bulan', y='Prediksi Jumlah Pembelian', data=df_proyeksi, palette='tab10')
plt.title('Proyeksi Jumlah Pembelian Bulanan dengan Penjualan Meningkat 20%')
plt.xlabel('Bulan')
plt.ylabel('Prediksi Jumlah Pembelian')
plt.xticks(rotation=45)
plt.show()

print(df_proyeksi)

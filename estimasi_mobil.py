# mengimport library yang dibutuhkan
import pickle
import streamlit as st
# memanggil model yang sudah di training
model = pickle.load(open('estimasi-mobil-bekas.sav', 'rb'))
# membuat judul aplikasi
st.title('Estimasi Harga Mobil Bekas')
# membuat deskripsi aplikasi
st.write('Aplikasi ini dapat memprediksi harga mobil bekas berdasarkan fitur yang diinputkan')
# membuat inputan untuk setiap fitur
year = st.number_input('Input Tahun Mobil', min_value=1990, max_value=2021)
mileage = st.number_input('Input Jarak Tempuh Mobil (KM)', min_value=0)
tax = st.number_input('Input Pajak Mobil', min_value=0)
mpg = st.number_input('Input Konsumsi Bahan Bakar (MPG)', min_value=0)
engineSize = st.number_input('Input Ukuran Mesin (CC)', min_value=0)
# membuat tombol untuk memprediksi harga mobil
if st.button('Prediksi Harga Mobil'):
    # memprediksi harga mobil berdasarkan fitur yang diinputkan
    prediction = model.predict([[year, mileage, tax, mpg, engineSize]])
    # menampilkan hasil prediksi
    st.write('Harga mobil bekas yang diprediksi adalah: Rp', prediction[0])
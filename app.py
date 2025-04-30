import streamlit as st

st.title("Simulasi Clinker Factor Konsolidasi")

plant_ubah = st.selectbox("Pilih Plant yang ingin diubah:", [1, 2, 3])
target = st.number_input("Masukkan target Clinker Factor:", min_value=0.0, max_value=1.0, value=0.75)

produksi_semen = [1000, 1500, 1200]
konsumsi_klinker_asli = [800, 1350, 1020]
konsumsi_klinker_baru = konsumsi_klinker_asli.copy()

klinker = 0
while klinker / produksi_semen[plant_ubah - 1] < target:
    klinker += 1
konsumsi_klinker_baru[plant_ubah - 1] = klinker

total_klinker = sum(konsumsi_klinker_baru)
total_semen = sum(produksi_semen)
cf_konsolidasi = total_klinker / total_semen

st.subheader("Hasil Simulasi:")
for i in range(3):
    st.write(f"Plant {i+1}: Semen = {produksi_semen[i]} ton, Klinker = {konsumsi_klinker_baru[i]} ton")

st.write(f"**Clinker Factor Konsolidasi = {cf_konsolidasi:.4f}**")

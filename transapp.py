import streamlit as st
import qrcode
from io import BytesIO

st.title('Data Gacor Rental')
st.write("Data Gacor Rental menyediakan sewa mobil dan truk termurah di Bandar Lampung dengan pelayanan yang memuaskan ")
st.write("**Mau rental mobil? DGR-in aja!!!**")

nama_pelanggan = st.text_input('Nama Pelanggan:')
tanggal_penyewaan = st.date_input('Tanggal Penyewaan:')
durasi_penyewaan = st.number_input('Durasi Penyewaan (hari):', min_value=1, value=1)
waktu_jemput = st.time_input('Waktu Penjemputan:')
jenis_mobil = st.selectbox('Jenis Mobil:', ['Biasa(Max 4 orang)', 'Besar(Max 7 orang)', 'Truk(Barang)'])
asuransi = st.checkbox('Tambahkan Asuransi')
driver = st.selectbox('Pilih dengan driver atau tidak :', ["Driver", "Tanpa Driver"])
lokasi = st.text_input('Tambahkan alamat lengkap penjemputan (bisa dengan link):')
metode_pembayaran = st.radio('Metode Pembayaran:', ['Tunai', 'Transfer Bank', 'QRIS'])

harga_mobil = {'Biasa(Max 4 orang)': 250000, 'Besar(Max 7 orang)': 350000, 'Truk(Barang)': 600000}
biaya_sewa = durasi_penyewaan * harga_mobil[jenis_mobil]
biaya_asuransi = 150000 if asuransi else 0
biaya_driver = 100000 * durasi_penyewaan if driver == 'Driver' else 0
total_biaya = biaya_sewa + biaya_asuransi + biaya_driver

def get_virtual_account():
    return "696966644"

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

if st.button('Submit'):
    st.success('Pemesanan Gacor!')
    st.markdown('**Detail Pemesanan:**')
    st.write(f'Nama Pelanggan: {nama_pelanggan}')
    st.write(f'Tanggal Penyewaan: {tanggal_penyewaan}')
    st.write(f'Waktu Penjemputan : {waktu_jemput.strftime("%H:%M")} WIB')
    st.write(f'Jenis Mobil: {jenis_mobil}')
    st.write(f'Durasi Penyewaan: {durasi_penyewaan} hari')
    st.write(f'Alamat Penjemputan: {lokasi}')
    st.write(f'Biaya Sewa: Rp.{biaya_sewa}')
    st.write(f'Biaya Asuransi: Rp.{biaya_asuransi}')
    st.write(f'Biaya Driver: Rp.{biaya_driver}')
    st.write(f'Total Biaya: Rp.{total_biaya}')
    st.write('***Informasi lebih lanjut hubungi: 083838446212***')

    if metode_pembayaran == 'Transfer Bank':
        virtual_account_number = get_virtual_account()
        st.write(f'Nomor Virtual Account: {virtual_account_number}')
    elif metode_pembayaran == 'QRIS':
        data_pemesanan = f'Nama: {nama_pelanggan}\nTanggal Penyewaan: {tanggal_penyewaan}\nWaktu Penjemputan:{waktu_jemput.strftime("%H:%M")}\nJenis Mobil: {jenis_mobil}\nDurasi Penyewaan: {durasi_penyewaan} hari\nAlamat Penjemputan: {lokasi}\nBiaya Sewa: Rp.{biaya_sewa}\nBiaya Asuransi: Rp.{biaya_asuransi}\nBiaya Driver: Rp.{biaya_driver}\nTotal Biaya: Rp.{total_biaya}'
        qr_image = generate_qr_code(data_pemesanan)
        buffered = BytesIO()
        qr_image.save(buffered, format="PNG")
        st.image(buffered, caption='QR Code Pemesanan', use_column_width=True)
## LaporanBug

Skrip ini digunakan untuk membuat laporan bug dengan berbagai jenis kerentanan keamanan.

### Instalasi

#### Persyaratan Sistem
- Sistem operasi Linux

#### Langkah-langkah Instalasi

1. **Perbarui dan Tingkatkan Paket Sistem:**
   ```bash
   $ sudo apt update && sudo apt upgrade
   ```

2. **Klon Repository:**
   ```bash
   $ git clone <repository_url>
   ```

3. **Masuk ke Direktori:**
   ```bash
   $ cd LapporanBug
   ```

4. **Instal Paket yang Diperlukan:**
   Beri izin eksekusi dan jalankan skrip instalasi:
   ```bash
   $ chmod +x install_packages.sh
   $ ./install_packages.sh
   ```

5. **Jalankan Skrip Utama:**
   Beri izin eksekusi dan jalankan skrip utama:
   ```bash
   $ chmod 777 lapporanbug.py
   $ python lapporanbug.py
   ```

### Penjelasan Skrip

Skrip ini digunakan untuk membuat laporan bug dengan berbagai jenis kerentanan keamanan.

#### Langkah-langkah yang Dilakukan oleh Skrip:

1. **Memilih Jenis Laporan Bug:**

   Skrip meminta pengguna untuk memilih jenis bug yang ingin dilaporkan.
<p align="center">
  <img src="https://github.com/Yoga913/CheeatSheet-BugBounty/blob/main/bonuty.jpg" alt="Deskripsi Gambar" width="300">
</p>
2. **Mengumpulkan Informasi:**

   Setelah memilih jenis bug, skrip akan meminta informasi berikut:
   - URL situs yang mengalami bug.
   - Nama pelapor.

3. **Menggunakan Template HTML:**

   Berdasarkan jenis bug yang dipilih, skrip akan menggunakan template HTML yang sesuai (misalnya rfi.html, rce.html, dll.) untuk menyusun laporan.

4. **Menambahkan Bukti Konsep (POC):**
   
   Pengguna diminta untuk memasukkan lokasi file yang berisi bukti konsep (Proof of Concept) dari bug tersebut. File ini bisa berupa PDF, gambar, atau video.

   Skrip akan melampirkan file ini pada email yang akan dikirimkan.

5. **Mengirim Email:**

   Skrip menyusun email dengan menggunakan informasi yang diberikan dan template HTML, kemudian melampirkan file bukti konsep. Email ini bisa dikirimkan ke alamat yang ditentukan oleh pengguna.

### Petunjuk Menjalankan Skrip

#### Kebutuhan Dependen:

Pastikan Anda memiliki pustaka yang diperlukan (smtplib, email, os, base64). Anda bisa menginstal pustaka yang hilang menggunakan pip.

#### Template HTML:

Pastikan file template HTML yang diperlukan (misalnya rfi.html, rce.html, csrf.html, xss.html) berada di direktori yang sama dengan skrip Anda atau sesuaikan jalur file dalam perintah open().

#### Menjalankan Skrip:

Jalankan skrip ini di terminal atau command prompt.

#### Izin:

Jika Anda menjalankan skrip ini di lingkungan terbatas (seperti perangkat mobile atau server yang aman), pastikan Anda memiliki izin yang diperlukan untuk mengirim email dan mengakses file.

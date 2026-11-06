# Portofolio Immantaka Juniarsa

Saya menyajikan profil, hasil analisis, keahlian dan kontak dalam satu halaman HTML dan CSS yang dilayani langsung oleh GitHub Pages.

![CI](https://github.com/imman20/imman20.github.io/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-green)

Saya menggunakan HTML dan CSS tanpa framework, build step, atau JavaScript. Semua angka pada kartu mengikuti README repo sumber, dengan URL di komentar HTML. Saya memakai gambar output nyata yang diunduh dari raw.githubusercontent.com, dikecilkan ke lebar maksimal 800 px, lalu disimpan lokal di assets/.

## Isi dan sumber

| Bagian | Sumber yang saya pakai |
|---|---|
| Profil, pendidikan, skripsi | [README profil](https://github.com/imman20/imman20/blob/main/README.md) |
| Kurs, 105 minggu dan MAPE SVR 0,509% | [README kurs](https://github.com/imman20/forecast-kurs-rupiah-arima-svr/blob/main/README.md) |
| Retail, net GBP18,93 juta | [README retail](https://github.com/imman20/analisis-penjualan-retail-sql-powerbi/blob/main/README.md) |
| Survei dan SPC, Cpk 1,071 | [README R](https://github.com/imman20/analisis-survei-dan-eksperimen-r/blob/main/README.md) |
| Excel, 15 modul, 47 workbook, 327.539 rumus | [README Excel](https://github.com/imman20/portofolio-excel-hr-administrasi/blob/main/README.md) |
| HR, 1.500 karyawan simulasi, AUC logistic 0,6915 | [README hr-attrition-analytics](https://github.com/imman20/hr-attrition-analytics/blob/main/README.md) |
| Situs ini | Saya menautkan repo sumber pada footer dan memakai 0 JavaScript |

Sumber gambar tersimpan di [tools/prepare_assets.py](tools/prepare_assets.py). Saya menggunakan gambar HR dari branch ulasan karena analisisnya belum digabungkan ke main. Setelah PR HR digabungkan, saya mengganti URL sumber HR dan tautan kartu ke main sebelum menghapus branch tersebut. Semua aset yang sudah tersimpan tetap dapat ditampilkan tanpa mengunduh ulang.

## Cara memperbarui isi

1. Saya membuka `index.html`, memperbarui teks dari README sumber dan menjaga URL sumber angka pada komentar HTML.
2. Saya mengganti data simulasi hanya dengan penanda yang jelas dan tidak menuliskan pengalaman kerja atau hasil intervensi yang tidak saya miliki.
3. Saya memperbarui sumber gambar di `tools/prepare_assets.py`, lalu menjalankan `make assets` bila gambar hasil berubah. Unduhan membutuhkan jaringan. Saya mencocokkan atribut width dan height HTML dengan ukuran berkas baru.
4. Saya menambahkan tautan demo hanya setelah aplikasi benar-benar tersedia. Saat ini situs tidak menampilkan tautan demo publik.
5. Saya menjaga isi publik, termasuk HTML, CSS dan assets, di bawah 2.000.000 byte. Dependensi Python hanya untuk pemeriksaan dan pemrosesan gambar, tidak diperlukan server produksi.

## Menjalankan dan memeriksa

Saya dapat membuka `index.html` langsung atau menjalankan server lokal dari root:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Untuk lint dan pemeriksaan otomatis:

```bash
python -m pip install -r requirements.txt
make all
```

Saya memeriksa struktur dokumen, tautan lokal dan anchor, ukuran serta dimensi gambar, metadata, keberadaan aturan responsif dan reduced motion, serta kontras teks dua tema minimal 4,5:1. CSS memakai layout satu kolom pada lebar ponsel, termasuk 360 px, serta grid pada desktop. Pemeriksaan otomatis ini tidak menggantikan tinjauan peramban, pembaca layar, atau Lighthouse; saya belum menjalankan pengujian visual peramban pada lingkungan ini.

## Mengaktifkan GitHub Pages

Setelah PR digabungkan, saya membuka **Settings > Pages > Source: Deploy from a branch > Branch: main > / (root) > Save**. Saya menunggu deployment selesai, lalu memeriksa `https://imman20.github.io/` dan menambahkan URL itu ke kolom Website repositori. URL tersebut belum saya klaim aktif sebelum deployment tersedia.

## Struktur

```text
index.html                 Konten dan sumber angka pada komentar
style.css                  Layout responsif serta tema terang/gelap
assets/                    Grafik hasil nyata dan ikon situs
tools/prepare_assets.py     Pengambilan dan kompresi gambar
tests/test_site.py          Pemeriksaan statis dan kontras
.github/workflows/ci.yml    Lint dan tes
```

## Lisensi dan kontak

Saya menyediakan kode serta dokumentasi dengan [MIT License](LICENSE). Gambar hasil berasal dari repo portofolio saya sendiri. Saya **Immantaka Juniarsa**, S1 Statistika Universitas Airlangga (2024), GitHub [@imman20](https://github.com/imman20), email immantakajuniarsa30@gmail.com.

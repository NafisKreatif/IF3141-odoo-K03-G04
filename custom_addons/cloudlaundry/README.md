# CloudLaundry

Addon Odoo 17 untuk model inti dan layar P5 CloudLaundry. Layar-layar memakai
model standar Odoo yang diperluas dengan field CloudLaundry.

## Instalasi

Aktifkan Docker Compose, lalu instal addon pada database Odoo:

```powershell
docker compose run --rm web odoo -d odoo_app -i cloudlaundry --stop-after-init
```

Jika addon sudah terpasang dan file berubah, gunakan `-u cloudlaundry` untuk
memperbarui. Menu **CloudLaundry** memuat daftar pesanan, nota, pengantaran,
penugasan, komplain, stok, pembelian, kehadiran, laporan, akun, data master,
dan impor.

## Batas demonstrasi

- L-03 adalah laporan PDF yang dapat dicetak dari pesanan.
- L-04 `/cloudlaundry/status-demo` adalah halaman publik statis tanpa data
  pesanan nyata atau data pribadi.
- L-05 menampilkan tagihan demonstrasi. Tidak terhubung ke payment gateway dan
  bukan QRIS yang bisa dipindai.
- L-14 memakai graph/pivot penjualan standar; KPI operasional tambahan belum
  dihitung.
- L-17 membuka daftar pelanggan dengan fitur impor bawaan Odoo; pemetaan,
  pratinjau dan validasi khusus per baris belum dibuat.
- Layar internal hanya terlihat oleh grup Odoo yang ditetapkan pada menu.
  Aturan keamanan per cabang dan pemetaan peran CloudLaundry masih perlu
  dikonfigurasi untuk pemakaian operasional.
# Simulasi Aplikasi POS (Point of Sales)
## Deskripsi Proyek
Proyek ini adalah implementasi sistem kasir sederhana yang dibangun menggunakan arsitektur **Multi-Component** dan pola desain **Dependency Injection (DI)**. Aplikasi ini memisahkan tanggung jawab antara Data (Repository), Logika Bisnis (Service), dan Kontrol UI (Orchestrator).

## Deskripsi Langkah-Langkah Praktikum
Repository ini berisi hasil pengerjaan **Langkah-Langkah Praktikum**.
Program ini adalah simulasi sederhana dari sistem kasir (POS) yang menggunakan arsitektur Multi-Component (Model, Repository, Service, Orchestrator).

## Struktur File
## 1. Lapisan Data Model (`models.py`)
Ini adalah lapisan paling dasar. File ini tidak memiliki logika bisnis, hanya berfungsi mendefinisikan "bentuk" data.
* **Penjelasan:** Saya menggunakan `@dataclass` untuk membuat objek `Product` dan `CartItem` agar kode lebih bersih dan hemat memori.

## 2. Lapisan Akses Data (`repositories.py`)
Komponen ini bertugas seolah-olah mengambil data dari Database.
* **Penjelasan:** `ProductRepository` menyembunyikan detail darimana data berasal. `main_app.py` tidak perlu tahu apakah data dari Array atau SQL, ia cukup memanggil `.get_all()`.

## 3. Lapisan Logika Bisnis (`services.py`)
Ini adalah "otak" dari aplikasi. Semua perhitungan dan aturan bisnis terjadi di sini.
* **CartService:** Mengurus logika keranjang (tambah barang, hitung subtotal, hapus barang).
* **PaymentService:** Pada Versi C ini, saya mengimplementasikan `CashPayment` yang mewarisi interface `IPaymentProcessor`. Ini memastikan sistem siap menerima metode bayar lain di masa depan (persiapan untuk OCP).

## 4. Lapisan Orchestrator (`main_app.py`)
Ini adalah pengatur lalu lintas data.
* **Penjelasan:** Kelas `PosApp` berfungsi menggabungkan (wiring) Repository, Service, dan Payment.
* **Dependency Injection:** Perhatikan bahwa `PosApp` tidak membuat objek `CashPayment` sendiri (tidak ada `new CashPayment()` di dalam kelas). Objek tersebut "disuntikkan" dari luar melalui constructor. Ini membuat aplikasi *Loosely Coupled* (tidak saling terikat keras).

## Deskripsi Proyek Tugas Mandiri
Proyek ini adalah penyelesaian **Tugas Mandiri**.
Aplikasi ini merupakan pengembangan dari sistem POS dasar yang kini dilengkapi dengan fitur interaktif (CLI) dan metode pembayaran digital, menerapkan prinsip **SOLID** (OCP & DIP).

## Penyelesaian Challenge

### 1. Integrasi CLI (Command Line Interface)
Saya telah melengkapi method `run()` pada `PosApp` dengan `while` loop. Pengguna kini dapat:
* Melihat katalog produk.
* Menambah barang ke keranjang secara interaktif (Input ID & Jumlah).
* Melakukan Checkout berkali-kali.

### 2. Implementasi OCP (Open/Closed Principle)
Saya menambahkan fitur pembayaran baru tanpa mengubah kode pembayaran lama (`CashPayment`).
* **File:** `services.py`
* **Implementasi:** Membuat class `DebitCardPayment` yang mewarisi `IPaymentProcessor`. Class ini mensimulasikan proses visual mesin EDC (Electronic Data Capture).

### 3. Implementasi DIP (Dependency Inversion Principle)
Saya mengubah cara injeksi dependensi pada `main_app.py` tanpa menyentuh logika inti `PosApp`.
* **Implementasi:** Mengganti objek `CashPayment()` menjadi `DebitCardPayment()` pada block `if __name__ == "__main__":`.
* **Hasil:** `PosApp` tidak perlu diedit sama sekali untuk menerima metode pembayaran baru.

## Struktur File
* `models.py`: Data Class untuk Produk dan Item Keranjang.
* `repositories.py`: Simulasi Database Produk.
* `services.py`: Berisi logika `CartService` dan class baru `DebitCardPayment`.
* `main_app.py`: Aplikasi utama dengan Loop CLI dan Wiring Dependency.

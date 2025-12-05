# Simulasi Aplikasi POS (Point of Sales)
## Deskripsi Proyek
Proyek ini adalah implementasi sistem kasir sederhana yang dibangun menggunakan arsitektur **Multi-Component** dan pola desain **Dependency Injection (DI)**. Aplikasi ini memisahkan tanggung jawab antara Data (Repository), Logika Bisnis (Service), dan Kontrol UI (Orchestrator).

## Deskripsi Langkah-Langkah Praktikum
Repository ini berisi hasil pengerjaan **Langkah-Langkah Praktikum**.
Program ini adalah simulasi sederhana dari sistem kasir (POS) yang menggunakan arsitektur Multi-Component (Model, Repository, Service, Orchestrator).

Pada versi ini, implementasi murni mengikuti panduan modul:
1.  Metode pembayaran hanya **Cash Payment**.
2.  Tidak ada interaksi CLI (Loop), program berjalan sekali jalan (Test Run).

## Struktur File
* `models.py`: Definisi data `Product` dan `CartItem`.
* `repositories.py`: Data dummy produk.
* `services.py`: Logika keranjang belanja dan implementasi `CashPayment`.
* `main_app.py`: Orchestrator utama untuk menjalankan tes transaksi tunai.

## Deskripsi Proyek Tugas Mandiri
Proyek ini adalah penyelesaian **Tugas Mandiri** dari Modul 13.
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

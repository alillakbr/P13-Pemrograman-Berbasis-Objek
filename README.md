# Simulasi Aplikasi POS (Point of Sales) - Modul 13
## Deskripsi Proyek
Proyek ini adalah implementasi sistem kasir sederhana yang dibangun menggunakan arsitektur **Multi-Component** dan pola desain **Dependency Injection (DI)**. Aplikasi ini memisahkan tanggung jawab antara Data (Repository), Logika Bisnis (Service), dan Kontrol UI (Orchestrator).

## Struktur Komponen
1.  **`models.py`**: Mendefinisikan struktur data `Product` dan `CartItem`.
2.  **`repositories.py`**: Bertindak sebagai *Data Layer* yang menyediakan data dummy produk.
3.  **`services.py`**:
    * `CartService`: Menangani logika penambahan item dan perhitungan total.
    * `IPaymentProcessor`: Interface kontrak pembayaran.
    * `DebitCardPayment` & `CashPayment`: Implementasi konkret metode bayar.
4.  **`main_app.py`**: Kelas `PosApp` yang berfungsi sebagai Orchestrator (pengatur) alur aplikasi.

## Penyelesaian Challenge (Poin D)

### 1. Implementasi OCP (Open/Closed Principle)
Saya menambahkan fitur pembayaran Debit Card tanpa mengubah kode `CashPayment` atau logika inti lainnya.
* **Lokasi:** `services.py`
* **Kode:** Class `DebitCardPayment(IPaymentProcessor)` ditambahkan untuk menangani simulasi koneksi EDC.

### 2. Implementasi DIP (Dependency Inversion Principle)
Pada `main_app.py`, `PosApp` tidak menginisialisasi metode pembayaran sendiri. Metode pembayaran "disuntikkan" dari luar.
* **Sebelum (Hardcoded di dalam class):** `self.payment = CashPayment()` (Salah).
* **Sesudah (Dependency Injection):** `app = PosApp(..., payment_method)` (Benar).

Saya mengubah inisialisasi di blok `if __name__ == "__main__":` menjadi:
```python
payment_method = DebitCardPayment() # Wiring Challenge
app = PosApp(repo, cart_svc, payment_method)

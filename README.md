# Project-Management-Restu-Mertua-Team

# AutoMind: AI Smart Car Simulation (PoC)

**AutoMind** adalah proyek pengembangan mobil pintar berbasis IoT dan *Artificial Intelligence*. Repositori ini berisi **Simulasi Proof of Concept (PoC)** untuk memvalidasi arsitektur komunikasi data nirkabel sebelum diimplementasikan ke perangkat keras fisik (ESP32).

Simulasi ini mendemonstrasikan bagaimana perintah kontrol (latency-sensitive) dikirim dari *Controller* (Laptop) menuju *Unit Kendaraan* melalui protokol **MQTT**.

---

## 📋 Fitur Simulasi
* **Dual-Client Architecture:** Terdiri dari dua program terpisah (Controller & Car Unit) yang berkomunikasi via internet.
* **Real-time IoT Communication:** Menggunakan protokol MQTT (Message Queuing Telemetry Transport) untuk pengiriman data yang ringan dan cepat.
* **Visual Feedback:** Visualisasi pergerakan mobil menggunakan library `pygame`.
* **Keyboard Control:** Kontrol arah menggunakan tombol panah keyboard (sebagai pengganti sementara input Computer Vision).

---

## 🛠️ Prasyarat (Requirements)

Pastikan Anda memiliki:
* **Python 3.x** (Disarankan Python 3.10 ke atas)
* Koneksi Internet (Wajib, untuk terhubung ke MQTT Broker publik)

### Library yang Digunakan
* `pygame`: Untuk antarmuka grafis simulasi.
* `paho-mqtt`: Untuk komunikasi IoT.

---

## 🚀 Cara Instalasi

1.  **Clone Repositori ini**
    ```bash
    git clone [https://github.com/rizalwahyu/AutoMind-Simulation.git](https://github.com/rizalwahyu/AutoMind-Simulation.git)
    cd AutoMind-Simulation
    ```

2.  **Buat Virtual Environment (Opsional tapi Disarankan)**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Jika file `requirements.txt` belum ada, install manual: `pip install pygame paho-mqtt`)*

---

## ▶️ Cara Menjalankan (PENTING)

Karena ini adalah simulasi sistem IoT, Anda harus menjalankan **DUA Terminal** secara bersamaan.

### Langkah 1: Jalankan Unit Mobil (Penerima)
Buka terminal pertama, lalu jalankan:
```bash
python mobil_simulasi.py

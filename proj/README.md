# Dinamic System Modelling: Suhu Ruangan dengan AC

**Nama:** Soni Moch Leviansyah  
**NIM:** 301240030  
**Mata kuliah:** Pemodelan Sistem Dinamik

Pemodelan dan simulasi suhu ruangan dengan AC menggunakan **SciPy (ODEINT)** dan **GEKKO**.

Model utama: `dT/dt = (T_out - T)/tau - k*u(t)`

| File | Isi |
|---|---|
| `src/program01_ac_odeint.py` | AC menyala jam 2-7 (ODEINT) |
| `src/program02_termostat_odeint.py` | AC dengan termostat 24-26 C |
| `src/program03..06` | Contoh 1 dan 2 (ODEINT dan GEKKO) |
| `src/program07..08` | Contoh 3, input step AC |
| `src/program09..10` | Contoh 4, dua persamaan ekivalen |
| `src/program11..12` | Contoh 5, model 2 state udara-dinding |
| `src/program13_studikasus_setpoint.py` | Studi kasus setpoint termostat dan energi AC |
| `src/program14..15` | Contoh Pemodelan (GEKKO dan variasi k) |
| `src/hitung_manual_euler.py` | Tabel hitung manual Euler |
| `notebook/Pemodelan_AC_Soni_301240030.ipynb` | Notebook Google Colab |
| `run_all.py` | Menjalankan semua program dan menyimpan grafik ke `figures/` |

## Cara menjalankan
```bash
pip install -r requirements.txt
python run_all.py          # jalankan dari folder utama repo
```
Atau buka notebook di Google Colab (Upload notebook, lalu Runtime > Run all).

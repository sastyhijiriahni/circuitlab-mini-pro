# =========================================================
# Copyright (c) 2026 Sasty Hijiriahni. All Rights Reserved.
# Developed independently for commercial digital product.
# Product: CircuitLab Mini Pro (Web Simulation & Calculator)
# =========================================================

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="CircuitLab Mini Pro",
    page_icon="⚡",
    layout="wide"
)

# Header Utama
st.title("⚡ CircuitLab Mini Pro")
st.markdown("### Alat Bantu Hitung & Analisis Rangkaian Listrik Interaktif")
st.markdown("---")

# Menu Navigasi Sidebar
menu = st.sidebar.selectbox(
    "Pilih Menu Kalkulator:",
    [
        "1. Hukum Ohm (V-I-R)",
        "2. Rangkaian Seri & Paralel Resistor",
        "3. Daya & Energi Listrik",
        "4. Simulasi Gelombang AC Sederhana"
    ]
)

# =========================================================
# MENU 1: HUKUM OHM
# =========================================================
if menu == "1. Hukum Ohm (V-I-R)":
    st.header("🔌 Kalkulator Hukum Ohm")
    st.write("Menghitung hubungan antara Tegangan (V), Arus (I), dan Hambatan (R). Rumus: $V = I \\times R$")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pilihan_cari = st.radio("Apa yang ingin dicari?", ["Tegangan (V)", "Kuat Arus (I)", "Hambatan (R)"])
        
    with col2:
        if pilihan_cari == "Tegangan (V)":
            arus = st.number_input("Masukkan Kuat Arus (Ampere / A):", min_value=0.0, value=2.0, step=0.1)
            hambatan = st.number_input("Masukkan Hambatan (Ohm / $\\Omega$):", min_value=0.0, value=10.0, step=0.5)
            if st.button("Hitung Tegangan"):
                tegangan = arus * hambatan
                st.success(f"Hasil Tegangan ($V$) = **{tegangan:.2f} Volt**")
                
        elif pilihan_cari == "Kuat Arus (I)":
            tegangan = st.number_input("Masukkan Tegangan (Volt / V):", min_value=0.0, value=12.0, step=0.5)
            hambatan = st.number_input("Masukkan Hambatan (Ohm / $\\Omega$):", min_value=0.0, value=4.0, step=0.5)
            if hambatan > 0:
                if st.button("Hitung Arus"):
                    arus = tegangan / hambatan
                    st.success(f"Hasil Kuat Arus ($I$) = **{arus:.2f} Ampere**")
            else:
                st.error("Hambatan tidak boleh 0!")
                
        elif pilihan_cari == "Hambatan (R)":
            tegangan = st.number_input("Masukkan Tegangan (Volt / V):", min_value=0.0, value=24.0, step=0.5)
            arus = st.number_input("Masukkan Kuat Arus (Ampere / A):", min_value=0.0, value=3.0, step=0.1)
            if arus > 0:
                if st.button("Hitung Hambatan"):
                    hambatan = tegangan / arus
                    st.success(f"Hasil Hambatan ($R$) = **{hambatan:.2f} Ohm ($\\Omega$)**")
            else:
                st.error("Arus tidak boleh 0!")

# =========================================================
# MENU 2: RANGKAIAN SERI & PARALEL + DIAGRAM VISUAL
# =========================================================
elif menu == "2. Rangkaian Seri & Paralel Resistor":
    st.header("🔗 Kalkulator & Diagram Resistor Seri & Paralel")
    
    col_input, col_view = st.columns([1, 1])
    
    with col_input:
        tipe_rangkaian = st.selectbox("Pilih Jenis Rangkaian:", ["Seri", "Paralel"])
        st.write("Masukkan nilai resistor (pisahkan dengan koma, contoh: `10, 20, 30`)")
        input_nilai = st.text_input("Nilai Resistor (Ohm):", "10, 20, 30")
        
    try:
        resistor_list = [float(x.strip()) for x in input_nilai.split(",") if x.strip()]
        
        if resistor_list:
            if tipe_rangkaian == "Seri":
                r_total = sum(resistor_list)
                with col_input:
                    st.info(f"Rumus Seri: $R_{{total}} = R_1 + R_2 + R_3 + ...$")
                    st.success(f"Total Hambatan Seri ($R_{{tot}}$) = **{r_total:.2f} Ohm**")
                
                # Menggambar Diagram Rangkaian Seri
                fig, ax = plt.subplots(figsize=(6, 2.5))
                ax.set_title("Diagram Rangkaian Resistor Seri", fontsize=10, fontweight='bold')
                x_pos = 0
                ax.plot([x_pos, x_pos + 0.5], [0, 0], color='black', lw=2)
                x_pos += 0.5
                
                for idx, r in enumerate(resistor_list):
                    # Gambar kotak resistor
                    rect = plt.Rectangle((x_pos, -0.2), 0.8, 0.4, facecolor='#4CAF50', edgecolor='black', lw=1.5)
                    ax.add_patch(rect)
                    ax.text(x_pos + 0.4, 0.3, f"R{idx+1}\n{r} Ω", ha='center', va='bottom', fontsize=8, fontweight='bold')
                    x_pos += 0.8
                    # Garis penghubung
                    ax.plot([x_pos, x_pos + 0.5], [0, 0], color='black', lw=2)
                    x_pos += 0.5
                    
                ax.set_xlim(-0.2, x_pos + 0.2)
                ax.set_ylim(-0.8, 0.8)
                ax.axis('off')
                
                with col_view:
                    st.pyplot(fig)
                
            elif tipe_rangkaian == "Paralel":
                inv_sum = sum(1.0 / r for r in resistor_list if r > 0)
                if inv_sum > 0:
                    r_total = 1.0 / inv_sum
                    with col_input:
                        st.info(f"Rumus Paralel: $1 / R_{{total}} = (1/R_1) + (1/R_2) + ...$")
                        st.success(f"Total Hambatan Paralel ($R_{{tot}}$) = **{r_total:.2f} Ohm**")
                    
                    # Menggambar Diagram Rangkaian Paralel
                    num_r = len(resistor_list)
                    fig, ax = plt.subplots(figsize=(6, max(2.5, num_r * 0.8)))
                    ax.set_title("Diagram Rangkaian Resistor Paralel", fontsize=10, fontweight='bold')
                    
                    y_positions = np.linspace(num_r - 1, 0, num_r)
                    # Garis Rel Kiri & Kanan
                    ax.plot([0, 0], [y_positions[0], y_positions[-1]], color='black', lw=2)
                    ax.plot([2, 2], [y_positions[0], y_positions[-1]], color='black', lw=2)
                    
                    # Garis Masuk & Keluar Utama
                    ax.plot([-0.4, 0], [(y_positions[0] + y_positions[-1])/2, (y_positions[0] + y_positions[-1])/2], color='black', lw=2)
                    ax.plot([2, 2.4], [(y_positions[0] + y_positions[-1])/2, (y_positions[0] + y_positions[-1])/2], color='black', lw=2)
                    
                    for idx, (r, y) in enumerate(zip(resistor_list, y_positions)):
                        ax.plot([0, 0.6], [y, y], color='black', lw=1.5)
                        rect = plt.Rectangle((0.6, y - 0.15), 0.8, 0.3, facecolor='#2196F3', edgecolor='black', lw=1.5)
                        ax.add_patch(rect)
                        ax.text(1.0, y + 0.2, f"R{idx+1} = {r} Ω", ha='center', va='bottom', fontsize=8, fontweight='bold')
                        ax.plot([1.4, 2], [y, y], color='black', lw=1.5)
                        
                    ax.set_xlim(-0.6, 2.6)
                    ax.set_ylim(-0.5, num_r)
                    ax.axis('off')
                    
                    with col_view:
                        st.pyplot(fig)
                else:
                    st.error("Nilai resistor tidak boleh 0!")
        else:
            st.warning("Silakan masukkan minimal satu nilai resistor yang valid.")
    except ValueError:
        st.error("Format input salah! Gunakan angka dan pisahkan dengan koma (contoh: 10, 20, 30).")

# =========================================================
# MENU 3: DAYA & ENERGI LISTRIK
# =========================================================
elif menu == "3. Daya & Energi Listrik":
    st.header("💡 Kalkulator Daya Listrik")
    st.write("Menghitung besar daya listrik ($P$) menggunakan rumus $P = V \\times I$ atau $P = I^2 \\times R$.")
    
    pilihan_daya = st.radio("Metode Hitung Daya:", ["Berdasarkan V dan I", "Berdasarkan I dan R"])
    
    if pilihan_daya == "Berdasarkan V dan I":
        v_val = st.number_input("Tegangan (Volt):", min_value=0.0, value=220.0)
        i_val = st.number_input("Arus (Ampere):", min_value=0.0, value=2.0)
        if st.button("Hitung Daya"):
            p_val = v_val * i_val
            st.success(f"Daya Listrik ($P$) = **{p_val:.2f} Watt**")
            
    else:
        i_val = st.number_input("Arus (Ampere):", min_value=0.0, value=2.0)
        r_val = st.number_input("Hambatan (Ohm):", min_value=0.0, value=50.0)
        if st.button("Hitung Daya"):
            p_val = (i_val ** 2) * r_val
            st.success(f"Daya Listrik ($P$) = **{p_val:.2f} Watt**")

# =========================================================
# MENU 4: SIMULASI GELOMBANG AC
# =========================================================
elif menu == "4. Simulasi Gelombang AC Sederhana":
    st.header("📈 Visualisasi Gelombang Arus Bolak-Balik (AC)")
    st.write("Menampilkan grafik tegangan sinusoidal terhadap waktu $v(t) = V_{max} \\sin(2\\pi f t)$.")
    
    v_max = st.slider("Tegangan Maksimum ($V_{max}$ - Volt):", min_value=10, max_value=380, value=220)
    frekuensi = st.slider("Frekuensi ($f$ - Hz):", min_value=1, max_value=100, value=50)
    
    t = np.linspace(0, 0.05, 500)
    v_t = v_max * np.sin(2 * np.pi * frekuensi * t)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t * 1000, v_t, color='blue', linewidth=2, label=f'V(t) = {v_max} sin(2π {frekuensi} t)')
    ax.set_title("Grafik Tegangan Sinusoidal AC", fontsize=12, fontweight='bold')
    ax.set_xlabel("Waktu (milidetik / ms)")
    ax.set_ylabel("Tegangan (Volt)")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    
    st.pyplot(fig)

# Footer Informasi Hak Cipta di Web
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Sasty Hijiriahni. All Rights Reserved. Independent Commercial Application.</p>", unsafe_allow_html=True)
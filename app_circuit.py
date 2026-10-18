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

# =========================================================
# PILIHAN BAHASA (LANGUAGE SELECTION)
# =========================================================
lang = st.sidebar.selectbox("🌐 Choose Language / Pilih Bahasa:", ["Bahasa Indonesia", "English"])

# Kamus Teks 2 Bahasa
text = {
    "Bahasa Indonesia": {
        "title": "⚡ CircuitLab Mini Pro",
        "subtitle": "Alat Bantu Hitung & Analisis Rangkaian Listrik Interaktif",
        "menu_label": "Pilih Menu Kalkulator:",
        "menu_options": [
            "1. Hukum Ohm (V-I-R)",
            "2. Rangkaian Seri & Paralel Resistor",
            "3. Daya & Energi Listrik",
            "4. Simulasi Gelombang AC Sederhana"
        ],
        "ohm_header": "🔌 Kalkulator Hukum Ohm",
        "ohm_desc": "Menghitung hubungan antara Tegangan (V), Arus (I), dan Hambatan (R). Rumus: $V = I \\times R$",
        "ohm_cari": "Apa yang ingin dicari?",
        "ohm_opt": ["Tegangan (V)", "Kuat Arus (I)", "Hambatan (R)"],
        "res_header": "🔗 Kalkulator & Diagram Resistor Seri & Paralel",
        "res_type": "Pilih Jenis Rangkaian:",
        "res_types": ["Seri", "Paralel"],
        "res_input_label": "Nilai Resistor (Ohm):",
        "res_input_tip": "Masukkan nilai resistor (pisahkan dengan koma, contoh: 10, 20, 30)",
        "power_header": "💡 Kalkulator Daya Listrik",
        "power_desc": "Menghitung besar daya listrik ($P$) menggunakan rumus $P = V \\times I$ atau $P = I^2 \\times R$.",
        "power_method": "Metode Hitung Daya:",
        "power_opts": ["Berdasarkan V dan I", "Berdasarkan I dan R"],
        "ac_header": "📈 Visualisasi Gelombang Arus Bolak-Balik (AC)",
        "ac_desc": "Menampilkan grafik tegangan sinusoidal terhadap waktu $v(t) = V_{max} \\sin(2\\pi f t)$.",
        "ac_vmax": "Tegangan Maksimum ($V_{max}$ - Volt):",
        "ac_freq": "Frekuensi ($f$ - Hz):"
    },
    "English": {
        "title": "⚡ CircuitLab Mini Pro",
        "subtitle": "Interactive Electrical Circuit & Physics Simulator",
        "menu_label": "Select Calculator Menu:",
        "menu_options": [
            "1. Ohm's Law (V-I-R)",
            "2. Series & Parallel Resistors",
            "3. Electrical Power & Energy",
            "4. AC Waveform Simulation"
        ],
        "ohm_header": "🔌 Ohm's Law Calculator",
        "ohm_desc": "Calculate Voltage (V), Current (I), and Resistance (R). Formula: $V = I \\times R$",
        "ohm_cari": "What do you want to calculate?",
        "ohm_opt": ["Voltage (V)", "Current (I)", "Resistance (R)"],
        "res_header": "🔗 Series & Parallel Resistor Calculator & Diagram",
        "res_type": "Select Circuit Type:",
        "res_types": ["Series", "Parallel"],
        "res_input_label": "Resistor Values (Ohm):",
        "res_input_tip": "Enter resistor values separated by commas (e.g., 10, 20, 30)",
        "power_header": "💡 Electrical Power Calculator",
        "power_desc": "Calculate electrical power ($P$) using formula $P = V \\times I$ or $P = I^2 \\times R$.",
        "power_method": "Power Calculation Method:",
        "power_opts": ["Based on V and I", "Based on I and R"],
        "ac_header": "📈 AC Waveform Visualization",
        "ac_desc": "Display sinusoidal voltage graph over time $v(t) = V_{max} \\sin(2\\pi f t)$.",
        "ac_vmax": "Maximum Voltage ($V_{max}$ - Volts):",
        "ac_freq": "Frequency ($f$ - Hz):"
    }
}

t = text[lang]

# Header Utama
st.title(t["title"])
st.markdown(f"### {t['subtitle']}")
st.markdown("---")

# Menu Navigasi Sidebar
menu = st.sidebar.selectbox(t["menu_label"], t["menu_options"])

# =========================================================
# MENU 1: HUKUM OHM
# =========================================================
if menu == t["menu_options"][0]:
    st.header(t["ohm_header"])
    st.write(t["ohm_desc"])
    
    col1, col2 = st.columns(2)
    with col1:
        pilihan_cari = st.radio(t["ohm_cari"], t["ohm_opt"])
    with col2:
        if pilihan_cari == t["ohm_opt"][0]:
            arus = st.number_input("Kuat Arus / Current (A):", min_value=0.0, value=2.0, step=0.1)
            hambatan = st.number_input("Hambatan / Resistance (Ω):", min_value=0.0, value=10.0, step=0.5)
            if st.button("Hitung / Calculate"):
                tegangan = arus * hambatan
                st.success(f"Tegangan / Voltage ($V$) = **{tegangan:.2f} V**")
                
        elif pilihan_cari == t["ohm_opt"][1]:
            tegangan = st.number_input("Tegangan / Voltage (V):", min_value=0.0, value=12.0, step=0.5)
            hambatan = st.number_input("Hambatan / Resistance (Ω):", min_value=0.0, value=4.0, step=0.5)
            if hambatan > 0:
                if st.button("Hitung / Calculate"):
                    arus = tegangan / hambatan
                    st.success(f"Kuat Arus / Current ($I$) = **{arus:.2f} A**")
            else:
                st.error("Resistance cannot be 0! / Hambatan tidak boleh 0!")
                
        elif pilihan_cari == t["ohm_opt"][2]:
            tegangan = st.number_input("Tegangan / Voltage (V):", min_value=0.0, value=24.0, step=0.5)
            arus = st.number_input("Kuat Arus / Current (A):", min_value=0.0, value=3.0, step=0.1)
            if arus > 0:
                if st.button("Hitung / Calculate"):
                    hambatan = tegangan / arus
                    st.success(f"Hambatan / Resistance ($R$) = **{hambatan:.2f} Ω**")
            else:
                st.error("Current cannot be 0! / Arus tidak boleh 0!")

# =========================================================
# MENU 2: RANGKAIAN SERI & PARALEL + DIAGRAM VISUAL
# =========================================================
elif menu == t["menu_options"][1]:
    st.header(t["res_header"])
    
    col_input, col_view = st.columns([1, 1])
    
    with col_input:
        tipe_rangkaian = st.selectbox(t["res_type"], t["res_types"])
        st.write(t["res_input_tip"])
        input_nilai = st.text_input(t["res_input_label"], "10, 20, 30")
        
    try:
        resistor_list = [float(x.strip()) for x in input_nilai.split(",") if x.strip()]
        
        if resistor_list:
            is_series = (tipe_rangkaian == "Seri" or tipe_rangkaian == "Series")
            if is_series:
                r_total = sum(resistor_list)
                with col_input:
                    st.success(f"Total Resistance ($R_{{tot}}$) = **{r_total:.2f} Ω**")
                
                fig, ax = plt.subplots(figsize=(6, 2.5))
                ax.set_title("Series Resistor Diagram", fontsize=10, fontweight='bold')
                x_pos = 0
                ax.plot([x_pos, x_pos + 0.5], [0, 0], color='black', lw=2)
                x_pos += 0.5
                
                for idx, r in enumerate(resistor_list):
                    rect = plt.Rectangle((x_pos, -0.2), 0.8, 0.4, facecolor='#4CAF50', edgecolor='black', lw=1.5)
                    ax.add_patch(rect)
                    ax.text(x_pos + 0.4, 0.3, f"R{idx+1}\n{r} Ω", ha='center', va='bottom', fontsize=8, fontweight='bold')
                    x_pos += 0.8
                    ax.plot([x_pos, x_pos + 0.5], [0, 0], color='black', lw=2)
                    x_pos += 0.5
                    
                ax.set_xlim(-0.2, x_pos + 0.2)
                ax.set_ylim(-0.8, 0.8)
                ax.axis('off')
                
                with col_view:
                    st.pyplot(fig)
                
            else:
                inv_sum = sum(1.0 / r for r in resistor_list if r > 0)
                if inv_sum > 0:
                    r_total = 1.0 / inv_sum
                    with col_input:
                        st.success(f"Total Resistance ($R_{{tot}}$) = **{r_total:.2f} Ω**")
                    
                    num_r = len(resistor_list)
                    fig, ax = plt.subplots(figsize=(6, max(2.5, num_r * 0.8)))
                    ax.set_title("Parallel Resistor Diagram", fontsize=10, fontweight='bold')
                    
                    y_positions = np.linspace(num_r - 1, 0, num_r)
                    ax.plot([0, 0], [y_positions[0], y_positions[-1]], color='black', lw=2)
                    ax.plot([2, 2], [y_positions[0], y_positions[-1]], color='black', lw=2)
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
                    st.error("Resistor values cannot be 0!")
        else:
            st.warning("Please enter valid resistor values.")
    except ValueError:
        st.error("Invalid input format! Use numbers separated by commas (e.g., 10, 20, 30).")

# =========================================================
# MENU 3: DAYA & ENERGI LISTRIK
# =========================================================
elif menu == t["menu_options"][2]:
    st.header(t["power_header"])
    st.write(t["power_desc"])
    
    pilihan_daya = st.radio(t["power_method"], t["power_opts"])
    
    if pilihan_daya == t["power_opts"][0]:
        v_val = st.number_input("Voltage (V):", min_value=0.0, value=220.0)
        i_val = st.number_input("Current (A):", min_value=0.0, value=2.0)
        if st.button("Calculate Power"):
            p_val = v_val * i_val
            st.success(f"Power ($P$) = **{p_val:.2f} Watts**")
            
    else:
        i_val = st.number_input("Current (A):", min_value=0.0, value=2.0)
        r_val = st.number_input("Resistance (Ω):", min_value=0.0, value=50.0)
        if st.button("Calculate Power"):
            p_val = (i_val ** 2) * r_val
            st.success(f"Power ($P$) = **{p_val:.2f} Watts**")

# =========================================================
# MENU 4: SIMULASI GELOMBANG AC
# =========================================================
elif menu == t["menu_options"][3]:
    st.header(t["ac_header"])
    st.write(t["ac_desc"])
    
    v_max = st.slider(t["ac_vmax"], min_value=10, max_value=380, value=220)
    frekuensi = st.slider(t["ac_freq"], min_value=1, max_value=100, value=50)
    
    t_axis = np.linspace(0, 0.05, 500)
    v_t = v_max * np.sin(2 * np.pi * frekuensi * t_axis)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t_axis * 1000, v_t, color='blue', linewidth=2, label=f'V(t) = {v_max} sin(2π {frekuensi} t)')
    ax.set_title("AC Sinusoidal Voltage Graph", fontsize=12, fontweight='bold')
    ax.set_xlabel("Time (milliseconds / ms)")
    ax.set_ylabel("Voltage (V)")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    
    st.pyplot(fig)

# Footer Informasi Hak Cipta
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Sasty Hijiriahni. All Rights Reserved. Independent Commercial Application.</p>", unsafe_allow_html=True)

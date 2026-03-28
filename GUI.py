import tkinter as tk
from tkinter import ttk

def main():
    # 1. Tworzenie głównego okna
    root = tk.Tk()
    root.columnconfigure(1, weight=1) # Kolumna 1 (wykres) rośnie
    root.rowconfigure(0, weight=1)
    root.title("Analizator Sygnałów PID")
    root.geometry("1000x500")

    # Przykład LabelFrame - etykietowany kontener
    sidebar = tk.Frame(root)
    sidebar.grid(row=0, column=0, sticky="ns", padx=15, pady=10)
    
    # Sekcja Sygnału
    signal_frame = tk.LabelFrame(sidebar, text="Typ Sygnału", padx=10, pady=10)
    signal_frame.grid(row=2, column=0, sticky="ew", pady=5)

    def show_signal_params(signal_type):
        for widget in signal_frame.winfo_children():
            widget.destroy()

        signal_frame.config(text=f"Parametry: {signal_type}")
        signal_frame.entries = {}

        if signal_type == "Harmoniczny":
            tk.Label(signal_frame, text="Phi (stopnie):").grid(row=0, column=0)
            phi_entry = tk.Entry(signal_frame, width=10)
            phi_entry.grid(row=0, column=1)
            signal_frame.entries["phi"] = phi_entry

            tk.Label(signal_frame, text="Amplituda:").grid(row=1, column=0)
            amp_entry = tk.Entry(signal_frame, width=10)
            amp_entry.grid(row=1, column=1)
            signal_frame.entries["amp"] = amp_entry

            tk.Label(signal_frame, text="Omega (rad/s):").grid(row=2, column=0)
            freq_entry = tk.Entry(signal_frame, width=10)
            omega_entry = tk.Entry(signal_frame, width=10)
            omega_entry.grid(row=2, column=1)
            signal_frame.entries["omega"] = omega_entry

        elif signal_type == "Prostokąt":
            tk.Label(signal_frame, text="Wypełnienie (0-100)%:").grid(row=0, column=0)
            duty_entry = tk.Entry(signal_frame, width=10)
            duty_entry.grid(row=0, column=1)
            signal_frame.entries["duty"] = duty_entry

            tk.Label(signal_frame, text="Amplituda:").grid(row=1, column=0)
            amp_entry = tk.Entry(signal_frame, width=10)
            amp_entry.grid(row=1, column=1)
            signal_frame.entries["amp"] = amp_entry

            tk.Label(signal_frame, text="Częstotliwość (Hz):").grid(row=2, column=0)
            freq_entry = tk.Entry(signal_frame, width=10)
            freq_entry.grid(row=2, column=1)
            signal_frame.entries["freq"] = freq_entry

        elif signal_type == "Piłokształtny":
            tk.Label(signal_frame, text="Szerokość (0-1):").grid(row=0, column=0)
            width_entry = tk.Entry(signal_frame, width=10)
            width_entry.grid(row=0, column=1)
            signal_frame.entries["width"] = width_entry

            tk.Label(signal_frame, text="Amplituda:").grid(row=1, column=0)
            amp_entry = tk.Entry(signal_frame, width=10)
            amp_entry.grid(row=1, column=1)
            signal_frame.entries["amp"] = amp_entry

            tk.Label(signal_frame, text="Częstotliwość (Hz):").grid(row=2, column=0)
            freq_entry = tk.Entry(signal_frame, width=10)
            freq_entry.grid(row=2, column=1)
            signal_frame.entries["freq"] = freq_entry

        # Przycisk powrotu, żeby móc zmienić typ sygnału
        tk.Button(signal_frame, text="Zmień typ", command=setup_initial_buttons).grid(row=3, column=0, columnspan=2, pady=5)

    def setup_initial_buttons():
        for widget in signal_frame.winfo_children():
            widget.destroy()
        signal_frame.config(text="Wybierz Typ Sygnału")
        
        tk.Button(signal_frame, text="Harmoniczny", command=lambda: show_signal_params("Harmoniczny")).pack(fill="x", pady=2)
        tk.Button(signal_frame, text="Prostokąt", command=lambda: show_signal_params("Prostokąt")).pack(fill="x", pady=2)
        tk.Button(signal_frame, text="Piłokształtny", command=lambda: show_signal_params("Piłokształtny")).pack(fill="x", pady=2)

    # Uruchamiamy widok początkowy przycisków
    setup_initial_buttons()



    #Parametry Obiektu
    object_frame = tk.LabelFrame(sidebar, text="Parametry Obiektu", padx=10, pady=10)
    object_frame.grid(row=1, column=0, sticky="ew", pady=5)

    # Etykieta i pole dla a1
    tk.Label(object_frame, text="a1:").grid(row=1, column=0, sticky="w")
    a1_entry = tk.Entry(object_frame, width=10)
    a1_entry.grid(row=1, column=1, padx=5, pady=2)

    # Dodajemy etykietę i pole dla a0
    tk.Label(object_frame, text="a0:").grid(row=0, column=0, sticky="w")
    a0_entry = tk.Entry(object_frame, width=10)
    a0_entry.grid(row=0, column=1, padx=5, pady=2)

    # Dodajemy etykietę i pole dla b2
    tk.Label(object_frame, text="b2:").grid(row=2, column=2, sticky="w")
    b2_entry = tk.Entry(object_frame, width=10)
    b2_entry.grid(row=2, column=3, padx=5, pady=2)

    # Dodajemy etykietę i pole dla b1
    tk.Label(object_frame, text="b1:").grid(row=1, column=2, sticky="w")
    b1_entry = tk.Entry(object_frame, width=10)
    b1_entry.grid(row=1, column=3, padx=5, pady=2)

    # Dodajemy etykietę i pole dla b0
    tk.Label(object_frame, text="b0:").grid(row=0, column=2, sticky="w")
    b0_entry = tk.Entry(object_frame, width=10)
    b0_entry.grid(row=0, column=3, padx=5, pady=2)




    #Parametry PID
    pid_frame = tk.LabelFrame(sidebar, text="Regulator PID", padx=10, pady=10)
    pid_frame.grid(row=0, column=0, sticky="ew", pady=5)

    #Etykieta i pole dla Kp
    tk.Label(pid_frame, text="Kp:").grid(row=0, column=0, sticky="w")
    kp_entry = tk.Entry(pid_frame, width=10) # RODZICEM JEST pid_frame!
    kp_entry.grid(row=0, column=1, padx=5, pady=2)

    # Dodajemy etykietę i pole dla Ti
    tk.Label(pid_frame, text="Ti:").grid(row=1, column=0, sticky="w")
    ti_entry = tk.Entry(pid_frame, width=10)
    ti_entry.grid(row=1, column=1, padx=5, pady=2)

    # Dodajemy etykietę i pole dla Td
    tk.Label(pid_frame, text="Td:").grid(row=2, column=0, sticky="w")
    td_entry = tk.Entry(pid_frame, width=10)
    td_entry.grid(row=2, column=1, padx=5, pady=2)

    def calc_params():
        kp = kp_entry.get() or "0"
        ti = ti_entry.get() or "0"
        td = td_entry.get() or "0"

        a0 = a0_entry.get() or "0"
        a1 = a1_entry.get() or "0"
        b0 = b0_entry.get() or "0"
        b1 = b1_entry.get() or "0"
        b2 = b2_entry.get() or "0"
        return kp, ti, td, a0, a1, b0, b1, b2

    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    # --- 1. TWORZENIE GŁÓWNEGO OKNA ---
    root = tk.Tk()
    root.columnconfigure(1, weight=1) # Kolumna 1 (wykres) rośnie
    root.rowconfigure(0, weight=1)
    root.title("Analizator Sygnałów PID")
    root.geometry("1100x650")

    # Pasek boczny
    sidebar = tk.Frame(root)
    sidebar.grid(row=0, column=0, sticky="ns", padx=15, pady=10)

    fig, ax = plt.subplots(figsize=(7, 5))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # --- 3. PARAMETRY REGULATORA PID ---
    pid_frame = tk.LabelFrame(sidebar, text="Regulator PID", padx=10, pady=10)
    pid_frame.grid(row=0, column=0, sticky="ew", pady=5)

    tk.Label(pid_frame, text="Kp:").grid(row=0, column=0, sticky="w")
    kp_entry = tk.Entry(pid_frame, width=10)
    kp_entry.insert(0, "2.0")
    kp_entry.grid(row=0, column=1, padx=5, pady=2)

    tk.Label(pid_frame, text="Ti:").grid(row=1, column=0, sticky="w")
    ti_entry = tk.Entry(pid_frame, width=10)
    ti_entry.insert(0, "1.0")
    ti_entry.grid(row=1, column=1, padx=5, pady=2)

    tk.Label(pid_frame, text="Td:").grid(row=2, column=0, sticky="w")
    td_entry = tk.Entry(pid_frame, width=10)
    td_entry.insert(0, "0.5")
    td_entry.grid(row=2, column=1, padx=5, pady=2)

    # --- 4. PARAMETRY OBIEKTU ---
    object_frame = tk.LabelFrame(sidebar, text="Parametry Obiektu", padx=10, pady=10)
    object_frame.grid(row=1, column=0, sticky="ew", pady=5)

    tk.Label(object_frame, text="a1:").grid(row=1, column=0, sticky="w")
    a1_entry = tk.Entry(object_frame, width=8)
    a1_entry.insert(0, "1.0")
    a1_entry.grid(row=1, column=1, padx=2, pady=2)

    tk.Label(object_frame, text="a0:").grid(row=0, column=0, sticky="w")
    a0_entry = tk.Entry(object_frame, width=8)
    a0_entry.insert(0, "2.0")
    a0_entry.grid(row=0, column=1, padx=2, pady=2)

    tk.Label(object_frame, text="b2:").grid(row=2, column=2, sticky="w")
    b2_entry = tk.Entry(object_frame, width=8)
    b2_entry.insert(0, "1.0")
    b2_entry.grid(row=2, column=3, padx=2, pady=2)

    tk.Label(object_frame, text="b1:").grid(row=1, column=2, sticky="w")
    b1_entry = tk.Entry(object_frame, width=8)
    b1_entry.insert(0, "3.0")
    b1_entry.grid(row=1, column=3, padx=2, pady=2)

    tk.Label(object_frame, text="b0:").grid(row=0, column=2, sticky="w")
    b0_entry = tk.Entry(object_frame, width=8)
    b0_entry.insert(0, "2.0")
    b0_entry.grid(row=0, column=3, padx=2, pady=2)

    # --- 5. WYBÓR SYGNAŁU ---
    signal_frame = tk.LabelFrame(sidebar, text="Typ Sygnału", padx=10, pady=10)
    signal_frame.grid(row=2, column=0, sticky="ew", pady=5)
    
    current_signal_type = tk.StringVar(value="")

    def show_signal_params(signal_type):
        for widget in signal_frame.winfo_children():
            widget.destroy()

        current_signal_type.set(signal_type)
        signal_frame.config(text=f"Parametry: {signal_type}")
        signal_frame.entries = {}

        if signal_type == "Harmoniczny":
            tk.Label(signal_frame, text="Amplituda:").grid(row=0, column=0)
            amp_entry = tk.Entry(signal_frame, width=10)
            amp_entry.insert(0, "1.0")
            amp_entry.grid(row=0, column=1)
            signal_frame.entries["amp"] = amp_entry

            tk.Label(signal_frame, text="Omega (rad/s):").grid(row=1, column=0)
            omega_entry = tk.Entry(signal_frame, width=10)
            omega_entry.insert(0, "3.14")
            omega_entry.grid(row=1, column=1)
            signal_frame.entries["omega"] = omega_entry
            
            tk.Label(signal_frame, text="Faza Phi (rad):").grid(row=2, column=0)
            phi_entry = tk.Entry(signal_frame, width=10)
            phi_entry.insert(0, "0")
            phi_entry.grid(row=2, column=1)
            signal_frame.entries["phi"] = phi_entry

        elif signal_type == "Prostokąt":
            tk.Label(signal_frame, text="Amplituda:").grid(row=0, column=0)
            amp_entry = tk.Entry(signal_frame, width=10)
            amp_entry.insert(0, "1.0")
            amp_entry.grid(row=0, column=1)
            signal_frame.entries["amp"] = amp_entry

            tk.Label(signal_frame, text="Częstotliwość (Hz):").grid(row=1, column=0)
            freq_entry = tk.Entry(signal_frame, width=10)
            freq_entry.insert(0, "0.2")
            freq_entry.grid(row=1, column=1)
            signal_frame.entries["freq"] = freq_entry
            
            tk.Label(signal_frame, text="Wypełnienie (0-1):").grid(row=2, column=0)
            duty_entry = tk.Entry(signal_frame, width=10)
            duty_entry.insert(0, "0.5")
            duty_entry.grid(row=2, column=1)
            signal_frame.entries["duty"] = duty_entry

        elif signal_type == "Piłokształtny":
            tk.Label(signal_frame, text="Amplituda:").grid(row=0, column=0)
            amp_entry = tk.Entry(signal_frame, width=10)
            amp_entry.insert(0, "1.0")
            amp_entry.grid(row=0, column=1)
            signal_frame.entries["amp"] = amp_entry

            tk.Label(signal_frame, text="Częstotliwość (Hz):").grid(row=1, column=0)
            freq_entry = tk.Entry(signal_frame, width=10)
            freq_entry.insert(0, "0.2")
            freq_entry.grid(row=1, column=1)
            signal_frame.entries["freq"] = freq_entry
            
            tk.Label(signal_frame, text="Symetria (0-1):").grid(row=2, column=0)
            width_entry = tk.Entry(signal_frame, width=10)
            width_entry.insert(0, "0.5")
            width_entry.grid(row=2, column=1)
            signal_frame.entries["width"] = width_entry

        tk.Button(signal_frame, text="Zmień typ sygnału", command=setup_initial_buttons).grid(row=3, column=0, columnspan=2, pady=10)

    def setup_initial_buttons():
        for widget in signal_frame.winfo_children():
            widget.destroy()
        current_signal_type.set("")
        signal_frame.config(text="Wybierz Typ Sygnału")
        
        tk.Button(signal_frame, text="Harmoniczny", command=lambda: show_signal_params("Harmoniczny")).pack(fill="x", pady=2)
        tk.Button(signal_frame, text="Prostokąt", command=lambda: show_signal_params("Prostokąt")).pack(fill="x", pady=2)
        tk.Button(signal_frame, text="Piłokształtny", command=lambda: show_signal_params("Piłokształtny")).pack(fill="x", pady=2)

    setup_initial_buttons()

    # --- 6. LOGIKA SYMULACJI ---
    def run_simulation():
        sig_type = current_signal_type.get()
        if not sig_type:
            messagebox.showwarning("Uwaga", "Wybierz najpierw typ sygnału!")
            return

        try:
            # Pobieranie parametrów
            a1 = float(a1_entry.get())
            a0 = float(a0_entry.get())
            b2 = float(b2_entry.get())
            b1 = float(b1_entry.get())
            b0 = float(b0_entry.get())

            Kp = float(kp_entry.get())
            Ti = float(ti_entry.get())
            Td = float(td_entry.get())
            
            Ki = Kp / Ti if Ti != 0 else 0.0
            Kd = Kp * Td
            Tf = 0.01 # Mała stała czasowa dla realizowalności pochodnej

            # Obliczanie transmitancji układu zamkniętego
            num_Go = [a1, a0] #licznik transmitancji obiektu
            den_Go = [b2, b1, b0] #mianownik transmitancji obiektu
            
            num_C = [Kp * Tf + Kd, Kp + Ki * Tf, Ki]
            den_C = [Tf, 1.0, 0.0]# mianownik oraz licznik regulatora
            
            num_open = np.polymul(num_C, num_Go)
            den_open = np.polymul(den_C, den_Go)
            
            num_closed = num_open
            den_closed = np.polyadd(den_open, num_open)
            system = signal.TransferFunction(num_closed, den_closed)

            # Wektor czasu i generowanie sygnału wejściowego
            t = np.linspace(0, 20.0, 2000)
            
            if sig_type == "Harmoniczny":
                amp = float(signal_frame.entries["amp"].get())
                omega = float(signal_frame.entries["omega"].get())
                phi = float(signal_frame.entries["phi"].get())
                u = amp * np.sin(omega * t + phi)
                
            elif sig_type == "Prostokąt":
                amp = float(signal_frame.entries["amp"].get())
                freq = float(signal_frame.entries["freq"].get())
                duty = float(signal_frame.entries["duty"].get())
                u = amp * (signal.square(2 * np.pi * freq * t, duty=duty) + 1) / 2 # Przesunięcie od 0 do amp
                
            elif sig_type == "Piłokształtny":
                amp = float(signal_frame.entries["amp"].get())
                freq = float(signal_frame.entries["freq"].get())
                width = float(signal_frame.entries["width"].get())
                u = amp * signal.sawtooth(2 * np.pi * freq * t, width=width)

            # Symulacja
            t_out, y_out, _ = signal.lsim(system, U=u, T=t)

            # Rysowanie na osadzonym wykresie
            ax.clear()
            ax.plot(t, u, 'k--', label='Sygnał Zadany (Wejście)', linewidth=1.5)
            ax.plot(t_out, y_out, 'b-', label='Odpowiedź Układu (Wyjście)', linewidth=2)

            ax.legend(loc = 0, framealpha=0.6, fancybox = True, shadow = False)
            ax.set_title(f'Odpowiedź dla sygnału: {sig_type}')
            ax.set_xlabel('Czas [s]')
            ax.set_ylabel('Amplituda')
            ax.grid(True, linestyle='--')
            
            
            canvas.draw()

        except ValueError:
            messagebox.showerror("Błąd danych", "Upewnij się, że wszystkie pola zawierają poprawne liczby (używaj kropek, nie przecinków).")
        except Exception as e:
            messagebox.showerror("Błąd symulacji", f"Wystąpił nieoczekiwany błąd:\n{str(e)}")

    sim_btn = tk.Button(sidebar, text="URUCHOM SYMULACJĘ", font=("Arial", 10, "bold"), bg="#4CAF50", fg="black", command=run_simulation)
    sim_btn.grid(row=3, column=0, sticky="ew", pady=15, ipady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk

def main():
    # 1. Tworzenie głównego okna
    root = tk.Tk()
    root.columnconfigure(1, weight=1) # Kolumna 1 (wykres) rośnie
    root.rowconfigure(0, weight=1)
    root.title("Analizator Sygnałów PID")
    root.geometry("800x500")

    # Przykład LabelFrame - etykietowany kontener
    sidebar = tk.Frame(root)
    sidebar.grid(row=0, column=0, sticky="ns", padx=15, pady=10)

    signal_frame = tk.LabelFrame(sidebar, text="Parametry Sygnału", padx=10, pady=10)
    signal_frame.grid(row=2, column=0, sticky="ew", pady=5)
    tk.Label(signal_frame, text="Częstotliwość (Hz):").grid(row=0, column=0, sticky="w")




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

    def calc_pid():
        kp = kp_entry.get() or "0"
        ti = ti_entry.get() or "0"
        td = td_entry.get() or "0"
        result_label.config(text=f"Kp={kp}, Ti={ti}, Td={td}")

    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox, ttk

porcentajes = {"2026": 0.1525, "2027": 0.16}

def calcular():
    try:
        monto = float(entrada_monto.get())
        if monto < 0:
            messagebox.showerror("Error", "El monto no puede ser negativo")
            return

        año = combo_año.get().split(" ")[0]
        porcentaje = porcentajes[año]

        if radio_var.get() == "bruto":
            bruto = monto
            retension = bruto * porcentaje
            liquido = bruto - retension
        else:
            liquido = monto
            bruto = liquido / (1 - porcentaje)
            retension = bruto - liquido

        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Año: {año}\n")
        resultado_text.insert(tk.END, f"Retención: {porcentaje*100}%\n\n")
        resultado_text.insert(tk.END, f"Monto Bruto: ${bruto:,.2f}\n")
        resultado_text.insert(tk.END, f"Retención: ${retension:,.2f}\n")
        resultado_text.insert(tk.END, f"Monto Líquido: ${liquido:,.2f}")
        resultado_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un monto válido")

def limpiar():
    entrada_monto.delete(0, tk.END)
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)
    resultado_text.config(state=tk.DISABLED)

def cambiar_tipo_monto():
    limpiar()

ventana = tk.Tk()
ventana.title("Simulador de Boleta de Honorarios")
ventana.geometry("700x750")
ventana.resizable(False, False)
ventana.bind("<Escape>", lambda event: ventana.quit())
ventana.config(bg="#f5f5f5")

frame_contenedor = tk.Frame(ventana, bg="#f5f5f5")
frame_contenedor.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

tk.Label(frame_contenedor, text="Simulador de Boleta de Honorarios", font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#1a1a1a").pack(anchor=tk.W, pady=(0, 30))

frame_seccion1 = tk.Frame(frame_contenedor, bg="white", relief=tk.FLAT)
frame_seccion1.pack(fill=tk.X, pady=15)

tk.Label(frame_seccion1, text="1. Año de emisión:", font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a1a").pack(anchor=tk.W, padx=20, pady=(15, 8))
combo_año = ttk.Combobox(frame_seccion1, values=[f"2026 (Retención 15.25%)", f"2027 (Retención 16%)"], state="readonly", width=40, font=("Segoe UI", 10))
combo_año.set("2027 (Retención 16%)")
combo_año.pack(anchor=tk.W, padx=20, pady=(0, 15))

frame_seccion2 = tk.Frame(frame_contenedor, bg="white", relief=tk.FLAT)
frame_seccion2.pack(fill=tk.X, pady=15)

tk.Label(frame_seccion2, text="2. ¿Con qué monto quieres simular tu boleta?", font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a1a").pack(anchor=tk.W, padx=20, pady=(15, 12))

radio_var = tk.StringVar(value="bruto")

frame_radio1 = tk.Frame(frame_seccion2, bg="white")
frame_radio1.pack(anchor=tk.W, padx=20, pady=5)
radio_bruto = tk.Radiobutton(frame_radio1, text="El monto bruto", variable=radio_var, value="bruto", bg="white", fg="#1a1a1a", font=("Segoe UI", 10), command=cambiar_tipo_monto)
radio_bruto.pack(anchor=tk.W)
tk.Label(frame_radio1, text="El valor total de tus servicios, antes de descontar la retención\ncorrespondiente.", font=("Segoe UI", 9), bg="white", fg="#666666").pack(anchor=tk.W, padx=20)

frame_radio2 = tk.Frame(frame_seccion2, bg="white")
frame_radio2.pack(anchor=tk.W, padx=20, pady=(10, 15))
radio_liquido = tk.Radiobutton(frame_radio2, text="El monto líquido", variable=radio_var, value="liquido", bg="white", fg="#1a1a1a", font=("Segoe UI", 10), command=cambiar_tipo_monto)
radio_liquido.pack(anchor=tk.W)
tk.Label(frame_radio2, text="Es lo que efectivamente recibes después de descontar la retención\ncorrespondiente.", font=("Segoe UI", 9), bg="white", fg="#666666").pack(anchor=tk.W, padx=20)

frame_seccion3 = tk.Frame(frame_contenedor, bg="white", relief=tk.FLAT)
frame_seccion3.pack(fill=tk.X, pady=15)

tk.Label(frame_seccion3, text="3. Ingresa el monto:", font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a1a").pack(anchor=tk.W, padx=20, pady=(15, 8))

frame_monto = tk.Frame(frame_seccion3, bg="white")
frame_monto.pack(anchor=tk.W, padx=20, pady=(0, 15))

tk.Label(frame_monto, text="$", font=("Segoe UI", 12, "bold"), bg="white", fg="#1a1a1a").pack(side=tk.LEFT, padx=(0, 5))

entrada_monto = tk.Entry(frame_monto, font=("Segoe UI", 11), width=35, relief=tk.FLAT, bd=0)
entrada_monto.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
entrada_monto.insert(0, "Ej: 500.000")
entrada_monto.bind("<FocusIn>", lambda e: entrada_monto.delete(0, tk.END) if entrada_monto.get() == "Ej: 500.000" else None)
entrada_monto.bind("<Return>", lambda event: calcular())

tk.Frame(frame_monto, bg="#e0e0e0", height=1).pack(side=tk.BOTTOM, fill=tk.X, expand=True)

btn_calcular = tk.Button(frame_contenedor, text="Simular mi Boleta", command=calcular, bg="#2563eb", fg="white", font=("Segoe UI", 12, "bold"), padx=20, pady=15, relief=tk.FLAT, cursor="hand2")
btn_calcular.pack(fill=tk.X, pady=20)

frame_resultados = tk.Frame(frame_contenedor, bg="white", relief=tk.FLAT)
frame_resultados.pack(fill=tk.BOTH, expand=True, pady=15)

tk.Label(frame_resultados, text="Resultado de tu simulación:", font=("Segoe UI", 11, "bold"), bg="white", fg="#1a1a1a").pack(anchor=tk.W, padx=20, pady=(15, 10))

resultado_text = tk.Text(frame_resultados, font=("Segoe UI", 10), height=8, width=50, state=tk.DISABLED, relief=tk.FLAT, bg="#f9f9f9", fg="#1a1a1a")
resultado_text.pack(padx=20, pady=(0, 15), fill=tk.BOTH, expand=True)

frame_botones = tk.Frame(frame_contenedor, bg="#f5f5f5")
frame_botones.pack(pady=(10, 0))

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar, bg="#f3f4f6", fg="#374151", font=("Segoe UI", 10), padx=15, relief=tk.FLAT, cursor="hand2")
btn_limpiar.pack(side=tk.LEFT, padx=5)

btn_cerrar = tk.Button(frame_botones, text="Cerrar", command=ventana.quit, bg="#f3f4f6", fg="#374151", font=("Segoe UI", 10), padx=15, relief=tk.FLAT, cursor="hand2")
btn_cerrar.pack(side=tk.LEFT, padx=5)

frame_aviso = tk.Frame(frame_contenedor, bg="#dbeafe", relief=tk.FLAT)
frame_aviso.pack(fill=tk.X, pady=(20, 0))

tk.Label(frame_aviso, text="Importante: Recuerda que el cálculo se realiza automáticamente al emitir tu Boleta de Honorarios, una vez que ingreses el valor bruto de la prestación.", font=("Segoe UI", 9), bg="#dbeafe", fg="#1e40af", wraplength=600, justify=tk.LEFT).pack(padx=15, pady=12)

ventana.mainloop()

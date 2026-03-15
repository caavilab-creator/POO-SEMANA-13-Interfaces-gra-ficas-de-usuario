import tkinter as tk
from tkinter import ttk, messagebox
from servicios.garaje_servicio import GarajeServicio

class AppTkinter:
    """Interfaz gráfica de la aplicación de registro de vehículos."""
    
    COLOR_FONDO       = "#F0F4F8"
    COLOR_PRIMARIO    = "#2C3E50"
    COLOR_ACENTO      = "#2980B9"
    COLOR_BOTON_REG   = "#27AE60"
    COLOR_BOTON_LIM   = "#E74C3C"
    COLOR_BOTON_DEL   = "#E67E22"
    COLOR_TEXTO       = "#FFFFFF"
    COLOR_FILA_PAR    = "#FFFFFF"
    COLOR_FILA_IMPAR  = "#EBF5FB"
    
    def __init__(self, root: tk.Tk, servicio: GarajeServicio):
        self.root = root
        self.servicio = servicio
        self._configurar_ventana()
        self._construir_ui()
    
    # ─────────────────────────── configuración ───────────────────────────
    def _configurar_ventana(self):
        self.root.title("🚗 Sistema de Gestión de Garaje")
        self.root.geometry("800x560")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLOR_FONDO)
    
    # ────────────────────────── construcción UI ──────────────────────────
    def _construir_ui(self):
        self._crear_encabezado()
        self._crear_formulario()
        self._crear_tabla()
        self._crear_pie()
    
    def _crear_encabezado(self):
        frame = tk.Frame(self.root, bg=self.COLOR_PRIMARIO, pady=12)
        frame.pack(fill="x")
        
        tk.Label(
            frame,
            text="🚗   Control de Vehículos",
            font=("Segoe UI", 18, "bold"),
            bg=self.COLOR_PRIMARIO,
            fg=self.COLOR_TEXTO,
        ).pack()
        
        tk.Label(
            frame,
            text="Registre y consulte los vehículos del garaje",
            font=("Segoe UI", 10),
            bg=self.COLOR_PRIMARIO,
            fg="#BDC3C7",
        ).pack()
    
    def _crear_formulario(self):
        contenedor = tk.LabelFrame(
            self.root,
            text=" Nuevo Vehículo ",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_PRIMARIO,
            padx=16,
            pady=12,
            relief="groove",
            bd=2,
        )
        contenedor.pack(fill="x", padx=20, pady=(16, 6))
        
        # Variables de entrada
        self.var_placa = tk.StringVar()
        self.var_marca = tk.StringVar()
        self.var_propietario = tk.StringVar()
        
        campos = [
            ("Placa: ",           self.var_placa,      False),
            ("Marca: ",           self.var_marca,      False),
            ("Propietario: ",     self.var_propietario, False),
        ]
        
        for col, (etiqueta, variable, _) in enumerate(campos):
            tk.Label(
                contenedor,
                text=etiqueta,
                font=("Segoe UI", 9, "bold"),
                bg=self.COLOR_FONDO,
                fg=self.COLOR_PRIMARIO,
            ).grid(row=0, column=col*2, sticky="w", padx=(0, 4))
            
            tk.Entry(
                contenedor,
                textvariable=variable,
                font=("Segoe UI", 10),
                width=22,
                relief="solid",
                bd=1,
            ).grid(row=1, column=col*2, padx=(0, 20), pady=4)
        
        # Botones
        frame_botones = tk.Frame(contenedor, bg=self.COLOR_FONDO)
        frame_botones.grid(row=1, column=6, padx=(10, 0))
        
        tk.Button(
            frame_botones,
            text="✔   Agregar",
            command=self._agregar_vehiculo,
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_BOTON_REG,
            fg=self.COLOR_TEXTO,
            activebackground="#1E8449",
            activeforeground=self.COLOR_TEXTO,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6,
        ).pack(side="left", padx=(0, 8))
        
        tk.Button(
            frame_botones,
            text="🗑   Eliminar",
            command=self._eliminar_vehiculo,
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_BOTON_DEL,
            fg=self.COLOR_TEXTO,
            activebackground="#D35400",
            activeforeground=self.COLOR_TEXTO,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6,
        ).pack(side="left", padx=(0, 8))
        
        tk.Button(
            frame_botones,
            text="✖   Limpiar",
            command=self._limpiar_campos,
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_BOTON_LIM,
            fg=self.COLOR_TEXTO,
            activebackground="#C0392B",
            activeforeground=self.COLOR_TEXTO,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6,
        ).pack(side="left")
    
    def _crear_tabla(self):
        contenedor = tk.LabelFrame(
            self.root,
            text=" Vehículos Registrados ",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_PRIMARIO,
            padx=16,
            pady=10,
            relief="groove",
            bd=2,
        )
        contenedor.pack(fill="both", expand=True, padx=20, pady=(6, 6))
        
        # Estilo del Treeview
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Tabla.Treeview",
            background=self.COLOR_FILA_PAR,
            fieldbackground=self.COLOR_FILA_PAR,
            rowheight=26,
            font=("Segoe UI", 9),
        )
        estilo.configure(
            "Tabla.Treeview.Heading",
            background=self.COLOR_ACENTO,
            foreground=self.COLOR_TEXTO,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
        )
        estilo.map("Tabla.Treeview", background=[("selected", "#AED6F1")])
        
        columnas = ("placa", "marca", "propietario")
        self.tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings",
            style="Tabla.Treeview",
        )
        
        # Cabeceras y anchos
        encabezados = {
            "placa":       ("Placa",        120),
            "marca":       ("Marca",        200),
            "propietario": ("Propietario",  380),
        }
        
        for col, (texto, ancho) in encabezados.items():
            self.tabla.heading(col, text=texto)
            self.tabla.column(col, width=ancho, anchor="center")
        
        # Scrollbar
        scroll = ttk.Scrollbar(contenedor, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        # Tags de color para filas alternas
        self.tabla.tag_configure("par",   background=self.COLOR_FILA_PAR)
        self.tabla.tag_configure("impar", background=self.COLOR_FILA_IMPAR)
    
    def _crear_pie(self):
        self.lbl_total = tk.Label(
            self.root,
            text="Total de vehículos: 0",
            font=("Segoe UI", 9),
            bg=self.COLOR_PRIMARIO,
            fg="#BDC3C7",
            anchor="e",
            padx=16,
            pady=5,
        )
        self.lbl_total.pack(fill="x", side="bottom")
    
    # ──────────────────────────── acciones ────────────────────────────────
    def _agregar_vehiculo(self):
        placa = self.var_placa.get()
        marca = self.var_marca.get()
        propietario = self.var_propietario.get()
        
        exito, mensaje = self.servicio.agregar_vehiculo(placa, marca, propietario)
        
        if exito:
            self._actualizar_tabla()
            self._limpiar_campos()
            messagebox.showinfo("Registro exitoso", mensaje)
        else:
            messagebox.showwarning("Error de validación", mensaje)
    
    def _limpiar_campos(self):
        self.var_placa.set("")
        self.var_marca.set("")
        self.var_propietario.set("")
    
    def _actualizar_tabla(self):
        # Limpiar filas actuales
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Insertar todos los vehículos con filas alternas
        for i, vehiculo in enumerate(self.servicio.listar_vehiculos()):
            tag = "par" if i % 2 == 0 else "impar"
            self.tabla.insert(
                "",
                "end",
                values=(vehiculo.placa, vehiculo.marca, vehiculo.propietario),
                tags=(tag,),
            )
        
        # Actualizar contador en el pie
        total = self.servicio.total_vehiculos()
        self.lbl_total.config(text=f"Total de vehículos registrados: {total}")
    
    def _eliminar_vehiculo(self):
        """Elimina el vehículo seleccionado en la tabla."""
        seleccion = self.tabla.selection()
        
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un vehículo de la tabla para eliminar.")
            return
        
        # Obtener los datos del vehículo seleccionado
        item = self.tabla.item(seleccion[0])
        placa = item['values'][0]
        
        # Confirmar eliminación
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el vehículo con placa {placa}?"
        )
        
        if confirmar:
            exito, mensaje = self.servicio.eliminar_vehiculo(placa)
            
            if exito:
                self._actualizar_tabla()
                messagebox.showinfo("Eliminación exitosa", mensaje)
            else:
                messagebox.showerror("Error", mensaje)
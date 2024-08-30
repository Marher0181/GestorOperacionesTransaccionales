import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
from Database.DataBase import Database
import pyodbc
class GestorApp:
    def __init__(self, root, db):

        self.root = root
        self.root.title("Gestión de operaciones")
        self.imagen_portada = tk.PhotoImage(file=r"enviar-dinero-telefono-inteligente.png")
        self.title_label = tk.Label(root, text=" Gestión Bancaria", font=("Trebuchet MS", 60, "bold"), bg="white",
                                    fg="#003D73", compound="left", image=self.imagen_portada)
        self.db = db
        self.title_label.pack(pady=50)
        self.centrar_ventana(root, 950, 730)
        self.create_main_menu()

    def centrar_ventana(self, ventana, ancho, altura):
        ancho_de_la_ventana = ventana.winfo_screenwidth()
        alto_de_la_ventana = ventana.winfo_screenheight()
        x = (ancho_de_la_ventana // 2) - (ancho // 2)
        y = (alto_de_la_ventana // 2) - (altura // 2)
        ventana.geometry(f"{ancho}x{altura}+{x}+{y}")

    def create_main_menu(self):
        self.imagen_deposito = tk.PhotoImage(file=r"Iconos/deposito.png")
        self.imagen_retiro = tk.PhotoImage(file=r"Iconos/retiro.png")
        self.imagen_transferencia = tk.PhotoImage(file=r"Iconos/transferencia.png")
        self.imagen_salir = tk.PhotoImage(file=r"Iconos/salir.png")
        self.imagen_deposito_port = tk.PhotoImage(file=r"Iconos/deposito_port.png")
        self.imagen_regresar = tk.PhotoImage(file=r"Iconos/regresar.png")
        self.imagen_retiro_port = tk.PhotoImage(file=r"Iconos/retiro_port.png")
        self.imagen_transferencia_port = tk.PhotoImage(file=r"Iconos/transferencia-port.png")
        self.imagen_administración = tk.PhotoImage(file=r"Iconos/administracion.png")
        self.imagen_adm_usuarios = tk.PhotoImage(file=r"Iconos/administrar_usuarios.png")
        self.imagen_adm_empleados = tk.PhotoImage(file=r"Iconos/administrar_empleados.png")
        self.imagen_adm_sucursales = tk.PhotoImage(file=r"Iconos/administrar_sucursales.png")
        self.imagen_adm_cuentas = tk.PhotoImage(file=r"Iconos/administrar_cuentas.png")
        self.imagen_administración_port = tk.PhotoImage(file=r"Iconos/administracion_port.png")
        self.imagen_adm_usuarios_port = tk.PhotoImage(file=r"Iconos/administrar_usuarios_port.png")
        self.imagen_adm_empleados_port = tk.PhotoImage(file=r"Iconos/administrar_empleados_port.png")
        self.imagen_adm_sucursales_port = tk.PhotoImage(file=r"Iconos/administrar_sucursales_port.png")
        self.imagen_adm_cuentas_port = tk.PhotoImage(file=r"Iconos/administrar_cuentas_port.png")

        self.menu_bar = tk.Menu(self.root)
        self.menu_bar.add_cascade(label="Depósitos")
        self.menu_bar.add_cascade(label="Retiros")
        self.menu_bar.add_cascade(label="Transferencias")
        self.menu_bar.add_cascade(label="Empleados")
        self.menu_bar.add_cascade(label="Clientes")
        self.menu_bar.add_cascade(label="Sucursales")
        self.menu_bar.add_cascade(label="Cuentas")


        button = tk.Button(self.root, text="  Depósitos", command=self.abrir_ventana_deposito, bg="#FFBD28", fg="#003D73",
                           font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_deposito, width=500, height=60)
        button.pack(pady=10)
        buttonu = tk.Button(self.root, text="  Retiros", command=self.abrir_ventana_retiro, bg="#3DCFCD", fg="white",
                            font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_retiro, width=500, height=60)
        buttonu.pack(pady=10)
        buttonp = tk.Button(self.root, text="  Transferencias", command=self.abrir_ventana_transferencia,bg="#3DCFCD", fg="white",
                            font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_transferencia, width=500, height=60)
        buttonp.pack(pady=10)
        buttonp = tk.Button(self.root, text="  Administración", command=self.abrir_ventana_administracion, bg="#3DCFCD", fg="white",
                            font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_administración, width=500, height=60)
        buttonp.pack(pady=10)
        buttonp = tk.Button(self.root, text="  Salir", command=self.root.quit, bg="#003D73", fg="white",
                            font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_salir, width=500, height=60)
        buttonp.pack(pady=10)



    def abrir_ventana_deposito(self):
        ventana = Toplevel(self.root)
        ventana.title("Depósito")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 575, 420)

        title_label = tk.Label(ventana, text=" Depósito", font=("Trebuchet MS", 60, "bold"), bg="white",
                               fg="#003D73", compound="left", image=self.imagen_deposito_port)
        title_label.grid(row=0, columnspan=2, column=0)

        label_No = tk.Label(ventana, text="Número de cuenta", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73", bg="white")
        label_No.grid(row=1, column=0, padx=10,  sticky="w", pady=10)
        label_Monto = tk.Label(ventana, text="Monto", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73", bg="white")
        label_Monto.grid(row=2, column=0, padx=10, sticky="w", pady=10)
        label_idSucursal = tk.Label(ventana, text="Id Sucursal", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73", bg="white")
        label_idSucursal.grid(row=3, column=0, padx=10, sticky="w", pady=10)

        entry_No = tk.Entry(ventana, width=15, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove", bd=2)
        entry_No.grid(row=1, column=1, padx=10)
        entry_Monto = tk.Entry(ventana, width=15, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove", bd=2)
        entry_Monto.grid(row=2, column=1, padx=10)
        entry_idSucursal = tk.Entry(ventana, width=15, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove", bd=2)
        entry_idSucursal.grid(row=3, column=1, padx=10)

        def deposito():
            no_cuenta = entry_No.get()
            monto = float(entry_Monto.get())
            idSucursal = int(entry_idSucursal.get())
            if no_cuenta and monto and idSucursal:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_Deposito @numeroCuenta = ?, @monto = ?, @idSucursal = ?",
                            (no_cuenta, monto, idSucursal))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50001" in error_message:
                            messagebox.showwarning("Duplicado", "El ID del cliente ya existe.")
                        else:
                            messagebox.showerror("Error al agregar", f"No se pudo agregar el cliente: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, complete todos los campos.")
        button = tk.Button(ventana, text="Depositar", bg="#FFBD28", fg="#003D73", command=deposito,
                           font=("Franklin Gothic Book", 25, "bold"), width=10, height=1)

        button.grid(row=4, column=1, pady=20)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=4, sticky="sw", column=0, padx=20, pady=20)


    def abrir_ventana_retiro(self):
        ventana = Toplevel(self.root)
        ventana.title("Retiro")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 575, 420)
        title_label = tk.Label(ventana, text=" Retiro", font=("Trebuchet MS", 60, "bold"), bg="white",
                               fg="#003D73", compound="left", image=self.imagen_retiro_port)
        title_label.grid(row=0, columnspan=2, column=0)
        label_No = tk.Label(ventana, text="Número de cuenta", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                            bg="white")
        label_No.grid(row=1, column=0, padx=10, sticky="w", pady=10)
        label_Monto = tk.Label(ventana, text="Monto", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                               bg="white")
        label_Monto.grid(row=2, column=0, padx=10, sticky="w", pady=10)
        label_idSuc = tk.Label(ventana, text="Id Sucursal", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                               bg="white")
        label_idSuc.grid(row=3, column=0, padx=10, sticky="w", pady=10)

        entry_No = tk.Entry(ventana, width=15, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                            bd=2)
        entry_No.grid(row=1, column=1, padx=10)
        entry_Monto = tk.Entry(ventana, width=15, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                               bd=2)
        entry_Monto.grid(row=2, column=1, padx=10)

        entry_idSuc = tk.Entry(ventana, width=15, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                               bd=2)
        entry_idSuc.grid(row=3, column=1, padx=10)

        def retiro():
            no_cuenta = entry_No.get()
            monto = float(entry_Monto.get())
            idSucursal = int(entry_idSuc.get())
            if no_cuenta and monto and idSucursal:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_Retiro @numeroCuenta = ?, @monto = ?, @idSucursal = ?",
                            (no_cuenta, monto, idSucursal))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50001" in error_message:
                            messagebox.showwarning("Duplicado", "El ID del cliente ya existe.")
                        else:
                            messagebox.showerror("Error al agregar", f"No se pudo agregar el cliente: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, complete todos los campos.")

        button = tk.Button(ventana, text="Retirar", bg="#FFBD28", fg="#003D73", command=retiro,
                           font=("Franklin Gothic Book", 25, "bold"), width=10, height=1)
        button.grid(row=4, column=1, pady=20)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=4, sticky="sw", column=0, padx=20, pady=20)

    def abrir_ventana_transferencia(self):
        ventana = Toplevel(self.root)
        ventana.title("Transferencia")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 680, 600)
        title_label = tk.Label(ventana, text=" Transferencia", font=("Trebuchet MS", 60, "bold"), bg="white",
                               fg="#003D73", compound="left", image=self.imagen_transferencia_port)
        title_label.grid(row=0, columnspan=2, column=0)
        label_No = tk.Label(ventana, text="Número de cuenta \n (origen)", font=("Franklin Gothic Book", 20, "bold"), fg="#003D73",
                            bg="white")
        label_No.grid(row=1, column=0, padx=10)
        label_Monto = tk.Label(ventana, text="Monto", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                               bg="white")
        label_Monto.grid(row=2, column=0, padx=10, sticky="w", pady=20)
        label_Origen = tk.Label(ventana, text="Número de cuenta \n (destino)", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                                bg="white")
        label_Origen.grid(row=3, column=0, padx=10, sticky="w", pady=20)
        label_ID = tk.Label(ventana, text="ID de la Sucursal", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                            bg="white")
        label_ID.grid(row=4, column=0, padx=10, sticky="w", pady=20)
        entry_No = tk.Entry(ventana, width=20, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                            bd=2)
        entry_No.grid(row=1, column=1, padx=10)
        entry_Monto = tk.Entry(ventana, width=20, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                               bd=2)
        entry_Monto.grid(row=2, column=1, padx=10)
        entry_des = tk.Entry(ventana, width=20, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                bd=2)
        entry_des.grid(row=3, column=1, padx=10)
        entry_ID = tk.Entry(ventana, width=20, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                            bd=2)
        entry_ID.grid(row=4, column=1, padx=10)

        def transferencia():
            no_cuentao = entry_No.get()
            monto = float(entry_Monto.get())
            no_cuentad = entry_des.get()
            idSucursal = int(entry_ID.get())
            if no_cuentao and monto and no_cuentad and idSucursal:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_Transaccion  @numeroCuenta = ?,@monto = ?, @idSucursal = ?, @numeroCuentaDestino = ?",
                            (no_cuentao, monto, idSucursal, no_cuentad))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Transferencia exitosa")
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50001" in error_message:
                            messagebox.showwarning("Duplicado", "Transferencia ya existe.")
                        else:
                            messagebox.showerror("Error al agregar", f"No se pudo agregar la Transferencia: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, complete todos los campos.")

        button = tk.Button(ventana, text="Transferir", bg="#FFBD28", fg="#003D73", command=transferencia,
                           font=("Franklin Gothic Book", 25, "bold"), width=10, height=1)
        button.grid(row=5, column=1, pady=20)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, sticky="sw", column=0, padx=20, pady=20)

    def abrir_ventana_administracion(self):
        ventana = Toplevel(self.root)
        ventana.title("Administración")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 700, 520)
        label_adm = tk.Label(ventana, text=" Administración", font=("Franklin Gothic Book", 60, "bold"), fg="#003D73",
                             bg="white", compound="left", image=self.imagen_administración_port)
        label_adm.pack(pady=10)
        button = tk.Button(ventana, text=" Clientes", command=self.abrir_ventana_adm_clientes, bg="#FFBD28", fg="#003D73",
                           font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_adm_usuarios, width=300, height=60)
        button.pack(pady=10)
        button = tk.Button(ventana, text=" Empleados", command=self.abrir_ventana_adm_empleados,  bg="#3DCFCD", fg="white",
                           font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_adm_empleados, width=300, height=60)
        button.pack(pady=10)
        button = tk.Button(ventana, text=" Sucursales", command=self.abrir_ventana_adm_sucursales,  bg="#3DCFCD", fg="white",
                           font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_adm_sucursales, width=300, height=60)
        button.pack(pady=10)
        button = tk.Button(ventana, text=" Cuentas", command=self.abrir_ventana_adm_cuentas,  bg="#003D73", fg="white",
                           font=("Franklin Gothic Book", 25, "bold"), compound="left", image=self.imagen_adm_cuentas, width=300, height=60)
        button.pack(pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.pack(anchor="sw", pady=0, padx=10)


    def abrir_ventana_adm_clientes(self):
        ventana = Toplevel(self.root)
        ventana.title("Administrar Clientes")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 780, 500)

        def limpiar_campos():
            entry_id_cliente.delete(0, tk.END)
            entry_nombre_cliente.delete(0, tk.END)
            entry_direccion_cliente.delete(0, tk.END)
            entry_email_cliente.delete(0, tk.END)
            entry_telefono_cliente.delete(0, tk.END)

        def agregar_cliente():
            id_cliente = entry_id_cliente.get()
            nombre_cliente = entry_nombre_cliente.get()
            direccion_cliente = entry_direccion_cliente.get()
            email_cliente = entry_email_cliente.get()
            telefono_cliente = entry_telefono_cliente.get()
            seleccion = 'Insertar'
            if id_cliente and nombre_cliente and direccion_cliente and email_cliente and telefono_cliente:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarCliente @Seleccion = ?, @numeroIdentificacion = ?, @nombreCliente = ?, @direccionCliente = ?, @email = ?, @telefono = ?",
                            (seleccion, id_cliente, nombre_cliente, direccion_cliente, email_cliente,
                             telefono_cliente))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
                        limpiar_campos()
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50001" in error_message:
                            messagebox.showwarning("Duplicado", "El ID del cliente ya existe.")
                        else:
                            messagebox.showerror("Error al agregar", f"No se pudo agregar el cliente: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, complete todos los campos.")

        def eliminar_cliente():
            id_cliente = int(entry_id_cliente.get())
            if id_cliente:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarCliente @Seleccion = ?, @numeroIdentificacion = ?, @nombreCliente = null, @direccionCliente = null, @email = null, @telefono = null",
                            ('Eliminar', id_cliente))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
                        limpiar_campos()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50002" in error_message:
                            messagebox.showwarning("No encontrado", "El cliente no existe.")
                        else:
                            messagebox.showerror("Error al eliminar",
                                                 f"No se pudo eliminar el paciente: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, ingrese un ID.")

        title_label = tk.Label(ventana, text=" Clientes", font=("Trebuchet MS", 60, "bold"), bg="white",
                               fg="#003D73", compound="left", image=self.imagen_adm_usuarios_port)
        title_label.grid(row=0, columnspan=2, column=0)
        tk.Label(ventana, text="Numero Identificacion", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=1, column=0, sticky="w", padx=10)
        entry_id_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                    bd=2)
        entry_id_cliente.grid(row=1, column=1, padx=10)

        tk.Label(ventana, text="Nombre del Cliente", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=2, column=0, sticky="w", padx=10)
        entry_nombre_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                        bd=2)
        entry_nombre_cliente.grid(row=2, column=1, padx=10)

        tk.Label(ventana, text="Dirección del Cliente", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=3, column=0, sticky="w", padx=10)
        entry_direccion_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                           bd=2)
        entry_direccion_cliente.grid(row=3, column=1, padx=10)

        tk.Label(ventana, text="Email del Cliente", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=4, column=0, sticky="w", padx=10)
        entry_email_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                       bd=2)
        entry_email_cliente.grid(row=4, column=1, padx=10)

        tk.Label(ventana, text="Teléfono del Cliente", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=5, column=0, sticky="w", padx=10)
        entry_telefono_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                          bd=2)
        entry_telefono_cliente.grid(row=5, column=1, padx=10)

        boton = tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente, bg="#FFBD28", fg="#003D73",
                          font=("Franklin Gothic Book", 25, "bold"), width=15, height=1)
        boton.grid(row=6,column=0, padx=10, pady=10)
        boton2 = (tk.Button(ventana, text="Eliminar Cliente", command=eliminar_cliente, bg="#003D73", fg="white",
                            font=("Franklin Gothic Book", 25, "bold"), width=15, height=1))
        boton2.grid(row=6, column=1, padx=10, pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=7, sticky="w", column=0, padx=20, pady=20)

    def abrir_ventana_adm_empleados(self):
        ventana = Toplevel(self.root)
        ventana.title("Administrar Empleados")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 790, 530)

        def limpiar_campos():
            entry_id_empleado.delete(0, tk.END)
            entry_nombre_empleado.delete(0, tk.END)
            entry_cargo.delete(0, tk.END)
            entry_salario.delete(0, tk.END)
            entry_telefono_emp.delete(0, tk.END)

        def agregar_empleado():
            nombre_empleado = entry_nombre_empleado.get()
            cargo = entry_cargo.get()
            salario = int(entry_salario.get())
            telefono = entry_telefono_emp.get()
            email = entry_email.get()

            if nombre_empleado and cargo and salario and telefono and email:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarEmpleados  @Seleccion = ?, @idEmpleado = null, @nombreEmpleado = ?, @cargo = ?, @salario = ?, @telefono = ?, @email = ?",
                            ('Insertar', nombre_empleado, cargo, salario,
                             telefono, email))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Empleado agregado correctamente")
                        limpiar_campos()
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50001" in error_message:
                            messagebox.showwarning("Duplicado", "El ID del cliente ya existe.")
                        else:
                            messagebox.showerror("Error al agregar", f"No se pudo agregar el cliente: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, complete todos los campos.")

        def eliminar_empleado():
            id_cliente = int(entry_id_empleado.get())
            if id_cliente:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarEmpleados  @Seleccion = ?, @idEmpleado = ?, @nombreEmpleado = null, @cargo = null, @salario = null, @telefono = null, @email = null",
                            ('Eliminar', id_cliente))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
                        limpiar_campos()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50002" in error_message:
                            messagebox.showwarning("No encontrado", "El Empleado no existe.")
                        else:
                            messagebox.showerror("Error al eliminar",
                                                 f"No se pudo eliminar el Empleado: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, ingrese un ID.")

        title_label = tk.Label(ventana, text=" Empleados", font=("Trebuchet MS", 60, "bold"), bg="white",
                               fg="#003D73", compound="left", image=self.imagen_adm_empleados_port)
        title_label.grid(row=0, columnspan=2, column=0)
        tk.Label(ventana, text="ID Empleado", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=1, column=0, sticky="w", padx=10)
        entry_id_empleado = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                    bd=2)
        entry_id_empleado.grid(row=1, column=1, padx=10)

        tk.Label(ventana, text="Nombre del Empleado", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=2, column=0, sticky="w", padx=10)
        entry_nombre_empleado = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                        bd=2)
        entry_nombre_empleado.grid(row=2, column=1, padx=10)

        tk.Label(ventana, text="Cargo", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=3, column=0, sticky="w", padx=10)
        entry_cargo = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                           bd=2)
        entry_cargo.grid(row=3, column=1, padx=10)

        tk.Label(ventana, text="Salario", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=4, column=0, sticky="w", padx=10)
        entry_salario = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                       bd=2)
        entry_salario.grid(row=4, column=1, padx=10)

        tk.Label(ventana, text="Teléfono del Empleado", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=5, column=0, sticky="w", padx=10)
        entry_telefono_emp = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                          bd=2)
        entry_telefono_emp.grid(row=5, column=1, padx=10)

        tk.Label(ventana, text="Email del Empleado", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=6, column=0, sticky="w", padx=10)
        entry_email = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                          bd=2)
        entry_email.grid(row=6, column=1, padx=10)

        tk.Button(ventana, text="Agregar Empleado", command=agregar_empleado, bg="#FFBD28", fg="#003D73",
                  font=("Franklin Gothic Book", 25, "bold"), width=15, height=1).grid(row=7,column=0, padx=10, pady=10)
        tk.Button(ventana, text="Eliminar Empleado", command=eliminar_empleado, bg="#003D73", fg="white",
                  font=("Franklin Gothic Book", 25, "bold"), width=15, height=1).grid(row=7, column=1, padx=10, pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=8, sticky="w", column=0, padx=20, pady=20)

    def abrir_ventana_adm_sucursales(self):
        ventana = Toplevel(self.root)
        ventana.title("Administrar Sucursales")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 800, 400)

        def limpiar_campos():

            entry_nombre_cliente.delete(0, tk.END)
            entry_direccion_cliente.delete(0, tk.END)
            entry_email_cliente.delete(0, tk.END)


        def agregar_sucursal():

            nombre_sucursal = entry_nombre_cliente.get()
            direccion_sucursal = entry_direccion_cliente.get()
            empleado_responsable = int(entry_email_cliente.get())


            if nombre_sucursal and direccion_sucursal and empleado_responsable :
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarSucursales @Seleccion = ?, @nombreSucursal = ?, @direccionSucursal = ?, @idEmpleadoResponsable = ?",
                            ('Insertar', nombre_sucursal, direccion_sucursal, empleado_responsable))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Sucursal agregada correctamente")
                        limpiar_campos()
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50001" in error_message:
                            messagebox.showwarning("Duplicado", "La sucursal ya existe.")
                        else:
                            messagebox.showerror("Error al agregar", f"No se pudo agregar la sucursal: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, complete todos los campos.")

        def eliminar_sucursal():
            id_cliente = entry_nombre_cliente
            if id_cliente:
                conn = self.db
                if conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarEmpleados @Seleccion = ?, @numeroIdentificacion = ?, @nombreCliente = null, @direccionCliente = null, @email = null, @telefono = null",
                            ('Eliminar', id_cliente))
                        conn.commit()
                        messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
                        limpiar_campos()
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50002" in error_message:
                            messagebox.showwarning("No encontrado", "La sucursal no existe.")
                        else:
                            messagebox.showerror("Error al eliminar",
                                                 f"No se pudo eliminar la sucursal: {error_message}")
                    finally:
                        
                        conn.close()
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, ingrese un ID.")

        title_label = tk.Label(ventana, text=" Sucursales", font=("Trebuchet MS", 60, "bold"), bg="white",
                               fg="#003D73", compound="left", image=self.imagen_adm_empleados_port)
        title_label.grid(row=0, columnspan=2, column=0)

        tk.Label(ventana, text="Nombre de sucursal", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=2, column=0, sticky="w", padx=10)
        entry_nombre_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                        bd=2)
        entry_nombre_cliente.grid(row=2, column=1, padx=10)

        tk.Label(ventana, text="Direccion", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=3, column=0, sticky="w", padx=10)
        entry_direccion_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                           bd=2)
        entry_direccion_cliente.grid(row=3, column=1, padx=10)

        tk.Label(ventana, text="Empleado Responsable", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=4, column=0, sticky="w", padx=10)
        entry_email_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                       bd=2)
        entry_email_cliente.grid(row=4, column=1, padx=10)

        tk.Button(ventana, text="Agregar Sucursal", command=agregar_sucursal, bg="#FFBD28", fg="#003D73",
                  font=("Franklin Gothic Book", 25, "bold"), width=15, height=1).grid(row=5,column=0, padx=10, pady=10)
        tk.Button(ventana, text="Eliminar Sucursal", command=eliminar_sucursal, bg="#003D73", fg="white",
                  font=("Franklin Gothic Book", 25, "bold"), width=15, height=1).grid(row=5, column=1, padx=10, pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=6, sticky="w", column=0, padx=20, pady=20)

    def abrir_ventana_adm_cuentas(self):
        ventana = Toplevel(self.root)
        ventana.title("Administrar Cuentas")
        ventana.config(bg="white")
        self.centrar_ventana(ventana, 750, 450)

        def limpiar_campos():
            entry_num_cuenta.delete(0, tk.END)
            entry_saldo.delete(0, tk.END)
            entry_cliente.delete(0, tk.END)
            entry_tipo_cuenta.delete(0, tk.END)

        def agregar_cuenta():
            numero_cuenta = entry_num_cuenta.get()
            saldo = entry_saldo.get()
            cliente = entry_cliente.get()
            tipoCuenta = entry_tipo_cuenta.get()
            seleccion = 'Insertar'
            if numero_cuenta and saldo and cliente and tipoCuenta:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarCuentasBancarias @Seleccion = ?, @numeroCuenta = ?, @saldo = ?, @idCliente = ?, @idTipoCuenta = ?",
                            (seleccion, numero_cuenta, saldo, cliente,
                             tipoCuenta))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Cuenta agregada correctamente")
                        limpiar_campos()
                        ventana.destroy()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50001" in error_message:
                            messagebox.showwarning("Duplicado", "El numero de la cuenta ya existe.")
                        else:
                            messagebox.showerror("Error al agregar", f"No se pudo agregar la Cuenta: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, complete todos los campos.")

        def eliminar_cuenta():
            numero_cuenta = entry_num_cuenta.get()
            if numero_cuenta:
                cursor = self.db.cursor
                if cursor:
                    try:
                        cursor.execute(
                            "EXEC sp_GestionarCuentasBancarias @Seleccion = ?, @numeroCuenta = ?, @saldo = null, @idCliente = null, @idTipoCuenta = null",
                            ('Eliminar', numero_cuenta))
                        cursor.commit()
                        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
                        limpiar_campos()
                    except pyodbc.Error as e:
                        error_message = str(e)
                        if "50002" in error_message:
                            messagebox.showwarning("No encontrado", "El cliente no existe.")
                        else:
                            messagebox.showerror("Error al eliminar",
                                                 f"No se pudo eliminar el paciente: {error_message}")
            else:
                messagebox.showwarning("Entrada vacía", "Por favor, ingrese un ID.")

        title_label = tk.Label(ventana, text=" Cuentas", font=("Trebuchet MS", 60, "bold"), bg="white",
                               fg="#003D73", compound="left", image=self.imagen_adm_cuentas_port)
        title_label.grid(row=0, columnspan=2, column=0)
        tk.Label(ventana, text="Numero Cuenta", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=1, column=0, sticky="w", padx=10)
        entry_num_cuenta = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                    bd=2)
        entry_num_cuenta.grid(row=1, column=1, padx=10)

        tk.Label(ventana, text=" Saldo", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=2, column=0, sticky="w", padx=10)
        entry_saldo = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                        bd=2)
        entry_saldo.grid(row=2, column=1, padx=10)

        tk.Label(ventana, text=" Cliente", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=3, column=0, sticky="w", padx=10)
        entry_cliente = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                           bd=2)
        entry_cliente.grid(row=3, column=1, padx=10)

        tk.Label(ventana, text=" Tipo Cuenta", font=("Franklin Gothic Book", 25, "bold"), fg="#003D73",
                 bg="white").grid(row=4, column=0, sticky="w", padx=10)
        entry_tipo_cuenta = tk.Entry(ventana, width=25, fg="gray", font=("Franklin Gothic Book", 20, "bold"), relief="groove",
                                       bd=2)
        entry_tipo_cuenta.grid(row=4, column=1, padx=10)


        boton = tk.Button(ventana, text="Agregar Cuenta", command=agregar_cuenta, bg="#FFBD28", fg="#003D73",
                          font=("Franklin Gothic Book", 25, "bold"), width=15, height=1)
        boton.grid(row=5,column=0, padx=10, pady=10)
        boton2 = (tk.Button(ventana, text="Eliminar Cuenta", command=eliminar_cuenta, bg="#003D73", fg="white",
                            font=("Franklin Gothic Book", 25, "bold"), width=15, height=1))
        boton2.grid(row=5, column=1, padx=10, pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="#3DCFCD", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=6, sticky="w", column=0, padx=20, pady=20)


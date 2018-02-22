import gi
import sqlite3 as dbapi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MascotasPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Principal")

        # Declaracion de la caja principal
        caixaventana = Gtk.Box(spacing=2)
        caixaventana.set_orientation(Gtk.Orientation.VERTICAL)
        caixaventana.set_margin_left(10)
        caixaventana.set_margin_right(10)
        caixaventana.set_size_request(200, 150)

        self.add(caixaventana)

        # Declaracion de la caja Superior
        caixaSuperior = Gtk.Box()
        caixaventana.add(caixaSuperior)

        nombretienda = Gtk.Label("Nombre de la tienda")
        caixaSuperior.add(nombretienda)

        caixaSuperior.set_margin_bottom(30)

        # Declaracion de la caja Inferior
        caixaInferior = Gtk.Box(spacing=20)
        caixaInferior.set_orientation(Gtk.Orientation.HORIZONTAL)
        caixaInferior.set_size_request(200, 150)

        caixaventana.add(caixaInferior)

        # Declaracion de las cajas separadoras dere e izq
        caixaInferiorDere = Gtk.Box(spacing=20)
        caixaInferiorDere.set_orientation(Gtk.Orientation.VERTICAL)
        caixaInferiorDere.set_size_request(200, 75)

        caixaInferiorIzq = Gtk.Box(spacing=20)
        caixaInferiorIzq.set_orientation(Gtk.Orientation.VERTICAL)
        caixaInferiorIzq.set_size_request(200, 75)

        botonMascotas = Gtk.Button("Gestión de mascotas")
        botonClientes = Gtk.Button("Gestión de clientes")
        botonListado = Gtk.Button("Listado")
        botonSalir = Gtk.Button("Salir")

        # Declaracion de los botones
        caixaInferiorDere.add(botonClientes)
        caixaInferiorIzq.add(botonMascotas)
        caixaInferiorDere.add(botonListado)
        caixaInferiorIzq.add(botonSalir)

        caixaInferior.add(caixaInferiorDere)
        caixaInferior.add(caixaInferiorIzq)

        # Eventos de los botones
        botonMascotas.connect("clicked", self.on_boton_mascotas)
        botonListado.connect("clicked", self.on_boton_listado)
        botonClientes.connect("clicked", self.on_boton_clientes)
        botonSalir.connect("clicked", self.on_boton_salir)

    def on_boton_mascotas (self, button):

        regis = MascotasRegistro()
        regis.show_all()

    def on_boton_clientes (self, button):
        cli = MascotasClientes()
        cli.show_all()

    def on_boton_listado (self, button):
        lista = MascotasListado()
        lista.show_all()

    def on_boton_salir (self, button):
        Gtk.main_quit()

class MascotasRegistro(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Clientes")

        # Declaracion de la caja principal
        self.caixaventana = Gtk.Box(spacing=10)
        self.caixaventana.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.caixaventana.set_margin_left(10)
        self.caixaventana.set_margin_right(10)
        self.caixaventana.set_size_request(400, 300)
        self.add(self.caixaventana)

        ##Declaracion caja crear
        self.caixaCrear = Gtk.Box(spacing=10)
        self.caixaCrear.set_orientation(Gtk.Orientation.VERTICAL)

        self.frameCrear = Gtk.Frame()
        self.frameCrear.set_label("Registro de mascota")
        self.frameCrear.add(self.caixaCrear)
        self.caixaventana.add(self.frameCrear)

        #Combo DNI
        self.etiquetaDni = Gtk.Label("Dni del cliente")
        self.entryDni = Gtk.ListStore(str)
        self.cargar_dni_cliente()

        self.country_combo = Gtk.ComboBox.new_with_model(self.entryDni)

        self.country_combo.connect("changed", self.on_country_combo_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.country_combo.pack_start(self.renderer_text, True)
        self.country_combo.add_attribute(self.renderer_text, "text", 0)

        ###

        self.etiquetaId = Gtk.Label("Id")
        self.entryId = Gtk.Entry()

        self.etiquetaNombre = Gtk.Label("Nombre")
        self.entryNombre = Gtk.Entry()

        self.etiquetaTipo = Gtk.Label("Tipo de animal")
        self.entryTipo = Gtk.Entry()

        self.etiquetaSexo = Gtk.Label("Sexo")

        self.cajaRadio = Gtk.Box(spacing=10)
        self.cajaRadio.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoH = Gtk.RadioButton.new_with_label_from_widget(None, "Macho")
        self.sexoH.connect("toggled", self.on_button_toggled, "1")

        self.sexoM = Gtk.RadioButton.new_from_widget(self.sexoH)
        self.sexoM.set_label("Hembra")
        self.sexoM.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadio.add(self.sexoH)
        self.cajaRadio.add(self.sexoM)

        self.etiquetaRaza = Gtk.Label("Raza")
        self.entryRaza = Gtk.Entry()


        self.botonCrear = Gtk.Button("Registrar mascota")

        self.caixaCrear.add(self.etiquetaDni)
        self.caixaCrear.add(self.country_combo)
        self.caixaCrear.add(self.etiquetaId)
        self.caixaCrear.add(self.entryId)
        self.caixaCrear.add(self.etiquetaNombre)
        self.caixaCrear.add(self.entryNombre)
        self.caixaCrear.add(self.etiquetaTipo)
        self.caixaCrear.add(self.entryTipo)
        self.caixaCrear.add(self.etiquetaSexo)

        self.caixaCrear.add(self.cajaRadio)

        self.caixaCrear.add(self.etiquetaRaza)
        self.caixaCrear.add(self.entryRaza)

        self.caixaCrear.add(self.botonCrear)

        self.botonCrear.connect("clicked", self.on_crear_mascota)

        ##Declaracion caja modificar
        self.caixaMod = Gtk.Box(spacing=10)
        self.caixaMod.set_orientation(Gtk.Orientation.VERTICAL)

        self.frameMod = Gtk.Frame()
        self.frameMod.set_label("Modificacion de mascota")
        self.frameMod.add(self.caixaMod)
        self.caixaventana.add(self.frameMod)

        ##
        self.etiquetaIdM = Gtk.Label("Id")
        self.entryIdM = Gtk.ListStore(str)

        self.country_comboM = Gtk.ComboBox.new_with_model(self.entryIdM)

        self.auxMod = self.country_comboM.connect("changed", self.on_country_combo_changed2)
        self.renderer_textM = Gtk.CellRendererText()
        self.country_comboM.pack_start(self.renderer_textM, True)
        self.country_comboM.add_attribute(self.renderer_textM, "text", 0)

        ##

        self.etiquetaNombreM = Gtk.Label("Nombre")
        self.entryNombreM = Gtk.Entry()

        self.etiquetaTipoM = Gtk.Label("Tipo de animal")
        self.entryTipoM = Gtk.Entry()

        self.etiquetaSexoM = Gtk.Label("Sexo")

        self.cajaRadioM = Gtk.Box(spacing=10)
        self.cajaRadioM.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoHM = Gtk.RadioButton.new_with_label_from_widget(None, "Macho")
        self.sexoHM.connect("toggled", self.on_button_toggled, "1")

        self.sexoMM = Gtk.RadioButton.new_from_widget(self.sexoHM)
        self.sexoMM.set_label("Hembra")
        self.sexoMM.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadioM.add(self.sexoHM)
        self.cajaRadioM.add(self.sexoMM)

        self.etiquetaRazaM = Gtk.Label("Raza")
        self.entryRazaM = Gtk.Entry()

        self.botonMod = Gtk.Button("Modificar mascota")

        self.caixaMod.add(self.etiquetaIdM)
        self.caixaMod.add(self.country_comboM)
        self.caixaMod.add(self.etiquetaNombreM)
        self.caixaMod.add(self.entryNombreM)
        self.caixaMod.add(self.etiquetaTipoM)
        self.caixaMod.add(self.entryTipoM)
        self.caixaMod.add(self.etiquetaSexoM)

        self.caixaMod.add(self.cajaRadioM)

        self.caixaMod.add(self.etiquetaRazaM)
        self.caixaMod.add(self.entryRazaM)

        self.caixaMod.add(self.botonMod)

        self.botonMod.connect("clicked", self.on_modificar_mascota)

        ##Declaracion caja eliminar
        self.caixaEliminar = Gtk.Box(spacing=10)
        self.caixaEliminar.set_orientation(Gtk.Orientation.VERTICAL)

        self.frameEliminar = Gtk.Frame()
        self.frameEliminar.set_label("Eliminar mascota")
        self.frameEliminar.add(self.caixaEliminar)
        self.caixaventana.add(self.frameEliminar)

        ##
        self.etiquetaIdE = Gtk.Label("Id")
        self.entryIdE = Gtk.ListStore(str)
        self.cargar_id_mascota()

        self.country_comboE = Gtk.ComboBox.new_with_model(self.entryIdM)

        self.auxEliminar = self.country_comboE.connect("changed", self.on_country_combo_changed3)
        self.renderer_textE = Gtk.CellRendererText()
        self.country_comboE.pack_start(self.renderer_textE, True)
        self.country_comboE.add_attribute(self.renderer_textE, "text", 0)

        ##
        self.botonEliminar = Gtk.Button("Eliminar mascota")

        self.caixaEliminar.add(self.etiquetaIdE)
        self.caixaEliminar.add(self.country_comboE)
        self.caixaEliminar.add(self.botonEliminar)

        self.botonEliminar.connect("clicked", self.on_borrar_mascota)




    def cargar_dni_cliente(self):
        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()

        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                                    (dni TEXT PRIMARY KEY, 
                                     nombre TEXT NOT NULL, 
                                     apellidos TEXT NOT NULL,
                                     sexo TEXT NOT NULL,
                                     direccion TEXT NOT NULL, 
                                     telefono TEXT NOT NULL,
                                     email TEXT NOT NULL)
                        """)
            cursor.execute("select dni from clientes")
            for rexistro in cursor.fetchall():
                self.entryDni.append([rexistro[0]])

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def cargar_id_mascota(self):
        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()

        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS mascotas
                                                    (id TEXT PRIMARY KEY,
                                                     dni TEXT NOT NULL,
                                                     nombre TEXT NOT NULL,
                                                     tipo TEXT NOT NULL,
                                                     sexo TEXT NOT NULL,
                                                     raza TEXT NOT NULL)
                                        """)
            cursor.execute("select id from mascotas")

            self.entryIdM.clear()
            self.entryIdE.clear()
            for rexistro in cursor.fetchall():
                self.entryIdM.append([rexistro[0]])
                self.entryIdE.append([rexistro[0]])

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.aux = country

    def on_country_combo_changed2(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.auxMod = country
            bbdd = dbapi.connect("BaseClientes.dat")
            cursor = bbdd.cursor()

            try:
                cursor.execute("""CREATE TABLE IF NOT EXISTS mascotas
                                                                    (id TEXT PRIMARY KEY,
                                                                     dni TEXT NOT NULL,
                                                                     nombre TEXT NOT NULL,
                                                                     tipo TEXT NOT NULL,
                                                                     sexo TEXT NOT NULL,
                                                                     raza TEXT NOT NULL)
                                                        """)

                cursor.execute("select * from mascotas where id = '" + self.auxMod + "'")

                for rexistro in cursor.fetchall():
                    self.entryNombreM.set_text(rexistro[2])
                    self.entryTipoM.set_text(rexistro[3])
                    self.entryRazaM.set_text(rexistro[5])

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()

    def on_country_combo_changed3(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.auxEliminar = country

    def on_crear_mascota(self, button):

        Id = self.entryId.get_text()
        Dni = self.aux
        Nombre = self.entryNombre.get_text()
        Tipo = self.entryTipo.get_text()

        if (self.sexoH.get_active()):
            Sexo = "Macho"
        else:
            Sexo = "Hembra"

        Raza = self.entryRaza.get_text()


        if(Id != "" and Dni != "" and Nombre != "" and Tipo != "" and Sexo != "" and Raza != ""):

            bbdd = dbapi.connect("BaseClientes.dat")
            cursor = bbdd.cursor()

            try:

                cursor.execute("""CREATE TABLE IF NOT EXISTS mascotas
                                        (id TEXT PRIMARY KEY,
                                         dni TEXT NOT NULL,
                                         nombre TEXT NOT NULL,
                                         tipo TEXT NOT NULL,
                                         sexo TEXT NOT NULL,
                                         raza TEXT NOT NULL)
                            """)

                sql = "INSERT INTO mascotas (id,dni,nombre,tipo,sexo,raza) VALUES (?, ?, ?, ?, ?, ?)"
                parametros = (Id, Dni, Nombre, Tipo, Sexo, Raza)

                cursor.execute(sql, parametros)

                bbdd.commit()

                cursor.execute("select * from mascotas")

                for rexistro in cursor.fetchall():
                    print(rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5])

                self.cargar_id_mascota()

            except dbapi.OperationalError as errorOperacion:

                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                self.entryId.set_text("Inserta otro id diferente")
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear la mascota")

    def on_modificar_mascota(self, button):

        Id = self.auxMod
        Nombre = self.entryNombreM.get_text()
        Tipo = self.entryTipoM.get_text()

        if (self.sexoHM.get_active()):
            Sexo = "Macho"
        else:
            Sexo = "Hembra"

        Raza = self.entryRazaM.get_text()

        if (Nombre != "" and Tipo != "" and Sexo != "" and Raza != ""):

            bbdd = dbapi.connect("BaseClientes.dat")
            cursor = bbdd.cursor()

            try:
                cursor.execute("""CREATE TABLE IF NOT EXISTS mascotas
                                                        (id TEXT PRIMARY KEY,
                                                         dni TEXT NOT NULL,
                                                         nombre TEXT NOT NULL,
                                                         tipo TEXT NOT NULL,
                                                         sexo TEXT NOT NULL,
                                                         raza TEXT NOT NULL)
                                            """)

                sql = "UPDATE mascotas SET nombre = ?, tipo = ?, sexo = ?, raza = ? where id = ?"
                parametros = (Nombre, Tipo, Sexo, Raza, Id)

                cursor.execute(sql, parametros)

                bbdd.commit()

                self.cargar_id_mascota()

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear el cliente")

    def on_borrar_mascota(self, button):
        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS mascotas
                                                                    (id TEXT PRIMARY KEY,
                                                                     dni TEXT NOT NULL,
                                                                     nombre TEXT NOT NULL,
                                                                     tipo TEXT NOT NULL,
                                                                     sexo TEXT NOT NULL,
                                                                     raza TEXT NOT NULL)
                                                        """)
            sql = "DELETE FROM mascotas where id = '" + self.auxEliminar + "'"

            cursor.execute(sql)
            bbdd.commit()

            self.cargar_id_mascota()
            print("Eliminado")

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"

class MascotasListado(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Listado")
        self.set_default_size(250, 100)
        self.set_border_width(10)

        self.cajaVentana = Gtk.Box(spacing=20)
        self.cajaVentana.set_orientation(Gtk.Orientation.VERTICAL)

        self.add(self.cajaVentana)

        ##Tabla Clientes
        self.columnas = ["Dni", "Nombre", "Apellidos", "Sexo", "Direccion", "Telefono", "Email"]
        self.modelo = Gtk.ListStore(str, str, str, str, str, str, str)
        self.axenda = []
        self.vista = Gtk.TreeView(model=self.modelo)

        self.vista.get_selection().connect("changed", self.on_changed)

        self.nombre = Gtk.Label("Tabla clientes")
        self.cajaVentana.add(self.nombre)
        self.cajaVentana.add(self.vista)

        ##Tabla Clientes
        self.columnasM = ["Id", "Dni", "Nombre", "Tipo de animal", "Sexo", "Raza"]
        self.modeloM = Gtk.ListStore(str, str, str, str, str, str)
        self.axendaM = []
        self.vistaM = Gtk.TreeView(model=self.modeloM)
        self.auxiliar = True

        self.nombreM = Gtk.Label("Tabla mascotas ")
        self.cajaVentana.add(self.nombreM)
        self.cajaVentana.add(self.vistaM)


        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                        (dni TEXT PRIMARY KEY, 
                         nombre TEXT NOT NULL, 
                         apellidos TEXT NOT NULL,
                         sexo TEXT NOT NULL,
                         direccion TEXT NOT NULL, 
                         telefono TEXT NOT NULL,
                         email TEXT NOT NULL)
            """)

            cursor.execute("select * from clientes")

            for rexistro in cursor.fetchall():
                self.axenda.append([rexistro[0] , rexistro[1] , rexistro[2] , rexistro[3] , rexistro[4] , rexistro[5] , rexistro[6]])

            for elemento in self.axenda:
                self.modelo.append(elemento)

            for i in range(len(self.columnas)):
                    celda = Gtk.CellRendererText()
                    self.columna = Gtk.TreeViewColumn(self.columnas[i], celda, text=i)
                    self.vista.append_column(self.columna)

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def on_changed(self, selection):

        (model, iter) = selection.get_selected()

        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS mascotas
                                                    (id TEXT PRIMARY KEY,
                                                     dni TEXT NOT NULL,
                                                     nombre TEXT NOT NULL,
                                                     tipo TEXT NOT NULL,
                                                     sexo TEXT NOT NULL,
                                                     raza TEXT NOT NULL)
                                        """)
            cursor.execute("select * from mascotas where dni = '" + model[iter][0] + "'")

            self.axendaM.clear()
            for rexistro in cursor.fetchall():
                self.axendaM.append([rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5]])

            self.modeloM.clear()
            for elemento in self.axendaM:
                self.modeloM.append(elemento)

            if (self.auxiliar):
                for i in range(len(self.columnasM)):
                    celda = Gtk.CellRendererText()
                    self.columnaM = Gtk.TreeViewColumn(self.columnasM[i], celda, text=i)
                    self.vistaM.append_column(self.columnaM)
                    self.auxiliar = False

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()
        return True

class MascotasClientes(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clientes")

        # Declaracion de la caja principal
        self.caixaventana = Gtk.Box(spacing=10)
        self.caixaventana.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventana.set_margin_left(10)
        self.caixaventana.set_margin_right(10)
        self.caixaventana.set_size_request(400, 300)

        self.add(self.caixaventana)

        self.frameDere = Gtk.Frame()
        self.frameDere.set_label("Creacion de nuevo cliente")

        # Declaracion caja insertar
        self.caixaventanaDerecha = Gtk.Box(spacing=10)
        self.caixaventanaDerecha.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.caixaventanaDerecha1 = Gtk.Box(spacing=10)
        self.caixaventanaDerecha1.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaDerecha.add(self.caixaventanaDerecha1)

        self.caixaventanaDerecha2 = Gtk.Box(spacing=10)
        self.caixaventanaDerecha2.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaDerecha.add(self.caixaventanaDerecha2)

        self.frameDere.add(self.caixaventanaDerecha)
        self.caixaventana.add(self.frameDere)

        self.etiquetaDni = Gtk.Label("Dni")
        self.entryDni = Gtk.Entry()

        self.etiquetaNombre = Gtk.Label("Nombre")
        self.entryNombre = Gtk.Entry()

        self.etiquetaApellidos = Gtk.Label("Apellidos")
        self.entryApellidos = Gtk.Entry()

        self.etiquetaSexo = Gtk.Label("Sexo")

        self.cajaRadio = Gtk.Box(spacing=10)
        self.cajaRadio.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoH = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.sexoH.connect("toggled", self.on_button_toggled, "1")

        self.sexoM = Gtk.RadioButton.new_from_widget(self.sexoH)
        self.sexoM.set_label("Mujer")
        self.sexoM.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadio.add(self.sexoH)
        self.cajaRadio.add(self.sexoM)

        self.etiquetaDireccion = Gtk.Label("Direccion")
        self.entryDireccion = Gtk.Entry()

        self.etiquetaTelefono = Gtk.Label("Telefono")
        self.entryTelefono = Gtk.Entry()

        self.etiquetaEmail = Gtk.Label("Email")
        self.entryEmail = Gtk.Entry()

        self.botonCrear = Gtk.Button("Crear cliente")

        self.caixaventanaDerecha1.add(self.etiquetaDni)
        self.caixaventanaDerecha1.add(self.entryDni)
        self.caixaventanaDerecha1.add(self.etiquetaNombre)
        self.caixaventanaDerecha1.add(self.entryNombre)
        self.caixaventanaDerecha1.add(self.etiquetaApellidos)
        self.caixaventanaDerecha1.add(self.entryApellidos)
        self.caixaventanaDerecha1.add(self.etiquetaSexo)

        self.caixaventanaDerecha1.add(self.cajaRadio)

        self.caixaventanaDerecha2.add(self.etiquetaDireccion)
        self.caixaventanaDerecha2.add(self.entryDireccion)
        self.caixaventanaDerecha2.add(self.etiquetaTelefono)
        self.caixaventanaDerecha2.add(self.entryTelefono)
        self.caixaventanaDerecha2.add(self.etiquetaEmail)
        self.caixaventanaDerecha2.add(self.entryEmail)

        self.caixaventanaDerecha2.add(self.botonCrear)

        self.botonCrear.connect("clicked", self.on_crear_cliente)

        ##########################################################

        self.frameCentro = Gtk.Frame()
        self.frameCentro.set_label("Modificacion de un cliente")

        # Declaracion caja modificar
        self.caixaventanaCentro = Gtk.Box(spacing=9)
        self.caixaventanaCentro.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.caixaventanaCentro1 = Gtk.Box(spacing=10)
        self.caixaventanaCentro1.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaCentro.add(self.caixaventanaCentro1)

        self.caixaventanaCentro2 = Gtk.Box(spacing=10)
        self.caixaventanaCentro2.set_orientation(Gtk.Orientation.VERTICAL)
        self.caixaventanaCentro.add(self.caixaventanaCentro2)

        self.frameCentro.add(self.caixaventanaCentro)
        self.caixaventana.add(self.frameCentro)

        ##
        self.etiquetaDniM = Gtk.Label("Dni")
        self.entryDniM = Gtk.ListStore(str)

        self.country_combo = Gtk.ComboBox.new_with_model(self.entryDniM)

        self.aux = self.country_combo.connect("changed", self.on_country_combo_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.country_combo.pack_start(self.renderer_text, True)
        self.country_combo.add_attribute(self.renderer_text, "text", 0)
        ##


        self.etiquetaNombreM = Gtk.Label("Nombre")
        self.entryNombreM = Gtk.Entry()

        self.etiquetaApellidosM = Gtk.Label("Apellidos")
        self.entryApellidosM = Gtk.Entry()

        self.etiquetaSexoM = Gtk.Label("Sexo")

        self.cajaRadioM = Gtk.Box(spacing=10)
        self.cajaRadioM.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.sexoHM = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.sexoHM.connect("toggled", self.on_button_toggled, "1")

        self.sexoMM = Gtk.RadioButton.new_from_widget(self.sexoHM)
        self.sexoMM.set_label("Mujer")
        self.sexoMM.connect("toggled", self.on_button_toggled, "2")

        self.cajaRadioM.add(self.sexoHM)
        self.cajaRadioM.add(self.sexoMM)

        self.etiquetaDireccionM = Gtk.Label("Direccion")
        self.entryDireccionM = Gtk.Entry()

        self.etiquetaTelefonoM = Gtk.Label("Telefono")
        self.entryTelefonoM = Gtk.Entry()

        self.etiquetaEmailM = Gtk.Label("Email")
        self.entryEmailM = Gtk.Entry()

        self.botonM = Gtk.Button("Modificar cliente")

        self.caixaventanaCentro1.add(self.etiquetaDniM)
        self.caixaventanaCentro1.add(self.country_combo)
        self.caixaventanaCentro1.add(self.etiquetaNombreM)
        self.caixaventanaCentro1.add(self.entryNombreM)
        self.caixaventanaCentro1.add(self.etiquetaApellidosM)
        self.caixaventanaCentro1.add(self.entryApellidosM)
        self.caixaventanaCentro1.add(self.etiquetaSexoM)

        self.caixaventanaCentro1.add(self.cajaRadioM)

        self.caixaventanaCentro2.add(self.etiquetaDireccionM)
        self.caixaventanaCentro2.add(self.entryDireccionM)
        self.caixaventanaCentro2.add(self.etiquetaTelefonoM)
        self.caixaventanaCentro2.add(self.entryTelefonoM)
        self.caixaventanaCentro2.add(self.etiquetaEmailM)
        self.caixaventanaCentro2.add(self.entryEmailM)

        self.caixaventanaCentro2.add(self.botonM)

        self.botonM.connect("clicked", self.on_modificar_cliente)

        #####################
        # Declaracion caja eliminar
        self.caixaventanaIzq = Gtk.Box(spacing=9)
        self.caixaventanaIzq.set_orientation(Gtk.Orientation.HORIZONTAL)

        self.frameIzq = Gtk.Frame()
        self.frameIzq.set_label("Eliminacion de un cliente")
        self.frameIzq.add(self.caixaventanaIzq)
        self.caixaventana.add(self.frameIzq)

        ##
        self.etiquetaDniE = Gtk.Label("Dni")
        self.entryDniE = Gtk.ListStore(str)
        self.cargar_dni_cliente()

        self.country_comboM = Gtk.ComboBox.new_with_model(self.entryDniE)

        self.aux2 = self.country_comboM.connect("changed", self.on_country_combo_changed2)
        self.renderer_textM = Gtk.CellRendererText()
        self.country_comboM.pack_start(self.renderer_textM, True)
        self.country_comboM.add_attribute(self.renderer_textM, "text", 0)

        self.botonBorrar = Gtk.Button("Borrar cliente")

        self.caixaventanaIzq.add(self.etiquetaDniE)
        self.caixaventanaIzq.add(self.country_comboM)

        self.caixaventanaIzq.add(self.botonBorrar)


        self.botonBorrar.connect("clicked", self.on_borrar_cliente)


        ##



    def cargar_dni_cliente(self):
        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()

        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                                    (dni TEXT PRIMARY KEY, 
                                     nombre TEXT NOT NULL, 
                                     apellidos TEXT NOT NULL,
                                     sexo TEXT NOT NULL,
                                     direccion TEXT NOT NULL, 
                                     telefono TEXT NOT NULL,
                                     email TEXT NOT NULL)
                        """)

            cursor.execute("select dni from clientes")
            self.entryDniM.clear()
            self.entryDniE.clear()
            for rexistro in cursor.fetchall():
                print([rexistro[0]])
                self.entryDniM.append([rexistro[0]])
                self.entryDniE.append([rexistro[0]])


        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.aux = country

            bbdd = dbapi.connect("BaseClientes.dat")
            cursor = bbdd.cursor()
            try:
                cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                                        (dni TEXT PRIMARY KEY, 
                                         nombre TEXT NOT NULL, 
                                         apellidos TEXT NOT NULL,
                                         sexo TEXT NOT NULL,
                                         direccion TEXT NOT NULL, 
                                         telefono TEXT NOT NULL,
                                         email TEXT NOT NULL)
                            """)
                sql = "select * from clientes where dni = '" + country + "'"

                cursor.execute(sql)

                for rexistro in cursor.fetchall():
                    self.entryNombreM.set_text(rexistro[1])
                    self.entryApellidosM.set_text(rexistro[2])
                    self.entryDireccionM.set_text(rexistro[4])
                    self.entryTelefonoM.set_text(rexistro[5])
                    self.entryEmailM.set_text(rexistro[6])

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()

    def on_country_combo_changed2(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            country = model[tree_iter][0]

            self.aux2 = country

    def on_crear_cliente(self, button):

        Dni = self.entryDni.get_text()
        Nombre = self.entryNombre.get_text()
        Apellidos = self.entryApellidos.get_text()

        if (self.sexoH.get_active()):
            Sexo = "H"
        else:
            Sexo = "M"

        Direccion = self.entryDireccion.get_text()
        Telefono = self.entryTelefono.get_text()
        Email = self.entryEmail.get_text()

        if (Dni != "" and Nombre != "" and Apellidos != "" and Sexo != "" and Direccion != "" and Telefono != "" and Email != ""):

            bbdd = dbapi.connect("BaseClientes.dat")
            cursor = bbdd.cursor()

            try:
                cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                                        (dni TEXT PRIMARY KEY, 
                                         nombre TEXT NOT NULL, 
                                         apellidos TEXT NOT NULL,
                                         sexo TEXT NOT NULL,
                                         direccion TEXT NOT NULL, 
                                         telefono TEXT NOT NULL,
                                         email TEXT NOT NULL)
                            """)

                # Crear Cliente

                sql = "INSERT INTO clientes (dni,nombre,apellidos,sexo,direccion,telefono,email) VALUES (?, ?, ?, ?, ?, ?, ?)"
                parametros = (Dni, Nombre, Apellidos, Sexo, Direccion, Telefono, Email)

                cursor.execute(sql, parametros)

                bbdd.commit()

                cursor.execute("select * from clientes")

                for rexistro in cursor.fetchall():
                    print(rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5], rexistro[6])

                self.cargar_dni_cliente()

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear el cliente")

    def on_modificar_cliente(self, button):

        Dni = self.aux
        Nombre = self.entryNombreM.get_text()
        Apellidos = self.entryApellidosM.get_text()

        if (self.sexoHM.get_active()):
            Sexo = "H"
        else:
            Sexo = "M"

        Direccion = self.entryDireccionM.get_text()
        Telefono = self.entryTelefonoM.get_text()
        Email = self.entryEmailM.get_text()

        if (Dni != "" and Nombre != "" and Apellidos != "" and Sexo != "" and Direccion != "" and Telefono != "" and Email != ""):

            bbdd = dbapi.connect("BaseClientes.dat")
            cursor = bbdd.cursor()

            try:
                cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                                        (dni TEXT PRIMARY KEY, 
                                         nombre TEXT NOT NULL, 
                                         apellidos TEXT NOT NULL,
                                         sexo TEXT NOT NULL,
                                         direccion TEXT NOT NULL, 
                                         telefono TEXT NOT NULL,
                                         email TEXT NOT NULL)
                            """)

                sql = "UPDATE clientes SET nombre = ?, apellidos = ?, sexo = ?, direccion = ?, telefono = ?, email = ? where dni = ?"
                parametros = (Nombre, Apellidos, Sexo, Direccion, Telefono, Email, Dni)

                cursor.execute(sql, parametros)

                bbdd.commit()

                cursor.execute("select * from clientes")

                for rexistro in cursor.fetchall():
                    print(rexistro[0], rexistro[1], rexistro[2], rexistro[3], rexistro[4], rexistro[5], rexistro[6])

                self.cargar_dni_cliente()

            except dbapi.OperationalError as errorOperacion:
                print("Se ha producido un error ")

            except dbapi.DatabaseError as errorBaseDatos:
                print("tratamento doutra excepcion")

            finally:
                cursor.close()
                bbdd.close()
        else:
            print("Faltan valores para crear el cliente")

    def on_borrar_cliente(self, button):
        bbdd = dbapi.connect("BaseClientes.dat")
        cursor = bbdd.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS clientes
                                    (dni TEXT PRIMARY KEY, 
                                     nombre TEXT NOT NULL, 
                                     apellidos TEXT NOT NULL,
                                     sexo TEXT NOT NULL,
                                     direccion TEXT NOT NULL, 
                                     telefono TEXT NOT NULL,
                                     email TEXT NOT NULL)
                        """)

            sql = "DELETE FROM clientes where dni = '" + self.aux2 + "'"

            cursor.execute(sql)
            bbdd.commit()

            self.cargar_dni_cliente()
            print("Eliminado")

        except dbapi.OperationalError as errorOperacion:
            print("Se ha producido un error ")

        except dbapi.DatabaseError as errorBaseDatos:
            print("tratamento doutra excepcion")

        finally:
            cursor.close()
            bbdd.close()

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"


prin = MascotasPrincipal()
prin.connect("delete-event", Gtk.main_quit)
prin.show_all()
Gtk.main()

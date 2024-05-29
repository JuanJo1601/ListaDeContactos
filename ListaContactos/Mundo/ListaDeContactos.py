from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.contactos = []

    def darTodosLosContactos(self):
        nombresContactos = []
        for contacto in self.contactos:
            nombresContactos.append(contacto.darNombre() +" "+ contacto.darApellido())

    def buscarContactosPalabraClave(self, palabra):
        contactoPalabraClave = []
        for contacto in self.contactos:
            print("Contacto Actual:", contacto.darNombre(), contacto.darApellido())
            print("Palabras Contacto:", contacto.darPalabras())
            print("Palabra clave a buscar:", palabra)
            if palabra in contacto.darPalabras():
                print("La palabra clave es:", palabra, "Esta en las palabras del contacto. ")
                contactoPalabraClave.append(contacto.darNombre() + " " + contacto.darApellido())
            else:
                print("La palabra clave", palabra, "No esta en las palabras del contacto. ")
        print("Contactos encontrados:", contactoPalabraClave)
        return contactoPalabraClave
    
    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        nuevoContacto = Contacto(nombre, apellido, direccion, correo)
        for telefono in telefonos:
            nuevoContacto.agregarTelefono(telefono)
        for palabra in palabras:
            nuevoContacto.agregarPalabra(palabra)
        self.contactos.append(nuevoContacto)

    def eliminarContacto(self, nombre, apellido):
        contactoEliminar = self.buscarContacto(nombre, apellido)
        if contactoEliminar:
            self.contactos.remove(contactoEliminar)
            return True
        else:
            return False

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contactoModificar = self.buscarContacto(nombre, apellido)
        if contactoModificar:
            contactoModificar.cambiarDireccion(direccion)
            contactoModificar.cambiarCorreo(correo)
            self.actualizarTelefonos(telefonos, contactoModificar)
            self.actualizarPalabras(palabras, contactoModificar)
            return True
        else:
            return False

    def actualizarTelefonos(self, telefonos, contacto):
        for telefono in telefonos:
            contacto.agregarTelefono(telefono)

    def actualizarPalabras(self, palabras, contacto):
        for palabra in palabras:
            contacto.agregarPalabra(palabra)

    def metodo1(self):
        pass

    def metodo2(self):
        pass

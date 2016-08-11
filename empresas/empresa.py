#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from sqlempresa import DB

db = DB()
class Principal:

    def main(self):
        Gtk.main()
        return 0

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('listar.glade')

        self.ventana = builder.get_object('ventana')
        self.arbol = builder.get_object('arbol')
        self.lista = builder.get_object('lista_arbol')
        self.buscar = builder.get_object('boxBuscar')
        self.criterio = builder.get_object('criterio')
        self.filtro = builder.get_object('filtro')
        self.statusbar = builder.get_object('statusbar')
        self.on_refrescar_clicked()
        self.ventana.show_all()

    def mostrar_status(self):
        registros = db.contar_registros('empresas')
        buff = "Total de empresas registradas: %s" % registros
        context_id = self.statusbar.get_context_id('Total de empresas registradas: ')
        self.statusbar.push(context_id, buff)

    def lista_ordenada_por_id(self, *args):
        self.cargar_lista(db.consultar_empresas())

    def cargar_lista(self, tupla):
        print(tupla)
        self.lista.clear()
        for f in range(len(tupla)):
            self.lista.append([tupla[f][0], tupla[f][1]])

    # def on_agregar_clicked(self,*args):
        # dlg = DlgUsuario(self.padre, False)
        # dlg.iva_compra.set_text('12,00')
        # dlg.iva_venta.set_text('12,00')
        # dlg.usa_existencia.set_active(True)
        # dlg.foto.set_from_file('')
        # dlg.editando = False
        # response = dlg.dialogo.run()
        # if response == Gtk.RESPONSE_OK:
           # self.on_refrescar_clicked()

    # def on_quitar_clicked(self, *args):
        # Modelo, it = self.arbol.get_selection().get_selected()
        # codigo = Modelo.get_value(it,0)
        # usuario = Modelo.get_value(it,1)

        # if yesno("¿Desea eliminar el usuario <b>%s</b>?\nEsta accion no se puede deshacer\n" % usuario) == Gtk.RESPONSE_YES:
           # db.eliminar_usuario(codigo)
           # Modelo.remove(it)

        # self.on_refrescar_clicked()

    # def on_buscar_clicked(self,*args):
        # self.filtro.set_text('')
        # self.buscar.get_visible()
        # self.buscar.set_visible(True)

        # if self.buscar.get_visible == False:
            # self.criterio.grab_focus()
        # else:
            # self.buscar.set_visible(False)
            # self.criterio.set_visible(False)
            # self.filtro.set_visible(False)

    # def on_criterio_changed(self, *args):
        # self.filtro.set_text('')
        # self.filtro.grab_focus()

    # def on_filtro_changed(self, *args):
        # if self.criterio.get_active() == 0:
            # self.resultado = db.buscar_id_usuario(self.filtro.get_text())

        # elif self.criterio.get_active() == 1:
            # self.resultado = db.buscar_nombre_usuario(self.filtro.get_text())

        # self.cargar_lista(self.resultado)

    def on_refrescar_clicked(self,*args):
        self.mostrar_status()
        self.lista_ordenada_por_id()

    # def on_propiedades_clicked(self,*args):
       # self.on_arbol_row_activated()

    def on_imprimir_clicked(self,*args):
        pass

    def on_cerrar_clicked(self, *args):
        self.on_ventana_destroy()

    def on_ventana_destroy(self, *args):
        self.ventana.destroy()

    # def on_arbol_row_activated(self, *args):
        # (Modelo, f) = self.arbol.get_selection().get_selected()
        # dlg = DlgUsuario(self.frm_padre, False)
        # dlg.editando = True
        # dlg.codigo.set_text(Modelo.get_value(f,0))
        # dlg.codigo.set_editable(False)
        # dlg.nombre.set_text(Modelo.get_value(f,1))
        # dlg.nombre.grab_focus()
        # response = dlg.dialogo.run()
        # if response == Gtk.RESPONSE_OK:
           # self.lista.clear()
           # self.lista_ordenada_por_id()

# class DlgUsuario:

    # def __init__(self, editando = False):
        # builder = Gtk.builder()
        # builder.add_from_file(ruta_ver_editar)
        # builder.connect_signals(self)

        # self.dialogo = builder.get_object("dialogo")
        # self.codigo = builder.get_object("codigo")
        # self.nombre = builder.get_object("nombre")
        # self.editando = editando
        # self.dialogo.show()

    # def cargar_nombre(self, l):
        # self.nombre.set_text(l[0][1])

    # def on_codigo_changed(self, *args):
        # codigo = self.codigo.get_text()
        # l = db.buscar_id_nombre(codigo)
        # if l:
            # self.cargar_nombre(l)
        # else:
            # self.limpiar()

    # def on_guardar_clicked(self, *args):
        # codigo = self.codigo.get_text()
        # nombre = self.nombre.get_text()
        # lleno = self.campos_llenos(codigo, nombre)

        # if lleno == 1 and not self.editando:
            # db.agregar_nombre(codigo, nombre)
            # self.limpiar_todo()
            # self.codigo.grab_focus()

        # if lleno == 1 and self.editando:
            # db.modificar_nombre(codigo, nombre)
            # self.on_cancelar_clicked()

    # def on_cancelar_clicked(self, *args):
        # self.on_dialogo_destroy()

    # def campos_llenos(self, codigo,nombre):
        # ok = 0

        # if codigo == '':
            # print("Debe colocar un codigo a la nombre")
            # return

        # if nombre == '':
            # print("Debe colocar un nombre a la nombre")
            # return

        # if codigo != '' and nombre!='':
            # ok = 1
        # else:
            # ok = 0

        # return ok

    # #Se limpian las cajas de texto
    # def limpiar_todo(self, *args):
        # self.codigo.set_text("")
        # self.nombre.set_text("")

    # def limpiar(self, *args):
        # self.nombre.set_text("")

    # def on_dialogo_destroy(self, *args):
        # self.dialogo.destroy()

if __name__ == '__main__':
    Principal().main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       wprincipal.py
#
#       Este archivo muestra la ventana principal del sistema
#
#       Copyright 2010 Jesús Hómez <jesusenriquehomez@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.




rDir = os.getcwd()
os.chdir(rDir)

class Principal:

    def main(self):
        gtk.main()
        return 0

    def __init__(self):

        builder = gtk.Builder()
        builder.add_from_file("pymeadmin.glade")
        builder.connect_signals(self)

        #Se llaman las objetos del archivo wprincipal.glade
        self.ventana = builder.get_object("ventana")
        self.frm_padre = self.ventana
        self.ventana.show

    def on_item_empresa_activate(self, *args):
        Empresas(self)


    def on_ventana_destroy(self,*args):
        gtk.main_quit(self)

if __name__ == "__main__":
    Principal().main()

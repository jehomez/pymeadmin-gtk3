#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

class DB:

    def conectar(self):
        try:
            self.cnn = sqlite3.connect('/home/jesus/pymeadmin-gtk3/bd/admin.sqlite3')
            self.cursor = self.cnn.cursor()
        except:
            info('No se pudo establecer la conexion')

    def desconectar(self):
        self.cursor.close()
        self.cnn.commit()
        self.cnn.close()

    def contar_registros(self, tabla):
        self.conectar()
        sql = "SELECT count(*) FROM %s" % (tabla)
        self.cursor.execute(sql)
        registros = self.cursor.fetchone()
        self.desconectar()
        return registros

    def agregar_usuario(self, nombre, clave):
        self.conectar()
        a = nombre.upper()
        sql = "INSERT INTO usuarios( nombre, clave) VALUES('%s','%s')" % (nombre, clave)
        self.cursor.execute(sql)
        self.desconectar()

    def modificar_usuario(self, nombre, clave):
        self.conectar()
        sql = "UPDATE usuarios SET clave ='%s' WHERE nombre == '%s'" % (clave, nombre)
        self.cursor.execute(sql)
        self.desconectar()

    def eliminar_usuario(self, codigo):
        self.conectar()
        sql = "DELETE FROM usuarios WHERE usuario_id = '%s'" % (codigo)
        self.cursor.execute(sql)
        self.desconectar()

    def consultar_usuario_por_id(self, codigo):
        self.conectar()
        sql = "SELECT usuario_id, nombre FROM usuarios WHERE usuario_id = '%s'" % (codigo)
        self.cursor.execute(sql)
        nombre = self.cursor.fetchall()
        self.desconectar
        return nombre

    def consultar_usuario_por_nombre_aprox(self, nombre):
        self.conectar()
        nombre = nombre + '%'
        sql = "SELECT usuario_id, nombre FROM usuarios WHERE nombre LIKE '%s' order by nombre" % (nombre)
        self.cursor.execute(sql)
        usuarios = self.cursor.fetchall()
        self.desconectar
        return usuarios

    def consultar_usuario_por_nombre(self, nombre):
        self.conectar()
        sql = "SELECT usuario_id, nombre FROM usuarios WHERE nombre == '%s'" % (nombre)
        self.cursor.execute(sql)
        usuarios = self.cursor.fetchall()
        self.desconectar
        return usuarios

    def consultar_usuarios(self):
        self.conectar()
        sql = "SELECT usuario_id, nombre FROM usuarios ORDER BY usuario_id"
        self.cursor.execute(sql)
        listado = self.cursor.fetchall()
        self.desconectar()
        return listado

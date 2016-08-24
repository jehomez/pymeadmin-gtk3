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

    def agregar_empresa(self, empresa_id, empresa, rif, direccion, web, telefonos, fax, contacto, email):
        self.conectar()
        a = nombre.upper()
        sql = "INSERT INTO empresas(empresa_id, empresa, rif, direccion, web, telefonos, fax, contacto, email) VALUES('%s','%s', '%s','%s','%s','%s','%s','%s')" % (empresa, rif, direccion, web, telefonos, fax, contacto, empresa_id)
        self.cursor.execute(sql)
        self.desconectar()

    def modificar_empresa(self, empresa, rif, direccion, web, telefonos, fax, contacto, email, empresa_id):
        self.conectar()
        sql = "UPDATE empresas SET empresa, rif, direccion, web, telefonos, fax, contacto, email ='%s' WHERE empresa_id == '%s'" % (empresa, rif, direccion, web, telefonos, fax, contacto, email, empresa_id)
        self.cursor.execute(sql)
        self.desconectar()

    def eliminar_empresa(self, codigo):
        self.conectar()
        sql = "DELETE FROM empresas WHERE empresa_id = '%s'" % (codigo)
        self.cursor.execute(sql)
        self.desconectar()

    def consultar_empresa_por_id(self, codigo):
        self.conectar()
        sql = "SELECT empresa_id, empresa, rif, direccion, web, telefonos, fax, contacto, email FROM empresas WHERE empresa_id = '%s'" % (codigo)
        self.cursor.execute(sql)
        nombre = self.cursor.fetchall()
        self.desconectar
        return nombre

    def consultar_empresa_por_nombre_aprox(self, nombre):
        self.conectar()
        nombre = nombre + '%'
        sql = "SELECT empresa_id, empresa, rif, direccion, web, telefonos, fax, contacto, email FROM empresas WHERE empresa LIKE '%s' order by nombre" % (nombre)
        self.cursor.execute(sql)
        empresas = self.cursor.fetchall()
        self.desconectar
        return empresas

    def consultar_empresa_por_nombre(self, nombre):
        self.conectar()
        sql = "SELECT empresa_id, empresa, rif, direccion, web, telefonos, fax, contacto, email FROM empresas WHERE empresa == '%s'" % (nombre)
        self.cursor.execute(sql)
        empresas = self.cursor.fetchall()
        self.desconectar
        return empresas

    def consultar_empresas(self):
        self.conectar()
        sql = "SELECT empresa_id, empresa, rif, direccion, web, telefonos, fax, contacto, email FROM empresas ORDER BY empresa_id"
        self.cursor.execute(sql)
        listado = self.cursor.fetchall()
        self.desconectar()
        return listado

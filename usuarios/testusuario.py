#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlusuario import DB

db = DB()

registros = db.contar_registros('usuarios')

lista = db.consultar_usuarios();

print(registros)
print(lista)

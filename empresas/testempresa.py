#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlusuario import DB



db = DB()
lista = db.consultar_empresas()
print(lista)

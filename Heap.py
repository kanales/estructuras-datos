#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: canales
#

__all__ = ['min_heap']

class Node:
    def __init__(self, key, data, c_funct = None):
        self.key = key
        self.data = data
        self.c_funct = c_funct

    """
    A continuación el listado de funciones de comparacion de nodos.
    Nota: Si se usa una función 'c_funct' personalizada, esta debe cumplir:

        1. Tiene dos parámetros (las dos llaves a comparar)
        2. Debe devolver -1, 0 o 1 en si el resultado es menor igual o mayor
            respectivamente.
    """
    def __lt__(self, other):
        return self.c_funct(self.key, other.key) == -1 if self.c_funct else self.key < other.key

    def __gt__(self, other):
        return self.c_funct(self.key, other.key) == 1 if self.c_funct else self.key > other.key

    def __le__(self, other):
        return self.c_funct(self.key, other.key) <= 0 if self.c_funct else  self.key <= other.key

    def __ge__(self, other):
        return self.c_funct(self.key, other.key) >= 0 if self.c_funct else self.key >= other.key

    def __eq__(self, other):
        return self.c_funct(self.key, other.key) == 0 if self.c_funct else (self.data == other.data and self.key == other.key)

    def __ne__(self, other):
        return self.c_funct(self.key, other.key) != 0 if self.c_funct else (self.data != other.data or self.key == other.key)

    def __str__(self):
        return "key: " + str(self.key) + ", data: " + str(self.data)

class min_heap:
    """
    Clase principal del min_heap.
    """
    def __init__(self, set_max = 0):
        """
        Constructor del min_heap
        :param set_max: Permite establecer un tamaño inicial para el heap.
        """
        self._max = set_max
        self._vec = [None] * set_max
        self._last = -1;

    """
    ===================
    Funciones de ayuda
    ===================
    """

    def _next(self):
        """
        Devuelve la posicion del nodo immediatamente posterior al nodo final.
        Determina el punto de insercion de un nuevo nodo.
        :return:
        """
        return self._last + 1

    def _parent(self, i):
        """
        Devuelve el padre de un nodo.
        :param i: Posicion del nodo
        :return:
        """
        return (i-1) // 2

    def _children(self, i):
        """
        Devuelve las posiciones del los dos hijos asociados a un nodo
        :param i: posicion del nodo 'padre'
        :return:
        """
        return (2 * i + 1), (2 * i + 2)

    def _swap(self, a, b): # Intercambia el contenido de dos posiciones del heap
        temp = self._vec[a]
        self._vec[a] = self._vec[b]
        self._vec[b] = temp

    def _upheap(self, i):
        while i > 0:
            p = self._parent(i)
            if self._vec[i] < self._vec[p]:
                self._swap(i, p)
                i = p
            else: i = 0

    def _downheap(self):
        i = 0 # iniciamos la exploración en el primer elemento del heap
        while i < self._last:
            f,r = self._children(i)

            if r <= self._last:
                m = f if self._vec[f] < self._vec[r] else r
            elif r <= self._last:
                m = f
            else: break # si no tiene hijos se acaba el bucle

            if self._vec[i] > self._vec[m]:
                self._swap(i,m)
                i = m

    """
    ====================
    Métodos principales
    ====================
    """

    def min(self):
        """
        Devuelve el valor mínimo del heap sin modificarlo
        :return:
        """
        return self._vec[0]

    def pop_min(self):
        """
        Elimina y devuelve el elemento más pequeño por llave del heap
        :return:
        """
        tmp = self.min()
        self._last -= 1
        self._downheap()
        return tmp

    def insert(self,key, val):
        """
        Inserta un nuevo elemento en el heap
        :param key:
        :param val:
        :return:
        """
        n = Node(key,val)
        if len(self._vec) < self._next() + 1: self._vec.append(n) # si arribem al final fem append
        else: self._vec[self._next()] = n # si no simplement asociem
        self._last += 1
        self._upheap(self._last)

    def decrease_key(new_key, data):
        """
        Decrementa la llave de un elemento en el heap. Nota: el coste de este algoritmo es de O(n)
        en el peor de los casos (pues contiene una exploracion lineal)
        :param data:
        :return:
        """
        while i < self._last:
            if self._vec[i][1] == data:
                if new_key > self._vec[i][0]:
                    raise Exception('La nueva llave debe ser más pequeña.')
                else:
                    self._vec[i][0] = new_key
                    self._upheap(i)
            else:
                i += 1

    def increase_key(new_key, data):
        """
        Decrementa la llave de un elemento en el heap. Nota: el coste de este algoritmo es de O(n)
        en el peor de los casos (pues contiene una exploracion lineal)
        :param data:
        :return:
        """
        while i < self._last:
            if self._vec[i][1] == data:
                if new_key > self._vec[i][0]:
                    raise Exception('La nueva llave debe ser más grande.')
                else:
                    self._vec[i][0] = new_key
                    self._downheap(i)
            else:
                i += 1

    """
    ======================
    Sobrecarga de métodos
    ======================
    """
    def __str__(self):
        return "[" + ", ".join(str(self._vec[i].data) for i in range(self._last +1)) + "]"

    def __len__(self):
        return self._last + 1

    def __nonzero__(self):
        return self._last == -1

class dict_heap(min_heap):
    def __init__(self, set_max):
        """
        Este heap incluye un diccionario en el que se guardan los valores de los nodos para acceder a su posicion.
        Esto permite que el acceso al nodo 'decrease_key' sea constante~ i por lo tanto el coste total sea log(n)
        :param set_max:
        """
        min_heap.__init__(set_max)
        self.values = {}

    #@overrides
    def _swap(self, a, b):
        temp = self._vec[a]
        self._vec[a] = self._vec[b]
        self._vec[b] = temp

        self.values[self._vect[a].data] = b
        self.values[self._vect[b].data] = a


    #@overrides
    def pop_min(self):
        self.values.pop(min_heap.pop_min(self))

    #@overrides
    def insert(self,key, val):
        self.values[val] = key
        min_heap.insert(key, val)

    def decrease_key(self, new_key, data):
        i = self.values[data]
        if new_key > self._vec[i][0]:
            raise Exception('La nueva llave debe ser más pequeña.')
        else:
            self._vec[i][0] = new_key
            self._upheap(i)

    def increase_key(self,new_key, data):
        i = self.values[data]
        if new_key < self._vec[i][0]:
            raise Exception('La nueva llave debe ser más grande.')
        else:
            self._vec[i][0] = new_key
            self._downheap(i)
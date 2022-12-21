global adjacency_list
adjacency_list = []


class Inventory:
    _node = 0
    _size = 0
    _visit_req = []
    _inventory_req = []

    def __init__(self):
        self.__used = [0] * self._node
        self.__inventory = [0] * self._size

    @classmethod
    def visit_req(
        cls,
        v: "Вершина, для которой задается требование",
        u: "Вершина, которую необходимо посетить",
    ):
        """Задает требование для посещения вершины"""
        if max(v, u) >= cls._node:
            raise IndexError("Такой вершины нет")
        cls._visit_req[v].append(u)

    @classmethod
    def inventory_req(
        cls,
        v: "Вершина, для которой задается требование",
        i: "Индекс предмета, который должен быть у игрока",
    ):
        """Задает требование для посещения вершины"""
        if v >= cls._node:
            raise IndexError("Такой вершины нет")
        if i >= cls._size:
            raise IndexError("Такого предмета нет")
        cls._inventory_req[v].append(i)

    def visit_add(self, v: "Индекс вершины"):
        """Добавляет вершину v в список посещенных"""
        if v >= self._node:
            raise IndexError("Такой вершины нет")
        self.__used[v] += 1

    def visit_check(self, v: "Индекс начальной вершины", u: "Индекс конечной вершины"):
        """Проверка на возможность пройти по ребру v->u учитывая посещенные вершины"""
        if u not in adjacency_list[v]:
            return False
        for i in self._visit_req[u]:
            if not self.__used[i]:
                return False
        return True

    def visit_get(self, v: "Индекс вершины"):
        """Количество посешений вершины v"""
        if v >= self._node:
            raise IndexError("Такой вершины нет")
        return self.__used[v]

    def visit_get_all(self):
        """Список посещенности всех вершин"""
        return self.__used.copy()

    def inventory_add(self, i: "Индекс предмета в инвенторе"):
        """Добавление предмета с индексом i в инвентарь"""
        if i >= self._size:
            raise IndexError("Такого предмета нет")
        self.__inventory[i] += 1

    def inventory_check(
        self, v: "Индекс начальной вершины", u: "Индекс конечной вершины"
    ):
        """Проверка на возможность пройти по ребру v->u учитывая предметы инвенторя"""
        if u not in adjacency_list[v]:
            return False
        if not len(self._inventory_req[u]):
            return True
        for i in self._inventory_req[u]:
            if self.__inventory[i]:
                return True
        return False

    def inventory_get(self, i: "Индекс предмета в инвенторе"):
        """Количество предметов с индексом i"""
        if i >= self._size:
            raise IndexError("Такого предмета нет")
        return self.__inventory[i]

    def inventory_get_all(self):
        """Инвентарь игрока"""
        return self.__inventory.copy()

    def check(self, v: "Индекс начальной вершины", u: "Индекс конечной вершины"):
        """Проверка на возможность пройти по ребру v->u"""
        return self.visit_check(v, u) and self.inventory_check(v, u)


Inventory._node = 50
Inventory._size = 3
Inventory._visit_req = [[] for _ in range(Inventory._node)]
Inventory._inventory_req = [[] for _ in range(Inventory._node)]


def edge(u, v):
    adjacency_list[u].append(v)


def vreq(u, v):
    Inventory.visit_req(u, v)


def ireq(u, j):
    Inventory.inventory_req(u, j)


def go(v, u, i):
    return i.check(v, u)
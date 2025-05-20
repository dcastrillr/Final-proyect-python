from graphviz import Digraph

class GameTreeNode:
    def __init__(self, valor, turno=None):
        self.valor = valor
        self.turno = turno
        self.izquierda = None
        self.derecha = None

class GameTree:
    def __init__(self):
        self.raiz = GameTreeNode("Partida")

    def agregar_turno(self, turno_numero, jugada_blanca, jugada_negra=None):
        nuevo_turno = GameTreeNode(f"Turno {turno_numero}")
        nuevo_turno.izquierda = GameTreeNode(jugada_blanca)
        if jugada_negra:
            nuevo_turno.derecha = GameTreeNode(jugada_negra)

        actual = self.raiz
        while actual.izquierda:
            actual = actual.izquierda
        actual.izquierda = nuevo_turno

    def exportar_graphviz(self, filename="arbol_partida"):
        dot = Digraph(comment='Árbol de la Partida')
        self._agregar_nodos(dot, self.raiz)
        dot.render(filename, format='png', cleanup=True)
        print(f"Árbol exportado como {filename}.png")

    def _agregar_nodos(self, dot, nodo, padre_id=None):
        if nodo is None:
            return

        nodo_id = str(id(nodo))
        dot.node(nodo_id, nodo.valor)

        if padre_id:
            dot.edge(padre_id, nodo_id)

        self._agregar_nodos(dot, nodo.izquierda, nodo_id)
        self._agregar_nodos(dot, nodo.derecha, nodo_id)

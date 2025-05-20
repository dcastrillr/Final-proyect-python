from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QPushButton, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QPixmap
import sys
from parser import Parser
from game_tree import GameTree

class ChessApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validador SAN y Árbol de Ajedrez")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.instrucciones = QLabel("Introduce la partida en notación SAN:")
        layout.addWidget(self.instrucciones)

        self.input = QTextEdit()
        layout.addWidget(self.input)

        self.boton_validar = QPushButton("Validar y Generar Árbol")
        self.boton_validar.clicked.connect(self.validar)
        layout.addWidget(self.boton_validar)

        self.imagen_label = QLabel()
        self.imagen_label.setScaledContents(True)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.imagen_label)
        layout.addWidget(scroll)

        self.setLayout(layout)

    def validar(self):
        texto = self.input.toPlainText()
        parser = Parser()
        errores = parser.analizar_partida(texto)

        if errores:
            mensaje = "\n".join(errores)
            QMessageBox.critical(self, "Errores de Sintaxis", mensaje)
        else:
            arbol = GameTree()
            for linea in texto.strip().split("\n"):
                if not linea.strip():
                    continue
                match = parser.re_turno.match(linea.strip())
                if match:
                    num, blanca, negra = match.groups()
                    arbol.agregar_turno(num, blanca, negra)

            arbol.exportar_graphviz("arbol_salida")
            pixmap = QPixmap("arbol_salida.png")
            self.imagen_label.setPixmap(pixmap)


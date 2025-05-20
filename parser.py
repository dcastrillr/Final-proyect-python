import re

class Parser:
    def __init__(self):
        # Expresiones regulares para cada tipo de jugada según la BNF
        self.re_enroque = re.compile(r"^(O-O(-O)?)$")
        self.re_peon_avance = re.compile(r"^[a-h][1-8](=[QRBN])?[\+#]?$")
        self.re_peon_captura = re.compile(r"^[a-h]x[a-h][1-8](=[QRBN])?[\+#]?$")
        self.re_mov_pieza = re.compile(r"^[KQRBN]([a-h1-8]{0,2})?x?[a-h][1-8](=[QRBN])?[\+#]?$")

        self.re_turno = re.compile(r"^(\d+)\.\s*([^\s]+)\s*([^\s]*)$")

    def validar_jugada(self, jugada: str) -> bool:
        return bool(
            self.re_enroque.match(jugada) or
            self.re_peon_avance.match(jugada) or
            self.re_peon_captura.match(jugada) or
            self.re_mov_pieza.match(jugada)
        )

    def analizar_partida(self, texto: str):
        lineas = texto.strip().split("\n")
        errores = []

        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue

            match = self.re_turno.match(linea)
            if not match:
                errores.append(f"Error de formato en línea: '{linea}'")
                continue

            numero, blanca, negra = match.groups()
            if not self.validar_jugada(blanca):
                errores.append(f"Turno {numero}: jugada blanca inválida '{blanca}'")
            if negra and not self.validar_jugada(negra):
                errores.append(f"Turno {numero}: jugada negra inválida '{negra}'")

        return errores

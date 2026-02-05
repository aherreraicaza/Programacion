#EJERCICIO 1

class Equipo:
    def __init__(self, nome):
        self.__nome = nome
        self.__ganhados = 0
        self.__perdidos = 0
        self.__empatados = 0

    def get_nome(self) -> str:
        return self.__nome

    def get_ganhados(self) -> int:
        return self.__ganhados

    def get_perdidos(self) -> int:
        return self.__perdidos

    def get_empatados(self) -> int:
        return self.__empatados

    def add_victoria(self) -> None:
        self.__ganhados += 1

    def add_perdido(self) -> None:
        self.__perdidos += 1

    def add_empate(self) -> None:
        self.__empatados += 1

    def get_puntos(self) -> int:
        return self.__ganhados * 3 + self.__empatados

    def get_encontros_xogados(self) -> int:
        return self.__ganhados + self.__perdidos + self.__empatados

    def __str__(self):
        return f"{self.__nome} - V: {self.__ganhados} E: {self.__empatados} D: {self.__perdidos} (Puntos: {self.get_puntos()})"
-------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2

class Torneo:
    def __init__(self, nome: str, num_equipos: int):
        self.__nome = nome
        self.__num_max_equipos = num_equipos
        self.__equipos = [None] * num_equipos
        self.__num_equipos = 0

    def get_nome(self) -> str:
        return self.__nome

    def get_equipo(self, nome: str):
        for equipo in self.__equipos:
            if equipo is not None and equipo.get_nome() == nome:
                return equipo
        return None

    def add_equipo(self, equipo) -> bool:
        if self.__num_equipos < self.__num_max_equipos:
            self.__equipos[self.__num_equipos] = equipo
            self.__num_equipos += 1
            return True
        return False

    def get_equipos(self) -> list:
        return self.__equipos

    def get_clasificacion(self) -> list:
        equipos_validos = [e for e in self.__equipos if e is not None]
        equipos_ordenados = sorted(equipos_validos, key=lambda e: e.get_puntos(), reverse=True)
        return equipos_ordenados

    def numero_equipos(self) -> int:
        return self.__num_equipos
--------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3
class TorneoXestor:
    def __init__(self, nome_torneo: str, num_max_equipos: int):
        self.__nome_torneo = nome_torneo
        self.__num_max_equipos = num_max_equipos
        self.__equipos = [None] * num_max_equipos
        self.__num_equipos = 0

    def rexistrar_equipo(self, equipo) -> bool:
        if self.__num_equipos < self.__num_max_equipos:
            self.__equipos[self.__num_equipos] = equipo
            self.__num_equipos += 1
            return True
        return False

    def rexistrar_resultado(self, nome_equipo: str, resultado: str):
        equipo = self.consultar_equipo(nome_equipo)
        if equipo is None:
            return False

        if resultado == "V":
            equipo.add_victoria()
        elif resultado == "E":
            equipo.add_empate()
        elif resultado == "D":
            equipo.add_perdido()
        else:
            return False

        return True

    def mostrar_clasificacion(self):
        equipos_validos = [e for e in self.__equipos if e is not None]
        equipos_ordenados = sorted(equipos_validos, key=lambda e: e.get_puntos(), reverse=True)

        for e in equipos_ordenados:
            print(e)

    def consultar_equipo(self, nome: str):
        for equipo in self.__equipos:
            if equipo is not None and equipo.get_nome() == nome:
                return equipo
        return None

    def estadisticas_torneo(self):
        total_partidos = 0
        total_goles = 0
        equipos_validos = [e for e in self.__equipos if e is not None]

        for e in equipos_validos:
            total_partidos += e.get_encontros_xogados()

        print(f"Torneo: {self.__nome_torneo}")
        print(f"Equipos inscritos: {self.__num_equipos}")
        print(f"Partidos xogados no total: {total_partidos}")

    def sair(self):
        print("Saíndo do xestor do torneo...")
-------------------------------------------------------------------------------------------
#EJERCICIO RESUELTOS POR MI

#EJERCICIO 1
class Equipo:
    def __init__(self, nome):
        self.__nome = nome
        self.__ganhados = 0
        self.__perdidos = 0
        self.__empatados = 0
        self.puntos = []

    def get_nome(self) -> str:
        return self.__nome

    def get_ganhados(self) -> int:
        return self.__ganhados

    def get_perdidos(self) -> int:
        return self.__perdidos

    def get_empatados(self) -> int:
        return self.__empatados

    def add_victoria(self) -> None:
        self.__ganhados += 1

    def add_perdido(self) -> None:
        self.__perdidos += 1

    def add_empate(self) -> None:
        self.__empatados += 1

    def get_puntos(self) -> int:
            if self.__ganhados == 1:
                self.puntos +=3
            if self.__perdidos == 1:
                self.puntos += 0
            if self.__empatados == 1:
                self.puntos += 1

    def get_encontros_xogados(self) -> int:
        return self.__ganhados + self.__perdidos + self.__empatados

    def __str__(self):
        return f"{self.__nome} - V: {self.__ganhados} E: {self.__empatados} D: {self.__perdidos} (Puntos: {self.puntos})"

celta = Equipo("celta")
----------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2
class Torneo:
    def __init__(self, nome, num_equipos):
        self.__nome = nome
        self.__equipos = [None]* num_equipos
        self.__num_max_equipos = num_equipos
        self.__num_equipos = 0
        self.__equipos = []

    def get_nome(self) -> str:
        return self.__nome
    def get_equipo(self, nome: str) -> Equipo | None:
        for equipo in self.__equipos:
            if equipo is not None and equipo.get_nome() == nome:
                return equipo
        return None

    def add_equipo(self, equipo: Equipo) -> int:
        if self.__num_equipos < self.__max_equipos:
            self.__equipos[self.__num_equipos] = equipo
            self.__num_equipos += 1
            return True
        return False

    def get_equipos(self) -> list[Equipo | None]:
        return self.__equipos

    def get_clasificacion(self) -> list[Equipo]:
        for i in range(self.__equipos):
            if i < self.__equipos[1]:


    def numero_equipos(self) -> int:
        return self.__num_equipos
-------------------------------------------------------------------------------------------
#EJERCICIO 3
class TorneoXestor:
    def __init__(self, nome_torneo, num_max_equipos):
        self.__nome_torneo = nome_torneo
        self.__num_max_equipos = num_max_equipos
        self.__nome_equipos = []

    def rexistrar_resultado(self):
        self.__nome_equipos

    def mostrar_clasificacion(self):

    def consultar_equipo(self):

    def estadisticas_torneo(self):
        self.

    def sair(self):


    :)





class Automata:

    def __init__(self, data) -> None:
        self.states = data["states"]
        self.alpha = data["alpha"]
        self.startState = data["startState"]
        self.endStates = data["endStates"]
        self.currentState = data["startState"]

    def validar_cadena(self, cadena):
        for i in range(len(cadena)):
            caracter = cadena[i]
            if self.validar_existencia_caracter_alfabeto(caracter, self.alpha):
                estado = self.buscar_estado_conectado(self.currentState, self.states)
                estado_a_conectar = self.buscar_caracter_conexiones(caracter, estado["connections"])
                if estado_a_conectar:
                    self.currentState = estado_a_conectar
                    if i == len(cadena) - 1:
                        if self.buscar_estado_final(self.currentState, self.endStates):
                            return True
                else:
                    print("No hay un estado al cual conectar por el caracter ingresado")
                    return False
            else:
                print("El caracter no existe en el alfabeto")
                return False
        print("No cayó en ningún if")
        return False

    def restaurar_automata(self):
        self.currentState = self.startState

    # Función para validar que el caracter de la cadena ingresada exista en el alfabeto
    # Devuelve True si encuentra el caracter como símbolo del alfabeto
    def validar_existencia_caracter_alfabeto(self, caracter, alfabeto):
        # Usamos 'in' para verificar la existencia del caracter en el alfabeto
        if caracter in alfabeto:
            return True
        print("El caracter ingresado no existe en el alfabeto")
        return False

    # Función para validar que el estado conectado a conectar exista en los estados declarados
    # Devuelve True si el estado a conectar es encontrado en los estados declarados
    def validar_existencia_estado_conectado(self, estado_conectado_nombre, estados_con_conexion):
        # Usamos next() para buscar el estado a conectar en el array de estados
        if any(estado["name"] == estado_conectado_nombre for estado in estados_con_conexion):
            return True
        print("El estado a conectar ingresado no existe en los estados")
        return False

    # Función para buscar el estado a conectar
    def buscar_estado_conectado(self, estado_conectado_nombre, estados_con_conexion):
        for estado in estados_con_conexion:
            if estado["name"] == estado_conectado_nombre:
                return estado
        print("El estado a conectar no existe en los estados declarados")

    # Función para buscar si el estado actual está en el array de estados finales
    def buscar_estado_final(self, estado_final_nombre, estados_finales):
        # Usamos 'in' para verificar la existencia del estado final en los estados finales
        if estado_final_nombre in estados_finales:
            return True
        print("El estado actual no se encuentra como un estado final")
        return False

    # Función para buscar el caracter como conector en las conexiones
    def buscar_caracter_conexiones(self, caracter, conexiones):
        for connection in conexiones:
            for conector in connection["conector"]:
                if caracter == conector:
                    return connection["to"]
        return False

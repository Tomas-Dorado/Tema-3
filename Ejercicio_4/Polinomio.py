class PolinomioMagico:
    def __init__(self, coeficientes):
        """
        Inicializa un polinomio mágico.
        :param coeficientes: Diccionario donde las claves son los exponentes y los valores son los coeficientes.
        """
        self.coeficientes = coeficientes

    def __str__(self):
        """
        Representación en cadena del polinomio.
        """
        terminos = []
        for exp, coef in sorted(self.coeficientes.items(), reverse=True):
            if coef != 0:
                terminos.append(f"{coef}x^{exp}" if exp != 0 else f"{coef}")
        return " + ".join(terminos) if terminos else "0"

    def restar(self, otro):
        """
        Resta otro polinomio de este polinomio.
        :param otro: PolinomioMagico a restar.
        :return: Nuevo PolinomioMagico con el resultado.
        """
        resultado = self.coeficientes.copy()
        for exp, coef in otro.coeficientes.items():
            resultado[exp] = resultado.get(exp, 0) - coef
        return PolinomioMagico(resultado)

    def dividir(self, otro):
        """
        Divide este polinomio por otro polinomio.
        :param otro: PolinomioMagico divisor.
        :return: Tupla con (cociente, residuo) como PolinomioMagico.
        """
        cociente = {}
        residuo = self.coeficientes.copy()

        while residuo and max(residuo.keys()) >= max(otro.coeficientes.keys()):
            exp_residuo = max(residuo.keys())
            exp_otro = max(otro.coeficientes.keys())
            coef_residuo = residuo[exp_residuo]
            coef_otro = otro.coeficientes[exp_otro]

            nuevo_exp = exp_residuo - exp_otro
            nuevo_coef = coef_residuo / coef_otro
            cociente[nuevo_exp] = nuevo_coef

            # Resta el término correspondiente del divisor multiplicado por el nuevo término del cociente
            for exp, coef in otro.coeficientes.items():
                residuo[exp + nuevo_exp] = residuo.get(exp + nuevo_exp, 0) - coef * nuevo_coef
                if residuo[exp + nuevo_exp] == 0:
                    del residuo[exp + nuevo_exp]

        return PolinomioMagico(cociente), PolinomioMagico(residuo)

    def eliminar_termino(self, exponente):
        """
        Elimina un término del polinomio.
        :param exponente: Exponente del término a eliminar.
        """
        if exponente in self.coeficientes:
            del self.coeficientes[exponente]

    def existe_termino(self, exponente):
        """
        Determina si un término específico existe en el polinomio.
        :param exponente: Exponente del término a buscar.
        :return: True si existe, False en caso contrario.
        """
        return exponente in self.coeficientes
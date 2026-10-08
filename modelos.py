
# CLASES BASE Y SUBCLASES

class Actividad:
    def __init__(self, fecha, registrado_por):
        self.__fecha = fecha
        self.__registrado_por = registrado_por

    @property
    def fecha(self):
        return self.__fecha

    @property
    def registrado_por(self):
        return self.__registrado_por

    def calcular_huella_co2(self):
        raise NotImplementedError("Las subclases deben implementar el método calcular_huella_co2()")


class ConsumoEnergetico(Actividad):
    def __init__(self, fecha, registrado_por, kwh_consumidos, factor_emision=0.438):
        super().__init__(fecha, registrado_por)
        self.__kwh_consumidos = kwh_consumidos
        self.__factor_emision = factor_emision

    def calcular_huella_co2(self):
        return self.__kwh_consumidos * self.__factor_emision


class Transporte(Actividad):
    def __init__(self, fecha, registrado_por, kilometros, factor_emision=0.21):
        super().__init__(fecha, registrado_por)
        self.__kilometros = kilometros
        self.__factor_emision = factor_emision

    def calcular_huella_co2(self):
        return self.__kilometros * self.__factor_emision

class Residuos(Actividad):
    def __init__(self, fecha, registrado_por, kilogramos, factor_emision=0.52):
        super().__init__(fecha, registrado_por)
        self.__kilogramos = kilogramos
        self.__factor_emision = factor_emision

    def calcular_huella_co2(self):
        return self.__kilogramos * self.__factor_emision

class Departamento:
    def __init__(self, nombre, responsable):
        self.__nombre = nombre
        self.__responsable = responsable
        self.__actividades = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def responsable(self):
        return self.__responsable

    def agregar_actividad(self, actividad):
        if isinstance(actividad, Actividad):
            self.__actividades.append(actividad)
        else:
            raise TypeError("Debe ser una instancia de Actividad.")

    def obtener_actividades(self):
        return list(self.__actividades)

    def calcular_huella_departamento(self):
        return sum(act.calcular_huella_co2() for act in self.__actividades)

class Empresa:
    def __init__(self, nombre, rfc):
        self.__nombre = nombre
        self.__rfc = rfc
        self.__departamentos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rfc(self):
        return self.__rfc

    def registrar_departamento(self, departamento):
        if isinstance(departamento, Departamento):
            self.__departamentos.append(departamento)
        else:
            raise TypeError("Debe ser una instancia de Departamento.")

    def obtener_departamentos(self):
        return list(self.__departamentos)

    def calcular_huella_total(self):
        return sum(dep.calcular_huella_departamento() for dep in self.__departamentos)
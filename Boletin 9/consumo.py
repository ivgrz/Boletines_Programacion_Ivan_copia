## Boletín 9 - Exercicio 3


class Consumo:
    def __init__(self, km=0.0, litros=0.0, vMed=0.0, pGas=0.0):

        self.km = km
        self.litros = litros
        self.vMed = vMed
        self.pGas = pGas

    def getTempo(self):
        if self.vMed > 0:
            return self.km / self.vMed
        return 0

    def consumoMedio(self):
        if self.km > 0:
            return (self.litros / self.km) * 100
        return 0

    def consumoEuros(self):
        return self.consumoMedio() * self.pGas

    def setKms(self, km):
        self.km = km

    def setLitros(self, litros):
        self.litros = litros

    def setvMed(self, vMed):
        self.vMed = vMed

    def setpGas(self, pGas):
        self.pGas = pGas
    def __str__(self):
        return (f"Kilómetros: {self.km}, Litros: {self.litros}, "
                f"Velocidad media: {self.vMed}, Precio gasolina: {self.pGas}")



if __name__ == "__main__":
    coche = Consumo(km=150, litros=10, vMed=75, pGas=1.7)
    print("Tempo da viaxe:", coche.getTempo(), "horas")
    print("Consumo medio:", coche.consumoMedio(), "L/100km")
    print("Consumo en euros:", coche.consumoEuros(), "€/100km")
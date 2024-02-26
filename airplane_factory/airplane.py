from __future__ import annotations
from abc import ABC, abstractmethod


class IAirplaneFactory():

    @abstractmethod
    def comercial(self) -> comercial:
        pass

    @abstractmethod
    def military(self) -> military:
        pass

class EmbraerFactory(IAirplaneFactory):
    def comercial(self) -> comercial:
        return ejetse2()

    def military(self) -> military:
        return c390()

class BoeingFactory(IAirplaneFactory):
    def comercial(self) -> comercial:
        pass

    def military(self) -> military:
        pass

#Produto abstrato A
class comercial(ABC):
    @abstractmethod
    def exibirInfoComercial(self):
        pass

#Embraer
class ejetse2(comercial):
    def exibirInfoComercial(self):
        print("\n")
        print("--- E-JETS E2 Profit Hunter ---")
        print("Avião Comercial")
        print("Motor: Bimotor")
        print("Fabricante: Embraer")
        print("Passageiros: 80 a 144")
        print("Tripulação: 2(Piloto e Co-Piloto)")
        print("Carga Útil: 15.150kg")
        print("Dimensões: 41m x 10,9m")
        print("\n")
#Boeing
class boeing777(comercial):
    def exibirInfoComercial(self):
        print("\n")
        print("--- Boeing 777 ---")
        print("Avião Comercial")
        print("Motor: Bimotor")
        print("Fabricante: Embraer")
        print("Passageiros: 314 a 550")
        print("Tripulação: 2(Piloto e Co-Piloto)")
        print("Carga Útil: 103.000kg")
        print("Dimensões: 50m x 12m")
        print("\n")




#Produto abstrato B
class military(ABC):
    @abstractmethod
    def exibirInfoMilitary(self):
        pass

#Embraer
class c390(military):
    def exibirInfoComercial(self):
        print("\n")
        print("--- C-390 Millennium ---")
        print("Avião Militar")
        print("Motor: Bimotor")
        print("Fabricante: Embraer")
        print("Passageiros: 64 a 80")
        print("Tripulação: 3(Piloto, Co-Piloto e Engenheiro de Voo)")
        print("Carga Útil: 26.000kg")
        print("Dimensões: 35,2m x 11,8m")
        print("\n")




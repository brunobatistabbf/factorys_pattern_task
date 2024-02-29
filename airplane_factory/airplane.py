from __future__ import annotations
from abc import ABC, abstractmethod

#Solução antes da correção da atividade em aula
#Solução Antiga que fere varios principios SOLID
class IAirplaneFactory():

    @abstractmethod
    def comercial(self) -> comercial:
        pass

    @abstractmethod
    def military(self) -> military:
        pass

class EmbraerFactory(IAirplaneFactory):
    def comercial(self, exec="comercial") -> comercial:
        if(exec == "executivo" or exec == "Executivo"):
            return Phenom100Ex()
        else:
            return Ejetse2()

    def military(self) -> military:
        return C390()

class BoeingFactory(IAirplaneFactory):
    def comercial(self, exec="comercial") -> comercial:
        if(exec == "executivo" or exec == "Executivo"):
            return BBJ()
        else:
            return Boeing777()

    def military(self) -> military:
        return SuperHornet()

#Produto abstrato A
class ComercialAirplane(ABC):
    @abstractmethod
    def exibirInfoComercial(self):
        pass

#Embraer
class Ejetse2(ComercialAirplane):
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

class Phenom100Ex(ComercialAirplane):
    def exibirInfoComercial(self):
        print("\n")
        print("--- Phenom 100 ---")
        print("Avião Executivo")
        print("Motor: Bimotor")
        print("Fabricante: Embraer")
        print("Passageiros: 04 a 07")
        print("Tripulação: 2(Piloto e Co-Piloto)")
        print("Peso: 3.190kg")
        print("Dimensões: 12,80m x 12,30m")
        print("\n")
#Boeing
class Boeing777(ComercialAirplane):
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

class BBJ(ComercialAirplane):
    def exibirInfoComercial(self):
        print("\n")
        print("--- Boeing Business Jet---")
        print("Avião Executivo")
        print("Motor: Bimotor")
        print("Fabricante: Boeing")
        print("Passageiros: 08 a 63")
        print("Tripulação: 4")
        print("Peso: 42.895kg")
        print("Dimensões: 33,63m x 12,57m")
        print("\n")



#Produto abstrato B
class MilitaryComercial(ABC):
    @abstractmethod
    def exibirInfoMilitary(self):
        pass

#Embraer
class C390(MilitaryComercial):
    def exibirInfoMilitary(self):
        print("\n")
        print("--- C-390 Millennium ---")
        print("Avião Militar")
        print("Motor: Bimotor")
        print("Fabricante: Embraer")
        print("Tipo: Transporte Militar")
        print("Passageiros: 64 a 80")
        print("Tripulação: 3(Piloto, Co-Piloto e Engenheiro de Voo)")
        print("Carga Útil: 26.000kg")
        print("Dimensões: 35,2m x 11,8m")
        print("\n")

#Boeing
class SuperHornet(MilitaryComercial):
    def exibirInfoMilitary(self):
        print("\n")
        print("--- F/A-18E/F Super Hornet ---")
        print("Avião Militar")
        print("Motor: Bimotor")
        print("Fabricante: Boeing")
        print("Tipo: Caça Multiproposito")
        print("Passageiros: Sem Passageiros(Padrão)")
        print("Tripulação: 2")
        print("Carga Útil: 26.000kg")
        print("Dimensões: 18,31m x 4,8m")
        print("\n")


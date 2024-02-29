from __future__ import annotations
from abc import ABC, abstractmethod

class IBankFactory():

    @abstractmethod
    def seguroAutomovel(seelf) -> seguroAutomovel:
        pass

    @abstractmethod
    def seguroSaude(self) -> seguroSaude:
        pass

class Bradesco(IBankFactory):

    def seguroAutomovel(self) -> seguroAutomovel:
        return BradescoAuto()
    def seguroSaude(self) -> seguroSaude:
        return BradescoSaude()

    def seguroSaudeEmpresas(self) -> seguroSaudeEmpresas:
        return BradescoSaudeEmpresa()

class ItauUnibanco(IBankFactory):

    def seguroAutomovel(self) -> seguroAutomovel:
        return ItauAuto()

    def seguroSaude(self) -> seguroSaude:
        return ItauSaude()

    def seguroSaudeEmpresas(self) -> seguroSaudeEmpresas:
        return ItauSaudeEmpresa()

class SeguroAutomovelProduto(ABC):
    @abstractmethod
    def exibirInfoSeguroAutomovel(self):
        pass

class BradescoAuto(SeguroAutomovelProduto):
    def exibirInfoSeguroAutomovel(self):
        print("------Seguro de Automovel BRADESCO------")
        print(" > Serviço 24 horas")
        print(" > Cobertura em até 180 dias")
        print(" > Seguradoras conveniadas")
        print(" > Cobertura para KIT GÁS")
        print(" > Seguradoras conveniadas")
        print(" > Quilometragem de reboque ilimitada")
        print(" > Seguradoras conveniadas")
        print(" > Carro reserva por 15 a 30 dias")


class ItauAuto(SeguroAutomovelProduto):
    def exibirInfoSeguroAutomovel(self):
        print("------Seguro de Automovel ITAU UNIBANCO------")
        print(" > Cobertura a terceiros")
        print(" > Guincho até 400km")
        print(" > 24hrs: chaveiro, troca de pneu e auxílio mecânico")
        print(" > Reparos para vidros, farol e retrovisor")
        print(" > Roubo e furto")
        print(" > Alagamento")
        print(" > Incêndio")
        print(" > Carro reserva por 15 a 30 dias")
class SeguroSaudeProduto(ABC):
    @abstractmethod
    def exibirInfoSeguroSaude(self):
        pass

class BradescoSaude(SeguroSaudeProduto):
    def exibirInfoSeguroSaude(self):
        print("BRADESCO SAUDE")
        print(" > Cobertura abrangente")
        print(" > Rede de Provedores Nacional ")
        print(" > Preços Acessiveis")
        print(" > Cobertura de Emergencia Todo Territorio Nacional")
        print(" > Atendimento ao Cliente Personalizado")

class ItauSaude(SeguroSaudeProduto):
    def exibirInfoSeguroSaude(self):
        print("BRADESCO SAUDE")
        print(" > Cobertura em Todo Territorio Nacional")
        print(" > Rede de Provedores Nacional ")
        print(" > Serviços Preventivos")
        print(" > Transparencia e Clareza nas Politicas")
        print(" > Atendimento ao Cliente Personalizado")

class BradescoSaudeEmpresa(SeguroSaudeProduto):
    def exibirInfoSeguroSaude(self):
        print("BRADESCO SAUDE EMPRESAS")
        print(" > A partir de 200 pessoas")
        print(" > Atendimento 24 horas")
        print(" > Vigencia de 24 meses ")
class ItauSaudeEmpresa(SeguroSaudeProduto):
    def exibirInfoSeguroSaude(self):
        print("ITAU SAUDE EMPRESAS")
        print(" > A partir de 69 pessoas")
        print(" > Vigencia de 24 meses ")

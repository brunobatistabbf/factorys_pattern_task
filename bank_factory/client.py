from bank_factory.bank import IBankFactory, Bradesco, ItauUnibanco


def Client(factory: IBankFactory) -> None:
    if factory == Bradesco:
        seguroAutomovel = factory.seguroAutomovel()
        seguroSaude = factory.seguroSaude()
        seguroSaudeEmpresa = factory.seguroSaudeEmpresas()
        print(f"{seguroAutomovel.exibirInfoSeguroAutomovel()}")
        print(f"{seguroSaude.exibirInfoSeguroSaude()}")
        print(f"{seguroSaudeEmpresa.exibirInfoSeguroSaude()}")
    else:
        seguroAutomovel = factory.seguroAutomovel()
        seguroSaude = factory.seguroSaude()
        seguroSaudeEmpresa = factory.seguroSaudeEmpresas()
        print(f"{seguroAutomovel.exibirInfoSeguroAutomovel()}")
        print(f"{seguroSaude.exibirInfoSeguroSaude()}")
        print(f"{seguroSaudeEmpresa.exibirInfoSeguroSaude()}")


if __name__ == '__main__':
   print("----- SISTEMA DE SEGUROS BANCÁRIOS -------")
   print("Seguros Disponiveis: Bradesco")
   Client(Bradesco())
   print("\n")
   print("Seguros Disponiveis: Itau Unibanco")
   Client(ItauUnibanco())


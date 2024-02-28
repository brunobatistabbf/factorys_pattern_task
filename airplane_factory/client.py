from airplane_factory import airplane
from airplane_factory.airplane import IAirplaneFactory, EmbraerFactory, BoeingFactory


def Client(factory: IAirplaneFactory) -> None:
    if factory == EmbraerFactory:
        aircomercial = factory.comercial()
        airmilitary = factory.military()
        airexecutivo = factory.comercial(exec="executivo")
        print(f"{aircomercial.exibirInfoComercial()}")
        print(f"{airexecutivo.exibirInfoComercial()}")
        print(f"{airmilitary.exibirInfoMilitary()}")
    else:
        aircomercial = factory.comercial()
        airmilitary = factory.military()
        airexecutivo = factory.comercial(exec="executivo")
        print(f"{aircomercial.exibirInfoComercial()}")
        print(f"{airexecutivo.exibirInfoComercial()}")
        print(f"{airmilitary.exibirInfoMilitary()}")




if __name__ == '__main__':
    print("-----LEILÃO AERONAVES-----")
    print("Aeronaves Disponiveis: Embraer")
    Client(EmbraerFactory())
    print("\n")
    print("Aeronaves Disponiveis: Boeing")
    Client(BoeingFactory())

class Reserva:
    def __init__(self, dataEntrada, dataSaida, valorDiaria):
        self.dataEntrada = dataEntrada
        self.dataSaida = dataSaida
        self.valorDiaria = valorDiaria

    # 1 - Instancie 3 classes diferentes com no mínimo 3 atributos cada e seus respectivos getters e setters.

    # S E T 

    def set_DataEntrada(self, dataEntrada):
        self.dataEntrada = dataEntrada

    def set_DataSaida(self, dataSaida):
        self.dataSaida = dataSaida    

    def set_ValorDiaria(self, valorDiaria):
        self.valorDiaria = valorDiaria        

    # G E T                 

    def get_DataEntrada(self):
        return self.dataEntrada

    def get_DataSaida(self):
        return self.dataSaida

    def get_ValorDiaria(self):
        return self.valorDiaria    

    # M É T O D O S

    def ConfirmarReserva(self):
        print("\nReserva confirmada com sucesso!!!")

    def FormaPagamento(self, formaPagto):
        print(f"\nA forma desejada para pagamento será através : {formaPagto} .")    

    def Valor(self):
        print(f"O valor da diária é {self.valorDiaria}")   
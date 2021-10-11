from Reserva import Reserva

class Hotel:
    def __init__(self, nomeHotel, localizacao, acomodacoes):
        self.nomeHotel = nomeHotel      
        self.localizacao = localizacao 
        self.acomodacoes = acomodacoes 

    # 1 - Instancie 3 classes diferentes com no mínimo 3 atributos cada e seus respectivos getters e setters.

    # S E T 

    def set_NomeHotel(self, nomeHotel):
        self.nomeHotel = nomeHotel  

    def set_Localizacao(self, localizacao):
        self.localizacao = localizacao    

    def set_Acomodacoes(self, acomodacoes):
        self.acomodacoes = acomodacoes    
      
    # G E T     

    def get_NomeHotel(self):
        return self.nomeHotel

    def get_Localizacao(self):
        return self.localizacao    

    def get_Acomodacoes(self):
        return self.acomodacoes

    # M É T O D O S

    def Abrir(self):
        print(f"\nO Hotel {self.nomeHotel} encontra-se em funcionamento")    

    def Fechar(self):
        print(f"\nO Hotel {self.nomeHotel} encontra-se fechado!")    

    def Endereco(self):
        print(f"O Hotel {self.nomeHotel} encontra-se localizado em {self.localizacao}.")    

    def Estrelas(self, estrelas):
        print(f"\nO Hotel {self.nomeHotel} possui {estrelas} estrelas.")            



              
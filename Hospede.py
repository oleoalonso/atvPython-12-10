class Hospede:
    def __init__(self, nomeHospede, sexoHospede, idadeHospede):
        self.nomeHospede = nomeHospede
        self.sexoHospede = sexoHospede
        self.idadeHospede = idadeHospede

    # 1 - Instancie 3 classes diferentes com no mínimo 3 atributos cada e seus respectivos getters e setters.

    # S E T         

    def set_NomeHospede(self, nomeHospede):
        self.nomeHospede = nomeHospede

    def set_SexoHospede(self, sexoHospede):
        self.sexoHospede = sexoHospede

    def set_IdadeHospede(self, idadeHospede):
        self.idadeHospede = idadeHospede        

    # G E T         

    def get_NomeHospede(self):
        return self.nomeHospede

    def get_SexoHospede(self):
        return self.sexoHospede

    def get_IdadeHospede(self):
        return self.idadeHospede  

    # M É T O D O S 

    def Hospede(self):
        print(f"Seja bem vindo {self.nomeHospede}")

    def Checkin(self):
        print(f"\nCheck-In de {self.nomeHospede} realizado com sucesso!!!")

    def Checkout(self):
        print(f"\nCheck-Out de {self.nomeHospede} realizado com sucesso!!!")

    def Avaliar(self, avaliar):
        print(f"\n{self.nomeHospede}: Avaliou como {avaliar}")    
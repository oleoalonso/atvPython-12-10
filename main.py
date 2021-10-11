from Hotel import Hotel
from Hospede import Hospede
from Reserva import Reserva

hotel = Hotel("Feras", "Centro Histórico", 30)
hospede = Hospede("Maria", "Feminino", 32)
reserva = Reserva("25/12/2021", "05/01/2022", "600")

# H O T E L 
hotel.Abrir()
hotel.Endereco()

# R E S E R V A
reserva.ConfirmarReserva()

# R E S E R V A
print(f"Data de Entrada: {reserva.dataEntrada}")

# H O S P E D E
hospede.Hospede()
print(f"Cliente do sexo: {hospede.sexoHospede}")
print(f"Cliente tem a idade: {hospede.idadeHospede} anos.")

# R E S E R V A
# Método da classe Reserva para receber parâmetros digitados pelo usuário (input)
formaPagamento = input(f"\nQual é a forma de pagamento ? ")
reserva.FormaPagamento(formaPagamento)

# H O S P E D E 
hospede.Checkin()

# R E S E R V A
reserva.Valor()

# H O S P E D E
# Método da classe Hospede para receber parâmetros digitados pelo usuário (input)
avaliacao = input(f"\nComo o Hospede {hospede.get_NomeHospede()} avalia o serviço ? ")
hospede.Avaliar(avaliacao)

# H O T E L
# Método da classe Hotel para receber parâmetros digitados pelo usuário (input)
estrelas = input(f"\nQuantas estrelas possui o Hotel {hotel.get_NomeHotel()} ? ")
hotel.Estrelas(estrelas)

# H O S P E D E 
hospede.Checkout()

# R E S E R V A
print(f"Data de Saída: {reserva.dataSaida}")

# A g r a d e c i m e n t o
print("Agradecemos pela preferência!!!")

# H O T E L 
hotel.Fechar()
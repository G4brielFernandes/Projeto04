# CAPACITA BRASIL
# Permite múltiplos saques enquanto o limite de saques diários não for atingido.
# Realiza validações para impedir saques inválidos.
# Atualiza o saldo e o número de saques realizados após cada transação bem-sucedida.
# Interrompe o processo caso o limite de saques seja atingido.
# Pergunta ao usuário se deseja continuar antes de cada novo saque.
# Finaliza a operação ao atingir os limites ou por escolha do usuário.

class Conta:
    def __init__(self, limite : float, nome : str):
        self.limite = limite
        self.nome = nome 

    def saque(self, saque):
        limite = self.limite
        if self.limite >= saque:
            self.limite -= saque
            return f"Seu Saque foi realizado: R${saque}" , limite
        else:
            return f"Saldo Negado" , limite
    
    def saldo(self):
        limite = self.limite
        return f"Seu saldo é R${limite}"

while True:
    print("-=" * 10)
    print("BEM VINDO ao banco GABRIELBANCK")
    print("-=" * 10)

    nome = str(input("Informe seu nome: ")).title().strip()
    if nome.isalpha():
        conta = Conta(2000, nome)
    else:
        print("Nome Invalido")
        continue
    break

while True:

    print()
    print(f"Seja bem vindo {nome}")
    x = int(input("MENU: SACAR [1] VER SALDO [2] SAIR [3]: "))
    print()

    if x == 1:
        sacar = float(input("Informe o valor do saque: "))
        x , limite = conta.saque(sacar)
        print(x)
        if limite <= 0:
            print(f"{nome} SEU PROGRAMA FOI FINALIZADO, SEU LIMITE PAPOCOU")
            break
    
    elif x == 2:
        print(conta.saldo())
        
    elif x == 3:
        print("FIM PROGRAMA")
        break
    
    else:
        print("NÃO TEM ESSA OPÇÃO")

    print()
    X = int(input("Deseja continuar: SIM[1] NÃO[2]:  "))
    if x == 2:
        print("FIM PROGRAMA")
        break
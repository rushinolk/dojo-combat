import random


def receber_dano(atacante,defensor):
    defensor.get("vida") -= atacante.get("atk")

def rolar_dado():
    return random.random()

end_game = 0
turno = 1

player = {
    "vida": 200,
    "atk": 25
}

nomes = ["killik","bowden","RUIM"]

while end_game != 1:
    
    if turno == 1:
        npc = {
            "nome": random.choice(nomes),
            "vida": random.randint(150,200),
            "atk": random.randint(10,30) 
        }


    print(f"Turno: {turno}")
    print(f"{npc.get("nome")} NPC Boladão")
    print(f"Vida: {npc.get("vida")}")


    escolha = input("Escolha uma opção: \n1 - Atacar \n2 - Defender")

    if escolha == 1:
        receber_dano(player,npc)
        receber_dano(npc,player)

    if escolha == 2:


    print("Fim de jogo")


if __name__ == "__main__":
    print(random.random())
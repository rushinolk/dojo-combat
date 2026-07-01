import random


def receber_dano(atacante,defensor):
    defensor["vida"] -= atacante["atk"]

def rolar_dado():
    return random.random()

def is_endgame(player, npc):
    if player["vida"] <= 0 or npc["vida"] <= 0:
        return True



if __name__ == "__main__":

    end_game = 0
    turno = 1

    player = {
        "nome": "Leywin",
        "vida": 200,
        "atk": 25
    }

    nomes = ["killik","bowden","RUIM"]


    npc = {
        "nome": random.choice(nomes),
        "vida": random.randint(150,200),
        "atk": random.randint(10,30) 
    }

    while end_game != 1:
        
        if turno == 1:
            npc = {
                "nome": random.choice(nomes),
                "vida": random.randint(150,200),
                "atk": random.randint(10,30) 
            }


        print(f"Turno: {turno}")

        print(f"{player.get("nome")}")
        print(f"Vida: {player.get("vida")}")

        print("------------------------------")
        print(f"{npc['atk']} NPC Boladão")
        print(f"Vida: {npc.get("vida")}")




        escolha = int(input("\n\nEscolha uma opção: \n1 - Atacar \n2 - Defender\n"))

        if escolha not in [1, 2]:
            print("Escolha inválida")
            continue


        if escolha == 1:
            receber_dano(player,npc)
            receber_dano(npc,player)

        if escolha == 2:
            chance = rolar_dado() 
        
            if chance > 0.8:
                print("Esquivou com sucesso!")
            else:
                print("Defesa falhou!")
                receber_dano(npc, player)


        if is_endgame(player,npc):
            end_game = 1
            if player["vida"] <= 0:
                print("Você perdeu!")
            else:
                print("Você venceu!")


        turno += 1
        

    print("Fim de jogo")
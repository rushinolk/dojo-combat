import random


def rolar_dado():
    return random.random()

def receber_dano(atacante,defensor):
    defensor["vida"] -= atacante["atk"]

def realizar_ataque(player,npc):
    receber_dano(player,npc)
    receber_dano(npc,player)


def defender(player,npc):
    chance = rolar_dado() 

    if chance > 0.8:
        print("Esquivou com sucesso!")

    elif chance < 0.4:
        atk_original = npc["atk"]
        npc["atk"] = npc["atk"] / random.randint(2,4)
        receber_dano(npc,player)
        npc["atk"] = atk_original


    else:
        print("Defesa falhou!")
        receber_dano(npc, player)


def is_endgame(player, npc):
    if player["vida"] <= 0 or npc["vida"] <= 0:       
        if player["vida"] <= 0:
            print("Você perdeu!")
            return True
        else:
            print("Você venceu!")
            return True
    return False    




def realizar_ataque(atacante, defensor):
    receber_dano(atacante, defensor)
    print(f"{atacante['nome']} atacou {defensor['nome']} causando {atacante['atk']} de dano!")


if __name__ == "__main__":

    end_game = False
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
 
    while end_game != True:
        
            

        move_set = {
            "1":realizar_ataque,
            "2":defender
        }

        print(f"Turno: {turno}")

        print(f"{player.get("nome")}")
        print(f"Vida: {player.get("vida")}")

        print("------------------------------")
        
        print(f"{npc.get("nome")} NPC Boladão")
        print(f"Vida: {npc.get("vida")}")



        # PESQUISAR TRY/EXCEPT PARA INPUT
        # COMO UTILIZAR O DICIONARIO DE FUNÇÔES
        escolha = int(input("\n\nEscolha uma opção: \n1 - Atacar \n2 - Defender\n"))

        if escolha not in move_set:
            print("Escolha inválida")
            continue
         
            
        
        
        end_game = is_endgame(player,npc)
        turno += 1
        

    print("Fim de jogo")
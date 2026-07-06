import random
import time


def rolar_dado():
    return random.random()

def receber_dano(atacante,defensor):
    defensor["vida"] -= atacante["atk"]

def receber_dano_parcial(atacante,defensor,dano):
    pass

def bleeding(atacante,defensor):
    pass
        
def contra_ataque(atacante,defensor):
    pass


def realizar_ataque(atacante,defensor):
    print(f"{atacante.get('nome')} atacou {defensor.get('nome')}")
    time.sleep(0.6)
    receber_dano(atacante,defensor)
    print(f"{defensor.get('nome')} recebeu {atacante.get('atk')} de dano!")
    time.sleep(0.6)

    if defensor["vida"] > 0:
        print(f"{defensor.get('nome')} atacou {atacante.get('nome')}")
        time.sleep(0.6)
        receber_dano(defensor,atacante)
        print(f"{atacante.get('nome')} recebeu {defensor.get('atk')} de dano!")       
        time.sleep(0.6)

def defender(player,npc):
    chance = rolar_dado() 

    if chance > 0.8:
        time.sleep(0.6)
        print("Esquivou com sucesso!")

    elif chance < 0.4:
        atk_original = npc["atk"]
        npc["atk"] = npc["atk"] / random.randint(2,4)
        receber_dano(npc,player)
        time.sleep(0.6)
        print("Defesa parcial! Você recebeu dano reduzido!")
        npc["atk"] = atk_original


    else:
        time.sleep(1)
        print("Defesa falhou!")
        receber_dano(npc, player)


def use_special(player, npc):
    if player["cooldown_special"] == 0:
        print(f"{player.get('nome')} usou o ataque especial!")
        time.sleep(0.6)
        player["atk"] = player["atk"] * 2
        receber_dano(player, npc)
        print(f"{npc.get('nome')} recebeu {player.get('atk')} de dano!")

        # CAUSAR SANGRAMENTO

        time.sleep(0.6)
        player["atk"] = player["atk"] / 2
        player["cooldown_special"] = 3
    else:
        print(f"Ataque especial em cooldown! Aguarde {player['cooldown_special']}  turnos.")


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
        "atk": 25,
        "cooldown_special": 0
    }

    nomes = ["killik","bowden","RUIM"]

    npc = {
                "nome": random.choice(nomes),
                "vida": random.randint(150,200),
                "atk": random.randint(10,30) 
    }

    move_set = {
            "1":realizar_ataque,
            "2":defender,
            "3":use_special
    }
 
    while end_game != True:

        time.sleep(1.5)
        print(f"\n\nTurno: {turno}")

        print(f"{player.get("nome")}")
        print(f"Vida: {player.get("vida")}")

        print("------------------------------")

        print(f"{npc.get("nome")} NPC Boladão")
        print(f"Vida: {npc.get("vida")}\n")



        
        try:
            escolha = input("\n\nEscolha uma opção: \n1 - Atacar \n2 - Defender\n3 - Ataque Especial\n\n")

        except ValueError:
            print("Entrada inválida!")

        if escolha == "0":
            print("Encerrando programa...")
            break

        if escolha in move_set:
            funcao_escolhida = move_set[escolha]
            funcao_escolhida(player,npc)

        
        
        end_game = is_endgame(player,npc)
        turno += 1
        

    print("Fim de jogo")
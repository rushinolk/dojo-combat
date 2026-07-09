import random
import time
import logging



#logging configuration
logging.basicConfig(
    filename="luta.log", 
    level=logging.DEBUG, 
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)



def rolar_dado():
    return random.random()

def receber_dano_atk(atacante,defensor):
    defensor["vida"] -= atacante["atk"]

def receber_dano_parcial(defensor,dano):
    defensor["vida"] -= dano

def bleeding(atacante,defensor):
    pass
        
def contra_ataque(atacante,defensor):
    if defensor["vida"] > 0:
        logging.info(f"{defensor.get('nome')} atacou {atacante.get('nome')}")
        time.sleep(0.6)
        receber_dano_atk(defensor,atacante)
        logging.info(f"{atacante.get('nome')} recebeu {defensor.get('atk')} de dano!")       
        time.sleep(0.6)


def realizar_ataque(atacante,defensor):
    logging.info(f"{atacante.get('nome')} atacou {defensor.get('nome')}")
    time.sleep(0.6)
    receber_dano_atk(atacante,defensor)
    logging.info(f"{defensor.get('nome')} recebeu {atacante.get('atk')} de dano!")
    time.sleep(0.6)

    contra_ataque(atacante,defensor)

def defender(player,npc):
    chance = rolar_dado() 

    if chance > 0.8:
        time.sleep(0.6)
        logging.info("Esquivou com sucesso!")

    elif chance < 0.4:
        atk_original = npc["atk"]
        npc["atk"] = npc["atk"] / random.randint(2,4)
        receber_dano_atk(npc,player)
        time.sleep(0.6)
        logging.info("Defesa parcial! Você recebeu dano reduzido!")
        npc["atk"] = atk_original


    else:
        time.sleep(1)
        logging.info("Defesa falhou!")
        receber_dano_atk(npc, player)


def use_special(player, npc):
    if player["cooldown_special"] == 0:
        logging.info(f"{player.get('nome')} usou o ataque especial!")
        time.sleep(0.6)
        player["atk"] = player["atk"] * 2
        receber_dano_atk(player, npc)
        logging.info(f"{npc.get('nome')} recebeu {player.get('atk')} de dano!")

        # CAUSAR SANGRAMENTO

        time.sleep(0.6)
        player["atk"] = player["atk"] / 2
        player["cooldown_special"] = 3
    else:
        logging.info(f"Ataque especial em cooldown! Aguarde {player['cooldown_special']}  turnos.")

def is_endgame(player, npc):
    if player["vida"] <= 0 or npc["vida"] <= 0:       
        if player["vida"] <= 0:
            logging.info("Você perdeu!")
            return True
        else:
            logging.info("Você venceu!")
            return True
    return False    



if __name__ == "__main__":

    end_game = False
    turno = 1

    player = {
        "nome": "Leywin",
        "vida": 200,
        "atk": 25,
        "cooldown_special": 0,
        "debuff_time": 0,
        "buff_time": 0
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
 
    while not end_game:

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
            logging.error("Entrada inválida!")

        if escolha == "0":
            logging.info("Encerrando programa...")
            break

        if escolha in move_set:
            funcao_escolhida = move_set[escolha]
            funcao_escolhida(player,npc)

        
        
        end_game = is_endgame(player,npc)
        turno += 1
        

    logging.info("Fim de jogo")
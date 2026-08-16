import random
import time
import logging


console_handler = logging.StreamHandler()

# 2. Configura para mandar para o arquivo
file_handler = logging.FileHandler('log/luta.log', encoding='utf-8')

#logging configuration
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[console_handler, file_handler]
)



def rolar_dado():
    return random.random()

def receber_dano_atk(atacante,defensor):
    defensor["vida"] -= atacante["atk"]

def receber_dano_parcial(defensor,dano):
    defensor["vida"] -= dano

def bleeding(atacante, defensor, turnos=3, dano_min=4, dano_max=10, chance=1.0):
    if rolar_dado() >= chance:
        return False

    defensor["bleeding"] = {
        "turnos": turnos,
        "dano_min": dano_min,
        "dano_max": dano_max,
    }
    print(f"{defensor.get('nome')} está sangrando por {turnos} turno(s)!")
    time.sleep(0.6)
    return True


def processar_sangramento(combatente):
    if combatente.get("bleeding") is None or combatente["vida"] <= 0:
        return

    sangramento = combatente["bleeding"]
    dano = random.randint(sangramento["dano_min"], sangramento["dano_max"])
    receber_dano_parcial(combatente, dano)

    sangramento["turnos"] -= 1
    turnos_restantes = sangramento["turnos"]

    print(f"{combatente.get('nome')} sangrou e perdeu {dano} de vida!", end="")
    if turnos_restantes > 0:
        print(f" ({turnos_restantes} turno(s) restante(s))")
    else:
        print()
        del combatente["bleeding"]
        print(f"{combatente.get('nome')} parou de sangrar.")
    time.sleep(0.6)


def processar_sangramentos(*combatentes):
    for combatente in combatentes:
        processar_sangramento(combatente)

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
        if not bleeding(player, npc, chance=0.4):
            logging.info(f"{npc.get('nome')} resistiu ao sangramento!")
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


# Sistema de equipamentos que adicionam atributos ao char
# Atributos base: energia, atk, defesa, agilidade, concentração, percepção
# Atributos %: vida, perfuração, incremento de critico, incremento de absorção
# Adicionar mecanica de drop de itens aleatorios


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

    jutsu = {
        "nome": "jutsu",
        "atk": 0,
        "cooldown": 0,
        "tipo": "ataque"
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

        processar_sangramentos(player, npc)

        if is_endgame(player, npc):
            break

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
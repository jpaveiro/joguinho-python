import random

# Definir a vida do boss e o turno atual
vida_boss = random.choice([250.00, 415.00, 645.00])
turno_atual = 1

# Definir cooldown para cada habilidade
cooldown_q = 0
cooldown_e = 0
cooldown_r = 0

# Loop do jogo
while vida_boss > 0.00:
    # Mostrar o turno atual
    print(f"=== Turno {turno_atual} ===")

    # Mostrar as habilidades disponíveis
    print("Use uma habilidade! Habilidades disponíveis:")
    print("Q= Ataque simples - 7.3dmg")
    print("E= Bola de fogo - 17.5dmg (cooldown 2 turno)")
    print("R= Relâmpago - 23.7dmg (cooldown 3 turnos)")

    # Pedir para o usuário escolher uma habilidade
    habilidade = input()

    # Verificar qual habilidade foi escolhida e executá-la
    if habilidade == "Q":
        if cooldown_q == 0:
            print(f"\n===== @ =====\nVocê usou Ataque Simples e causou 7.3 de dano ao Boss!\n===== @ =====")
            vida_boss -= 7.3
            cooldown_q = 0
        else:
            print("Habilidade em cooldown. Escolha outra habilidade.")

    elif habilidade == "E":
        if cooldown_e == 0:
            print(f"\n===== @ =====\nVocê usou Bola de fogo e causou 17.5 de dano ao Boss!\n===== @ =====")
            vida_boss -= 17.5
            cooldown_e = 3
        else:
            print("Habilidade em cooldown. Escolha outra habilidade.")

    elif habilidade == "R":
        if cooldown_r == 0:
            print(f"\n===== @ =====\nVocê usou Relâmpago e causou 23.7 de dano ao Boss!\n===== @ =====")
            vida_boss -= 23.7
            cooldown_r = 4
        else:
            print("Habilidade em cooldown. Escolha outra habilidade.")

    else:
        print("Habilidade inválida. Escolha outra habilidade.")

    # Diminuir o cooldown de cada habilidade em 1
    if cooldown_q > 0:
        cooldown_q -= 1
    if cooldown_e > 0:
        cooldown_e -= 1
    if cooldown_r > 0:
        cooldown_r -= 1

    # Mostrar a vida restante do boss e aumentar o número de turnos
    print(f"Vida Restante do Boss: {vida_boss:.2f}")
    turno_atual += 1

# Mostrar a mensagem de vitória quando o boss for derrotado
print("Parabéns, você venceu o Boss!")

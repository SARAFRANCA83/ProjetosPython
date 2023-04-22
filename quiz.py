print("Bem vindo ao quiz")
resp_user = input("Quer começar? S/N ")

if resp_user != "S" and resp_user == "N":
    print("Até a próxima! ")
    quit()

score = 0

print("Começando...\n")
print("Onde está localizado o menor osso do corpo humano ? \n A Mão \n B Nariz \n C Ouvido \n D Língua \n")
resp_1 = input("Resposta: ")

if resp_1 == "C":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Quem foi o vencedor do Big Brother Brasil 20? \n A Thelma Assis \n B Prior \n C Rafa Caliman \n D Bam Bam \n")
resp_2 = input("Resposta: ")

if resp_2 == "A":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Como se chamam os dois melhores amigos do personagem Harry Potter? \n A Sirius e Dolores \n B Hermione e Rony \n C Edwiges e Fleur \n D Bellatrix e Pedro \n")
resp_3 = input("Resposta: ")

if resp_3 == "B":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print(" Em que ano estreou o filme Titanic? \n A 1997 \n B 1995 \n C 1998 \n D 1999 \n")
resp_4 = input("Resposta: ")

if resp_4 == "A":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Qual é o maior país do mundo? \n A Itália \n B Portugal \n C Brasil \n D Russia \n")
resp_5 = input("Resposta: ")

if resp_5 == "D":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Em quantas regiões o Brasil é dividido? \n A Seis \n B Sete \n C Tres \n D Cinco \n")
resp_6 = input("Resposta: ")

if resp_6 == "D":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Qual é o único mamífero que voa? \n A Águia \n B Morcego \n C Papagaio \n D Rolinha \n")
resp_7 = input("Resposta: ")

if resp_7 == "B":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Em que ano o Rio de Janeiro sediou os Jogos Olímpicos ? \n A 2018 \n B 2019 \n C 2016 \n D 2017 \n")
resp_8 = input("Resposta: ")

if resp_8 == "C":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Para quem o Brasil perdeu a final da Copa do Mundo de 1950, em pleno Maracanã ? \n A Paraguai \n B França \n C Alemanha \n D Uruguai \n")
resp_9 = input("Resposta: ")

if resp_9 == "D":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print("Quantas estrelas tem a bandeira do Brasil ? \n A 28 \n B 25 \n C 30 \n D 27 \n")
resp_10 = input("Resposta: ")

if resp_10 == "D":
    print("Correto")
    score = score + 1
else:
    print("Errado")

print(f"Quiz acaboou... Sua pontuação foi: {score}/10")
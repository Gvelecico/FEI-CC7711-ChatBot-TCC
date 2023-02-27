from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()




print("Bem vindo ao chatbot TiraDuvidaTCC, qual a sua duvida?")


pergunta = input("como posso te ajudar?")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="parada"):
    pergunta = input(" ")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")
    #if (intencao[0]['intent']=="Ajuda_00"):




print("Foi um prazer atendê-lo")

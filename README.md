# FEI-CC7711-ChatBot-TCC
<!-- START_SECTION: exemplo -->

Chat bot de Gustavo Velecico 22.120.044-7 e Pedro Henrique Braga 22.120.064-5


<!-- END_SECTION: exemplo -->
<!-- Exemplo de código JSON -->
```json

{"intents":[{ "tag": "parada", #Usuario para o programa
    "patterns":["até mais","até logo","isso é tudo","encerrar chat", "parar chat", "parar"],
    "responses": ["Obrigado por ter me utilizado","Ate logo!"]
  },
  { "tag": "erro", #Usuario recebe um erro e notifica o chat que a resposta está errada
  "patterns":["nao foi isso que perguntei", "a resposta nao está certa", "nao gostei da resposta"],
  "responses": ["Desculpe =( , voce poderia perguntar novamente?", "Que pena, poderia perguntar novamente sua duvida?"]
},
  { "tag": "intuito", #Para pessoas que não sabem nada do TCC
    "patterns":["Qual é o proposito do TCC?", "Qual é o intuito do trabalho de final de curso?", "objetivo do tcc", "oque e um tcc"],
    "responses": ["O trabalho de Final de Curso tem como objetivo em treinar os estudantes a desenvolver uma solucao, tendo base no metodo cinetifico, para uma questao que utilize recursos computacionais e os conhecimentos acumulados durante o curso de sua graduacao"]
  },
  { "tag": "inicio", #Para dicas iniciais do TCC
  "patterns":["Como posso comecar a desenvolver meu TCC?","Qual o primeiro passo a se tomar para fazer meu trabalho de final de curso?","Começo do tcc?"],
  "responses": ["Para comecar a desenvolver seu TCC, eh aconselhavel que você faca um grupo de 4 pessoas, depois disso escolha um tema para o desenvolvimento da solucao e no fim ache um professor orientador interessado em seu projeto"]
  },
  { "tag": "tema",  #Para dicas para tema do TCC
  "patterns":["Como posso achar um tema interessante para meu tcc?","qual o melhor tema para realizar o tcc?", "tema"],
  "responses": ["Nao existe melhor tema para o TCC, porem voce pode achar propostas interessantes na aba da disciplina CC7411 em Propostas Temas TCC"]
  },
  { "tag": "Ajuda_00", #Começo de series de perguntas para o usuario
  "patterns":["Como obtenho ajuda em relacao ao desenvolvimento do meu TCC"],
  "responses": ["Qual seria esse tipo de ajuda? Normas abnt, professor orientador?"]
  },
  { "tag": "Ajuda_01", #Duvidas na abnt
  "patterns":["Gostaria de ajuda para escrever nas normas ABNT", "escrita na norma ABNT", "Duvidas gerais"],
  "responses": ["Você pode procurar ajuda para escrever nas normas ABNT na aba da disciplina CC7411 em Modelos Exemplos Refêrencias "]
  },
  { "tag": "Ajuda_02", #Duvidas professor orientador
  "patterns":["Qual é a melhor forma de alinhamento com o professor orientador", "Professor orientador"],
  "responses": ["A melhor forma de fazer o alinhamento entre seu grupo e o professor orientador é realizar reuniões semanais"]
  },
  { "tag": "data_banca", #perguntar qual é a data da banca?
  "patterns":["Quando sera a banca","A banca será realizada em que dia?", "data", "banca"],
  "responses": ["no dia 19 de junho mas vale lembrar que você precisa enviar seu arquivo PDF contendo o TCC até o dia 05 de junho"]
  }
  

]
}
-->
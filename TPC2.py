#!/usr/bin/env python
# coding: utf-8

# # TPC2

# ## Adivinha o número

# * __Data início__: 2022-09-30
# * __Data fim__:2012-10-02
# * __Supervisor__: José Carlos Ramalho, https://www.di.uminho.pt/~jcr/index.html
# * __Autor__: Alexandra Cordeiro, A94524
# * __Resumo__: <p> O código realizado tem como objetivo adivinhar um número de 0 a 100 em que uma pessoa pensou em apenas 7 tentativas. <p> A pessoa apenas pode dizer se o número é maior ou menor.<p> 
# 
#     Foi criado com base na estratégia de dividir sucessivamente os números por 2 e ir somando ou subtraindo números de acordo com as indicações que a pessoa dá.

# In[ ]:


def adivinha():
    i=1
    x=50
    print('Pensa num número de 0 a 100 e tentarei adivinhá-lo!')
    encontrado=False
    while i<8 and encontrado==False:
        b=input("O número em que pensaste é igual a %s (introduza 'i'), maior (introduza 'M') ou menor (introduza 'm')?" %(x))
        if b=='M':
            x=x+(50/(2**i))
            x=round(x)
            i=i+1
        elif b=='m':
            x=x-(50/(2**i))
            x=round(x)
            i=i+1
        elif b=='i':
            print('Número encontrado!')
            print('Com',i,'tentativas, eu consegui adivinhar o número em que tu pensaste!')
            encontrado=True
        else:
            print('Introduza uma letra correta: i, M ou m')
    if encontrado==True:
        c=input("Desejas jogar novamente? Introduza 'S' para SIM e 'N' para NÃO")
        d=c.upper()
        if d=='S':
            return adivinha()
        else:
            print('Até à próxima!')
adivinha()


# In[ ]:





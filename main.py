from js import document
import math
import random


msgAviso = document.querySelector("#aviso")
msgAviso2 = document.querySelector("#aviso2")
criptografada = document.querySelector("#encrypted-message-primary") 
chave_privada = document.querySelector("#chave-privada1")
chave_publica = document.querySelector("#chave-publica1")




def criptografar(event):
    inputRSA = document.querySelector("#rsa")
    inputTWOFISH = document.querySelector("#twofish")
    inputDES = document.querySelector("#des")
    inputTLS = document.querySelector("#tls")
    inputSAFER = document.querySelector("#safer")


    mensagemTexto = document.querySelector("#message-primary")
    if mensagemTexto.value == "":
        msgAviso.innerText = "ERRO! Digite a mensagem para encriptografar!"
        msgAviso.style.display = "block"
        msgAviso.style.color = "red"
        criptografada.value = ""
        chave_privada.value = ""
        chave_publica.value = ""
        
    elif not inputRSA.checked and not inputTWOFISH.checked and not inputDES.checked and not inputTLS.checked and not inputSAFER.checked:
        msgAviso.innerText = "ERRO! Selecione um tipo de criptografia!"
        msgAviso.style.display = "block"
        msgAviso.style.color = "red"
        criptografada.value = ""
        chave_privada.value = ""
        chave_publica.value = ""
    elif not inputRSA.checked:
        msgAviso.innerText = "ERRO! Criptografia em desenvolvimento!"
        msgAviso.style.display = "block"
        msgAviso.style.color = "red"
        criptografada.value = ""
        chave_privada.value = ""
        chave_publica.value = ""
    else:
        msgAviso.style.display = "block"
        msgAviso.innerText = "Mensagem criptografada com sucesso!"
        msgAviso.style.color = "#7f8c8d"
        
        msgAviso2.innerText = ""
        
    
        msg = mensagemTexto.value        

        chave_privadaVisivel = document.querySelector("#senhaPrivadaVisivel")
        chave_publicaVisivel = document.querySelector("#senhaPublicaVisivel")
        
        chave_privadaVisivel.style.visibility = "visible"
        chave_publicaVisivel.style.visibility = "visible"
        
        msgCifrada = []
        msgCifradaTemp = []
        n,d,e,m = None,None,None,None
        
        primos = sort_prime(300)
        
        #dois números aleatórios dentro dos primos do range do número máximo de primos
        #usando a função get randown do import
        #- 60 para remover o 2 e 3, pois são 62 primos
        p = primos[get_random_int(len(primos)-60,len(primos))]
        q = primos[get_random_int(len(primos)-60,len(primos))]

        # multiplicar os primos (N)
        n = p*q
        
        #Co-primo (M)
        m = (p-1)*(q-1)
        
        tempE = 0
        temp=(get_random_int(1,m))
        e=0
        while(e==0) :
            tempE = mdc(temp,m)
            if tempE==1 : e = temp
            else : temp=(get_random_int(1,m))
        
        d = modInverse(e,m)
        
        #Transformou a mensagem de bytes para utf-8
        strBytes = bytes(msg, 'utf-8')
        for byte in strBytes:
            msgCifradaTemp.append(byte)
        
        
        for index in range(len(msgCifradaTemp)):
            temp = pow(msgCifradaTemp[index],e)
            temp2 = temp % n
            msgCifrada.append(temp2)
            
        
        #deixando o resultado da criptografia
        criptografada.value = msgCifrada

        chave_privada.value = n ,d
            
        chave_publica.value = n, p

        mensagemTexto.placeholder = "Mensagem para encriptografar"    
        
        
def exportadados(event):
    
    msgAviso.style.display = "block"
    if chave_publica.value == "" or chave_privada.value == "" or criptografada.value == "":
        msgAviso.style.color = "red"
        msgAviso.innerText = "ERRO! Criptografe uma mensagem para transferir dados!"
    else:
        msgAviso.style.color = "#7f8c8d"
        msgAviso.innerText = "Dados transferidos para descriptografação!"
        criptografadaTexto = str(criptografada.value)
        chave_privadaTexto = str(chave_privada.value)
        chave_publicaTexto = str(chave_publica.value)
        
        chave_privada2 = document.querySelector("#chave-privada2") # atribuindo a chave_privada ao id #chave-privada2 HTML
        chave_privada2.value = chave_privadaTexto
        chave_publica2 = document.querySelector("#chave-publica2")
        chave_publica2.value = chave_publicaTexto
        
        criptografada2 = document.querySelector("#encrypted-message-second") # TA FUNFANDO
        criptografada2.value = criptografadaTexto
        
        
    
    
    
def descriptografar(event):
    msgDecifradaTemp = []
    msgDecifrada = []
    mensagem = document.querySelector("#decrypted-message")
    chave_privada = document.querySelector("#chave-privada2") # atribuindo a chave_privada ao id #chave-privada2 HTML
    chave_publica = document.querySelector("#chave-publica2")
    criptografada = document.querySelector("#encrypted-message-second") # TA FUNFANDO
    inputRSA = document.querySelector("#rsa2")
    inputTWOFISH = document.querySelector("#twofish2")
    inputDES = document.querySelector("#des2")
    inputTLS = document.querySelector("#tls2")
    inputSAFER = document.querySelector("#safer2")
    
    if chave_privada.value == "" or chave_publica.value == "" or criptografada.value == "":
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "red"
        msgAviso2.innerText = "ERRO! Complete os campos obrigatórios!"
        mensagem.value = ""
    elif not inputRSA.checked and not inputTWOFISH.checked and not inputDES.checked and not inputTLS.checked and not inputSAFER.checked:
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "red"
        msgAviso2.innerText = "ERRO! Selecione um tipo de criptografia!"
        mensagem.value = ""
    
    elif not inputRSA.checked:
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "red"
        msgAviso2.innerText = "ERRO! Criptografia em desenvolvimento!"
        mensagem.value = ""

    else:
        msgAviso2.style.display = "block"
        msgAviso2.style.color = "#7f8c8d"
        msgAviso2.innerText = "Mensagem descriptografada com sucesso!"
        
        chave_privada1 = chave_privada.value
        chave_privada2 = chave_privada1.strip("()")
        listaChavePrivada = chave_privada2.split(",") # lista com as 2 chaves privadas (n, d)
        n = int(listaChavePrivada[0]) #atribuindo o primeiro index com n (int) X
        d = int(listaChavePrivada[1]) #atribuindo o segundo index com d (int) X
        
        chave_publica1 = chave_publica.value
        chave_publica2 = chave_publica1.strip("()")
        listaChavePublica = chave_publica2.split(",") # lista com as 2 chaves publicas (n, p)
        p = int(listaChavePublica[1]) #atribuindo o segundo index com d (int) X
        
        criptografada1 = criptografada.value
        criptografada2 = criptografada1[1: -1] # TA FUNFANDO PORRA!!! (tira cochete da string)
        criptografadaLista = criptografada2.split(",") #TA FUNFANDO PORRA!!! (virou uma lista)
        criptografadaLista2 = [int(i) for i in criptografadaLista] # saporra ta convertendo pra integers

        primos = sort_prime(300)

        q = primos[get_random_int(len(primos)-60,len(primos))]

        m = (p-1)*(q-1)

        tempE = 0
        temp=(get_random_int(1,m))
        e=0
        while(e==0) :
            tempE = mdc(temp,m)
            if tempE==1 : e = temp
            else : temp=(get_random_int(1,m))




        for index in range(len(criptografadaLista2)):
            temp = pow(criptografadaLista2[index],e)
            msgDecifradaTemp.append(pow(criptografadaLista2[index],d) % n)

        msgDecifrada = bytes(msgDecifradaTemp)
        msgDecifradaUTF8 = msgDecifrada.decode('utf-8')

        mensagem.value = msgDecifradaUTF8
        
        msgAviso.style.display = "none"
    


#função para o número primo
#num seria o número máx
# ex num = 100, todos os números primos de 1 à 100 e escolher um primo
def sort_prime(num):
    prime_num1 = []
    prime_num2 = [True] * (num + 1)
    for i in range(2, num + 1):
        if prime_num2[i]:
            prime_num1.append(i)
            for j in range(2, int(num / i) + 1):
                prime_num2[i * j] = False
    return prime_num1

#função para um número aleatório
def get_random_int(min, max):
    min = math.ceil(min)
    max = math.floor(max)
    return math.floor(random.random() * (max - min + 1)) + min

#MDC (máximo divisor comum)
#números primos entre si possuim apenas o 1 como divisor comum
def mdc(x,y):
    while(y) :
        t=y
        y=x%y
        x=t
    return x


def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
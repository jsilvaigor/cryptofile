import os
def encripta(entrada):
    chave = 3
    texto_lista = list(entrada)
    texto_encriptado = ""
    for i in texto_lista:
		# verifica se e uma letra
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            if (i >= 'a' and i <= 'z'):
                ord_c = (ord(i) - ord('a') + chave) % 26
                texto_encriptado += chr(ord_c + ord('a'))
            else:
                ord_c = (ord(i) - ord('A') + chave) % 26
                texto_encriptado += chr(ord_c + ord('A'))
	   # se for um numero
        else:
            texto_encriptado += i

    return texto_encriptado
def decripta(entrada):

    chave = 3
    texto_lista = list(entrada)
    texto_decriptado = ""
    for i in texto_lista:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            if (i >= 'a' and i <= 'z'):
                ord_c = (ord(i) - ord('a') - chave) % 26
                texto_decriptado += chr(ord_c + ord('a'))
            else:
                ord_c = (ord(i) - ord('A') - chave) % 26
                texto_decriptado += chr(ord_c + ord('A'))
        else:
            texto_decriptado += i
    return texto_decriptado

def encriptaTXT():
    apagar = input("Deseja apagar os arquivos originais? S para Sim N para Nao")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith(".txt"):
                print(os.path.join(root, name)+"  Processando....")
                caminho =(os.path.join(root, name))
                abreArquivo = open(caminho, "r+")
                texto = abreArquivo.read()
                encriptado = encripta(texto)
                abreArquivo.close()
                grava = open((caminho+'.enc'),'w')
                grava.write(encriptado)
                grava.close()
                if apagar == 'S' or apagar =='s':
                    os.remove(caminho)
                print(os.path.join(root, name)+" OK!")

def decriptaTXT():
    apagar = input("Deseja apagar os arquivos originais? S para Sim N para Nao")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith(".enc"):
                print(os.path.join(root, name)+"  Processando....")
                caminho =(os.path.join(root, name))
                abreArquivo = open(caminho, "r+")
                texto = abreArquivo.read()
                decriptado = decripta(texto)
                abreArquivo.close()
                grava = open((caminho[0:-4]),'w')
                grava.write(decriptado)
                grava.close()
                if apagar == 'S' or apagar =='s':
                    os.remove(caminho)
                print(os.path.join(root, name)+" OK!")

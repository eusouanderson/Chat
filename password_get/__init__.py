from cryptography.fernet import Fernet
from info import info
import os

dir_atual = os.getcwd()
path_cr = os.path.abspath(os.path.join(dir_atual, "password_get/""arquivo_criptografado.txt"))
path_dr = os.path.abspath(os.path.join(dir_atual, "password_get/""TXT.axx"))

# Gerar uma chave de criptografia aleatória
chave_cr = Fernet.generate_key()



def pegarsenha(username, password):
    senha = password
    login = username
    
    todos= username + password
    criptografar(password=todos.encode())

    descriptografar()
    return info(2)

def lersenha(password, username ):
    try :
        with open(path_dr, 'r') as file:
            texto = file.read()
        palavra_procurada = password + username
        nome = username
        if palavra_procurada in texto:
            return True, nome
        else:
            return False
    except FileNotFoundError:
            return False

def salvarUsername(username):
    # Criando uma lista
    listName = []
    try:
        with open(path_dr, 'r') as file:
            listName = file.readlines()
        letras = ""
        cont = len(listName)
        for caractere in listName[cont]:
            if caractere.isalpha():
                letras += caractere
                retUs1 = letras
        return retUs2[1:].replace("b'", ""), retUs1[1:].replace("b'", "")
    except IndexError:
        retUs1 = 'Ninguém conectado'
        retUs2 = 'Ninguém conctado'
        return retUs1 , retUs2

def criptografar(cripto=chave_cr, password=pegarsenha):
    # Cria um objeto Fernet usando a chave
    fernet = Fernet(cripto)
    conteudo_criptografado = fernet.encrypt(password)
    # Gravar o conteúdo criptografado em um novo arquivo
    with open(path_cr, 'ab') as arquivo_crip:
        #arquivo_crip.write(conteudo_criptografado)
        arquivo_crip.write(f'{conteudo_criptografado}\n'.replace("b'", "").encode())
    
    return 'Arquivo criptografado com sucesso!'


def descriptografar(cripto=chave_cr):
    # Criar o objeto Fernet com a chave
    fernet = Fernet(cripto)
    with open(path_cr, 'rb') as arquivo_cripto:
        # Ler o conteudo do arquivo criptografado e armazená-lo em uma variável
        arquivo_cripto_bytes = arquivo_cripto.read()
        # Descriptografar o arquivo
        arquivo_original_bytes = fernet.decrypt(arquivo_cripto_bytes)
    # Escrever o conteúdo descriptografado em um novo arquivo
    
    with open(path_dr, 'a') as arquivo_descripto:
        arquivo_descripto.write(f'{arquivo_original_bytes}\n')
    
    return os.remove(path_cr)



'''# verificar se um arquivo existe
caminho_absoluto = os.path.abspath(os.path.join(dir_atual, "arquivo_criptografado.txt"))

print(f"Caminho absoluto para arquivo.txt: {caminho_absoluto}")

# verificar se um arquivo existe
if os.path.isfile(path_cr):
    print("O arquivo existe.")
else:
    print("O arquivo não existe.")'''
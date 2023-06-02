import os
import json
import ast

dir_atual = os.getcwd()
path_user = os.path.abspath(os.path.join(dir_atual, "bd/""IP.axx"))

def users(users):
    with open(path_user,"w") as file:
            linha = json.dumps(users)
            file.write(linha)
    
def search(ip_busca):
     with open(path_user, 'r') as file:
          conteudo = file.read()
          dicionario = ast.literal_eval(conteudo)
          if ip_busca in dicionario:
               info = dicionario[ip_busca]
               return info
          else:
               return None

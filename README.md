
# Bate Papo

Com intuito de aprender mais sobre o flamworke Flask e a ferramenta Socket.io , criei esse bate papo em tempo real , que funciona em rede.


### Flask
Flask é um framework para desenvolvimento web em Python que oferece ferramentas e recursos para a criação de aplicativos web. Ele é conhecido por sua facilidade de uso e flexibilidade, tornando-o uma escolha popular para desenvolvedores de todos os níveis de experiência.

### Request
O módulo Request é parte do pacote Flask e é usado para lidar com requisições HTTP enviadas pelo cliente ao servidor. Ele fornece uma interface simples e fácil de usar para acessar os dados de uma requisição, incluindo parâmetros de consulta, dados do formulário e cabeçalhos HTTP.

### Cryptography
O módulo Cryptography é uma biblioteca Python para criptografia. Ele oferece suporte a uma ampla variedade de algoritmos de criptografia, incluindo AES, RSA e SHA-256, bem como funções de hash, geração de chaves e muito mais. É uma escolha popular para desenvolvedores que precisam de criptografia em seus aplicativos.

### SocketIO 
É uma biblioteca JavaScript que permite a comunicação em tempo real entre o servidor e o cliente por meio do protocolo WebSocket. Ela é amplamente utilizada para criar aplicativos da web em tempo real, como jogos online, bate-papos, notificações em tempo real, entre outros.

### Bootstrap
É um popular framework de design responsivo para a criação de sites e aplicativos web. Ele inclui um conjunto de estilos CSS, componentes JavaScript e fontes de ícones que ajudam a criar páginas web modernas, elegantes e funcionais.

## Ferramentas

1. Linguagem: [Python](https://www.python.org/) [Html](https://www.learn-html.org/) [Css](https://www.w3.org) [Javascript](https://js.org/)
2. Framework: [Flask](https://flask.palletsprojects.com/en/2.1.x/)
3. Plataforma de Hospedagem: 

## Get Started

1. Baixe o arquivo app.py junto com seu código
2. Adicionar as libs necessárias para o seu projeto no arquivo [requirements.txt](./requirements.txt)
3. Estou usando Linux Ubuntu 22.04.2 LTS
4. A versão funcional do Python é a 3.8
5. Ative o ambiente virtual dentro do diretório /bate-papo

~~~
source venv-3.8/bin/activate
~~~ 

## Testar Local

Para testar local execute o seguinte comando
no diretorio :



No Linux :

~~~
 python3 app.py run
~~~

No Windows :

~~~
 python app.py run
~~~
Ou pelo terminal bash :

``` bash
cd /bate-papo-flask

source root.sh

selecione 2
```


## Testar em Rede
Para testar em rede execute o seguinte comando
no diretorio :


No Linux : 
~~~
python3 app.py run --host=0.0.0.0
~~~
No Windows : 

~~~
python app.py run --host=0.0.0.0
~~~
Ou pelo terminal bash :

``` bash

cd /bate-papo-flask

source root.sh

selecione 1 

```




![screenshot](/img/Captura%20de%20tela%20de%202023-04-25%2015-05-31.png)


![screenshot](/img/Captura%20de%20tela%20de%202023-04-28%2022-04-58.png)

---
Developed by [Anderson B.O.B](https://github.com/eusouanderson)

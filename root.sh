#!/bin/bash

echo "Escolha uma opção:"
echo "1 - Rede  "
echo "2 - Local "

read opcao

if [ $opcao -eq 1 ]
then
  python3 app.py host = '0.0.0.0'
  echo "Bate Papo em Rede Local... "
  
elif [ $opcao -eq 2 ]
then
  python3 app.py main run
  echo "Bate Papo em modo local..."
  
else
  echo "Opção inválida!"
fi

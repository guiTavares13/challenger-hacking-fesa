import argparse
import os
import subprocess
import threading
import glob


REPLACE_STRING = "MEU_ARQUIVO"

# Função para executar o comando em uma thread
def execute_command(command,file_name):
    global REPLACE_STRING

    command = command.replace(REPLACE_STRING,file_name)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f"Comando '{command}' \n Saída:\n{stdout.decode('utf-8')}")

def main():
    parser = argparse.ArgumentParser(description='Execute um comando em múltiplas threads para arquivos com prefixo "small".')
    parser.add_argument('command', help='Comando a ser executado no terminal')

    args = parser.parse_args()

    # Lista de arquivos com prefixo "small" no diretório atual
    files = glob.glob("small*")

    # Criação e inicialização das threads para processar os arquivos
    threads = []
    for file in files:
        command = f"{args.command}"
        thread = threading.Thread(target=execute_command, args=(command,file))
        thread.start()
        threads.append(thread)

    # Aguarda até que todas as threads tenham terminado
    for thread in threads:
        thread.join()

    print("Todos os comandos foram executados para os arquivos com prefixo 'small'.")

if __name__ == "__main__":
    main()
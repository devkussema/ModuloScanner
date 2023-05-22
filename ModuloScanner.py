'''
# Um programa que lista todos os modulos instalados em Python.
#
## É obrigatório teres instalado o pacote 'tabulate'
 -> Para instalar o módulo tabulate faça o seguinte
 -> Execute no terminal >> ``pip install tabulate´´

 @author: Augusto Kussema
 @github: https://github.com/devkussema
 @email: dev.kussema@gmail.com
 @version: 2.3
 @copyright: (c) 2023 Augusto Kussema
 @license: MIT
 @country: Angola, Luanda
'''

import subprocess
from tabulate import tabulate


class ModuloScanner:
    """
        Classe para escanear e exibir todos os modulos instalados em Python no PC.
    """
    def __init__(self):
        self.applications = []

    def get_modulos_instalados(self):
        """
            Obtém a lista de módulos instalados no PC.
        """
        try:
            output = subprocess.check_output(['pip', 'list']).decode('utf-8', errors='ignore')
            lines = output.split('\n')[2:]
            for line in lines:
                if line:
                    parts = line.split()
                    name = parts[0]
                    version = parts[1]
                    self.applications.append((name, version))
        except subprocess.CalledProcessError as e:
            print("Ocorreu um erro ao obter as aplicações instaladas:", str(e))

    def exibir_modulos(self):
        """
            Exibe os módulos instalados no PC.
        """
        if not self.applications:
            print("Nenhuma aplicação instalada encontrada.")
        else:
            headers = ["Nome", "Versão"]
            print(tabulate(self.applications, headers=headers, tablefmt="plain"))

scanner = ModuloScanner()
scanner.get_modulos_instalados()
scanner.exibir_modulos()

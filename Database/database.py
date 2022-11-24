import sqlite3

from AnimaCursoPython2022.aula_4 import conexao


class Database:
    conexao = None
    cursor = None

    def __init__(self):
        #global conexao, cursor
        self.conexao = sqlite3.connect("database/imdb.db")
        self.cursor = self.conexao.cursor()

    def __del__(self):
        conexao.commit()
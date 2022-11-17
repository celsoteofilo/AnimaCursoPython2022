import  sqlite3

# ________CONEXAO DE DADOS___________
conexao = sqlite3.connect("dc_universe.db")

#__________CRIANDO OBJETO _________
curso = conexao.cursor()
sql = "SELECT pessoa_id, nome,nome_civil, tipo FROM pessoas"

curso.execute(sql)

pessoas=curso.fetchall()
for pessoa in pessoas:
    print(pessoa)

for pessoa in pessoas:
    print(f'nome{pessoa[1]} ({pessoa[3]})')

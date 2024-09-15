import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", host="localhost", password="cruzeiro")
    print("Conexão realizada com sucesso")
    cur = conn.cursor()

    comando = '''CREATE TABLE Registro ( 
                        codigo INTEGER NOT NULL,
                        data DATE NOT NULL,
                        nome TEXT NOT NULL,
                        turma TEXT NOT NULL,
                        PRIMARY KEY(codigo)
                        );'''
    cur.execute(comando)
    conn.commit()
    print("Tabela Registros criada com sucesso")
    cur.close()
except:
    print("Tabela Registros criada com erro")



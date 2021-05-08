import sqlite3

def exibir_agenda():
    banco = sqlite3.connect('teste_agenda.db')
    cursor = banco.cursor()
    cursor.execute("SELECT time, data from agenda1")
    for i in cursor:
        print (i)
    banco.close()
    print("Esta é sua agenda atualizada!")

def inserir_na_agenda(time, data):
    try:
        banco = sqlite3.connect('teste_agenda.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO agenda1 VALUES('"+time+"', '"+data+"')")
        banco.commit()
        banco.close()
        print("Agenda atualizada")

    except sqlite3.Error as erro:
        print(f'Erro ao inserir: {erro}')
    print()
def deletar_na_agenda(time):
    try:
        banco = sqlite3.connect('teste_agenda.db')
        cursor = banco.cursor()
        cursor.execute("DELETE FROM agenda1 WHERE time = '"+time+"'")
        banco.commit()
        banco.close()
        print("Dados apagados com sucesso!")

    except sqlite3.Error as erro:
        print(f'Erro ao excluir: {erro}')
    print()
def atualizar_na_agenda(time, data):
    banco = sqlite3.connect('teste_agenda.db')
    cursor = banco.cursor()
    cursor.execute("UPDATE agenda1 SET data = '"+data+"' WHERE time = '"+time+"'")
    banco.commit()
    banco.close()
    print("Dados atualizados com sucesso")
    print()
# try:
# banco = sqlite3.connect('teste_agenda.db')
# cursor = banco.cursor()
#
# # cursor.execute("CREATE TABLE agenda1 (time text, data text)")
#
# # cursor.execute("INSERT INTO agenda1 VALUES('Cruzeiro', '20/05/2020')")
# #
#     cursor.execute("DELETE FROM agenda1 WHERE data = '14/12/2021'")
#     banco.commit()
#     banco.close()
#     print("messagem")
#
# except sqlite3.Error as erro:
#     print(f'Erro ao excluir: {erro}')


# cursor.execute("SELECT * FROM agenda1")
# print(cursor.fetchall())
time = input("Time: ")
data = input("Data do jogo: ")
#atualizar_na_agenda(time, data)
inserir_na_agenda(time, data)


#deletar_na_agenda(time)
# inserir_na_agenda("cruzeiro", "12/07/2021")
# exibir_agenda()
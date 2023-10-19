from mysql.connector import cursor
from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def cadastrar(mov, desc, valor, cat, data):
    conexao, cursor = conectar()
    #try: tentar
    try:
        sql = f"""INSERT INTO tb_informacoes
                (movimentacao, descricao, valor, categoria, dataMovimentacao)
                VALUES
                ('{mov}', '{desc}', '{valor}', '{cat}','{data}')
                """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    #except: caso falhe
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()
from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def consultar():
    conexao, cursor = conectar()
    try:
        cursor.execute("SELECT * FROM tb_informacoes")
        resultado = cursor.fetchall() #fetchall: todos os resultados
        return resultado
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha","Falha ao consultar!"+str(falha))
        return None
    finally:
        conexao.close()
        cursor.close()
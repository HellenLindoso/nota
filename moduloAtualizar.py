from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def atualizar(cod, mov, desc, valor, cat, data):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tb_informacoes
              SET movimentacao='{mov}', descricao='{desc}', valor='{valor}', 
              categoria='{cat}', dataMovimentacao='{data}' WHERE codigo='{cod}'
              """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar", "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()
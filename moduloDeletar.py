from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def deletar(id):
    conexao, cursor = conectar()
    try:
        sql = f"""DELETE FROM tb_informacoes
                     WHERE codigo='{id}'
                     """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Deletado", "Apagado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao deletar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()
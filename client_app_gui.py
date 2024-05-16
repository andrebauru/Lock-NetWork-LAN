import socket
import tkinter as tk
from tkinter import simpledialog, messagebox

SERVER_IP = '192.168.0.1'
SERVER_PORT = 5000
CLIENT_IP = '192.168.0.2'

def check_status():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))
    client.send(CLIENT_IP.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    client.close()
    return response == 'blocked'

def lock_screen():
    lock_window = tk.Toplevel()
    lock_window.title("Computador Bloqueado")
    lock_window.geometry("300x150")
    
    label = tk.Label(lock_window, text="Computador bloqueado. Digite a senha para desbloquear.")
    label.pack(pady=10)
    
    password_entry = tk.Entry(lock_window, show="*")
    password_entry.pack(pady=10)
    
    def unlock():
        password = password_entry.get()
        if password == 'senha_correta':  
            lock_window.destroy()
        else:
            messagebox.showerror("Erro", "Senha incorreta")
    
    unlock_button = tk.Button(lock_window, text="Desbloquear", command=unlock)
    unlock_button.pack(pady=10)
    
    lock_window.grab_set()
    root.wait_window(lock_window)

def main():
    if check_status():
        lock_screen()
    else:
        messagebox.showinfo("Acesso Permitido", "Acesso permitido.")

root = tk.Tk()
root.title("Cliente LAN House")

main_button = tk.Button(root, text="Verificar Acesso", command=main)
main_button.pack(pady=20)

root.mainloop()

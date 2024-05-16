import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
import netifaces

# Obter o endereço IP local automaticamente
def get_local_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_info = addresses[netifaces.AF_INET][0]
            if ip_info['addr'] != '127.0.0.1':
                return ip_info['addr']
    return '127.0.0.1'

SERVER_IP = get_local_ip()
SERVER_PORT = 5000
blocked_ips = []

# Função para tratar conexões de clientes
def handle_client(client_socket):
    client_ip = client_socket.recv(1024).decode('utf-8')
    if client_ip in blocked_ips:
        client_socket.send('blocked'.encode('utf-8'))
    else:
        client_socket.send('allowed'.encode('utf-8'))
    client_socket.close()

# Função para iniciar o servidor
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(5)
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Função para bloquear um IP
def block_ip(ip):
    blocked_ips.append(ip)
    update_blocked_list()

# Função para desbloquear um IP
def unblock_ip(ip):
    if ip in blocked_ips:
        blocked_ips.remove(ip)
        update_blocked_list()

# Função para atualizar a lista de IPs bloqueados na GUI
def update_blocked_list():
    blocked_list.delete(0, tk.END)
    for ip in blocked_ips:
        blocked_list.insert(tk.END, ip)

# Função para iniciar o servidor em uma thread separada
def start_server_thread():
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    messagebox.showinfo("Servidor", f"Servidor iniciado em {SERVER_IP}:{SERVER_PORT}")

# Função para adicionar IP bloqueado via GUI
def block_ip_gui():
    ip = simpledialog.askstring("Bloquear IP", "Digite o IP para bloquear:")
    if ip:
        block_ip(ip)

# Função para remover IP bloqueado via GUI
def unblock_ip_gui():
    selected_ip = blocked_list.get(tk.ACTIVE)
    if selected_ip:
        unblock_ip(selected_ip)

# Função para escanear a rede local e encontrar clientes
def scan_network():
    start_ip = start_ip_entry.get()
    end_ip = end_ip_entry.get()
    start_octets = start_ip.split('.')
    end_octets = end_ip.split('.')
    
    if len(start_octets) != 4 or len(end_octets) != 4:
        messagebox.showerror("Erro", "Formato de IP inválido")
        return

    network_prefix = '.'.join(SERVER_IP.split('.')[:-1])
    client_list.delete(0, tk.END)
    for i in range(int(start_octets[-1]), int(end_octets[-1]) + 1):
        ip = f"{network_prefix}.{i}"
        try:
            host_name = socket.gethostbyaddr(ip)[0]
            client_list.insert(tk.END, f"{ip} - {host_name}")
        except socket.herror:
            continue

# Função para escanear a rede em uma thread separada
def scan_network_thread():
    scan_thread = threading.Thread(target=scan_network)
    scan_thread.daemon = True
    scan_thread.start()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Administrador LAN")
root.geometry("600x400")

# Exibir IP do servidor
server_ip_label = tk.Label(root, text=f"IP do Servidor: {SERVER_IP}", font=("Arial", 12))
server_ip_label.pack(pady=10)

# Botões estilizados
style = ttk.Style()
style.configure("TButton", font=("Arial", 10))

start_button = ttk.Button(root, text="Iniciar Servidor", command=start_server_thread)
start_button.pack(pady=10)

block_button = ttk.Button(root, text="Bloquear IP", command=block_ip_gui)
block_button.pack(pady=10)

unblock_button = ttk.Button(root, text="Desbloquear IP", command=unblock_ip_gui)
unblock_button.pack(pady=10)

# Campos para inserir intervalo de IPs para escaneamento
ip_frame = tk.Frame(root)
ip_frame.pack(pady=10)

start_ip_label = tk.Label(ip_frame, text="Início do IP:")
start_ip_label.pack(side=tk.LEFT, padx=5)
start_ip_entry = tk.Entry(ip_frame)
start_ip_entry.pack(side=tk.LEFT, padx=5)

end_ip_label = tk.Label(ip_frame, text="Fim do IP:")
end_ip_label.pack(side=tk.LEFT, padx=5)
end_ip_entry = tk.Entry(ip_frame)
end_ip_entry.pack(side=tk.LEFT, padx=5)

scan_button = ttk.Button(root, text="Escanear Rede", command=scan_network_thread)
scan_button.pack(pady=10)

blocked_list_label = tk.Label(root, text="IPs Bloqueados", font=("Arial", 12))
blocked_list_label.pack(pady=5)

blocked_list = tk.Listbox(root)
blocked_list.pack(pady=10, fill=tk.BOTH, expand=True)

client_list_label = tk.Label(root, text="Clientes na Rede", font=("Arial", 12))
client_list_label.pack(pady=5)

client_list = tk.Listbox(root)
client_list.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()

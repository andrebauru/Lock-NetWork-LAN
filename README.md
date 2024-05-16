
# LAN Admin e Cliente

Este projeto consiste em dois programas Python que simulam o controle de acesso de computadores em uma LAN House. Um dos programas atua como o servidor administrador e o outro como o cliente. O administrador pode bloquear ou desbloquear o acesso dos clientes baseando-se no endereço IP.

## Requisitos

- Python 3.x
- Bibliotecas listadas em `requirements.txt`

Para instalar os requisitos, execute:
```bash
pip install -r requirements.txt
```

## Arquivos

### admin_server_gui.py

Este arquivo contém o código para o servidor administrador com interface gráfica. Ele permite que o administrador bloqueie ou desbloqueie endereços IP, exiba o próprio IP do servidor, e escaneie a rede local para encontrar clientes ativos.

### client_app_gui.py

Este arquivo contém o código para o cliente com interface gráfica. Ele verifica com o servidor se o acesso está bloqueado e, em caso positivo, solicita uma senha para desbloquear.

## Uso

### Executando o Servidor Administrador

1. Execute o arquivo `admin_server_gui.py`:
   ```bash
   python admin_server_gui.py
   ```

2. Na interface gráfica que aparecer:
   - Clique em "Iniciar Servidor" para começar a aceitar conexões de clientes.
   - Use os botões "Bloquear IP" e "Desbloquear IP" para gerenciar os acessos dos clientes.
   - Use o botão "Escanear Rede" para encontrar clientes na rede local, inserindo o intervalo de IPs a serem escaneados.

### Executando o Cliente

1. Execute o arquivo `client_app_gui.py`:
   ```bash
   python client_app_gui.py
   ```

2. Na interface gráfica do cliente, clique em "Verificar Acesso" para checar o status de bloqueio com o servidor.

## Transformando em um Executável

Para transformar os arquivos Python em executáveis, você pode usar a biblioteca `pyinstaller`. Siga os passos abaixo:

1. Instale o `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```

2. Gere o executável para o `admin_server_gui.py`:
   ```bash
   pyinstaller --onefile --windowed admin_server_gui.py
   ```

3. Gere o executável para o `client_app_gui.py`:
   ```bash
   pyinstaller --onefile --windowed client_app_gui.py
   ```

Os executáveis serão gerados na pasta `dist` dentro do diretório do projeto.

## Estrutura do Código

- `admin_server_gui.py`: Contém a lógica do servidor e a interface gráfica para gerenciamento de IPs bloqueados, exibição do IP do servidor e escaneamento da rede.
- `client_app_gui.py`: Contém a lógica do cliente para verificar o status de bloqueio e a interface gráfica para solicitar senha em caso de bloqueio.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork, crie um branch, adicione suas alterações e envie um pull request.


DONE.

## Licença

Direitos autorais ANDRETSC, me doe um cafe paypal andretsc@gmail.com.
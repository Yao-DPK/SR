import socket

# Configuration du client
HOST = '172.18.0.1'  # Adresse IP du serveur (localhost dans ce cas)
PORT = 65432        # Port sur lequel le serveur écoute

# Créer un socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connecter au serveur
    client_socket.connect((HOST, PORT))
    print(f"Connecté au serveur {HOST}:{PORT}")
    
    # Envoyer des données au serveur
    message = "Bonjour, serveur!"
    client_socket.sendall(message.encode('utf-8'))
    print(f"Message envoyé : {message}")
    
    # Recevoir une réponse
    data = client_socket.recv(1024)
    print(f"Réponse reçue : {data.decode('utf-8')}")

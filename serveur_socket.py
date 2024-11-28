import socket

# Configurer le serveur
HOST = '10.41.38.197'  # Adresse IP locale
PORT = 65432        # Port d'écoute

# Créer un socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Associer le socket à l'adresse et au port
    server_socket.bind((HOST, PORT))
    
    # Écouter les connexions
    server_socket.listen()
    print(f"Serveur en écoute sur {HOST}:{PORT}")
    
    # Accepter une connexion
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connexion acceptée depuis {addr}")
        while True:
            # Recevoir des données
            data = conn.recv(1024)  # Taille du buffer en octets
            if not data:
                break
            print(f"Données reçues : {data.decode('utf-8')}")
            
            # Répondre au client
            conn.sendall(data)  # Écho des données reçues

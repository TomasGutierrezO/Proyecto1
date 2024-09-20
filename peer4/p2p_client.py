import json
import sys
import os
import grpc  # Asegúrate de que gRPC esté instalado
import requests

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from proto import p2p_pb2, p2p_pb2_grpc  # Asegúrate de que esto coincida con tu estructura de directorios

class P2PClient:
    def __init__(self):
        with open("peer_config.json") as f:
            data = json.load(f)
            self.peer_id = data["peer_id"]
            self.ip = data["ip"]
            self.port = data["port"]
            self.files = data["files"]
            self.api_url = f"http://127.0.0.1:5000/"
        
        with open("../auth/users.json") as g:
            data2 = json.load(g)
            self.password = data2[self.peer_id]

    def login(self):
        username = input("Ingrese su nombre de usuario (peer_id): ")
        password = input("Ingrese su contraseña: ")
        response = requests.post(self.api_url + "login", json={"username": username, "password": password})
        if response.status_code == 200:
            return {'message': 'Sesión iniciada correctamente'}
        return {'Error': 'Ha ocurrido un error iniciando sesión'}

    def logout(self):
        username = input("Ingrese su nombre de usuario (peer_id): ")
        response = requests.post(self.api_url + "logout", json={"username": username})
        if response.status_code == 200:
            return {'message': 'Sesión cerrada correctamente'}
        return {'Error': 'Ha ocurrido un error cerrando sesión'}

    def index(self):
        username = input("Ingrese su nombre de usuario (peer_id): ")
        password = input("Ingrese su contraseña: ")
        response = requests.post(self.api_url + "index", json={"username": username, "password": password})
        if response.status_code == 200:
            return {'message': 'Se han actualizado los archivos del peer'}
        return {'Error': 'Ha ocurrido un error actualizando los archivos del peer'}

    def search(self):
        file_name = input("Ingrese el nombre del archivo que desea buscar: ")
        response = requests.get(self.api_url + "search", params={"file_name": file_name})
        if response.status_code == 200:
            peers = response.json()["peers"]
            for peer in peers:
                channel = grpc.insecure_channel(f"{peer['ip']}:{peer['port']}")
                stub = p2p_pb2_grpc.P2PServiceStub(channel)
                request = p2p_pb2.FileRequest(peer_id=self.peer_id, file_name=file_name)
                file_response = stub.GetFiles(request)

                # Imprimir peer, IP y puerto
                print(f"Peer {peer['peer_id']} tiene archivos: {file_response.files}")
                print(f"IP: {peer['ip']}, Puerto: {peer['port']}")
        else:
            print("No se encontraron peers con ese archivo")

def main():
    peer = P2PClient()
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Login")
        print("2. Logout")
        print("3. Indexar archivos")
        print("4. Buscar archivo")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            resultado = peer.login()
            print(resultado)
        elif opcion == "2":
            resultado = peer.logout()
            print(resultado)
        elif opcion == "3":
            resultado = peer.index()
            print(resultado)
        elif opcion == "4":
            peer.search()  # No es necesario almacenar el resultado aquí
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
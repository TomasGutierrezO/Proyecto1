import grpc
from concurrent import futures
import json
import sys
import os

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from proto import p2p_pb2, p2p_pb2_grpc

class P2PServerServicer(p2p_pb2_grpc.P2PServiceServicer):

    def GetFiles(self, request, context):
        # Cargar información de peer1 desde peer_config.json
        with open("peer_config.json") as f:
            data = json.load(f)
            peer_files = data['files']

        # Comprobar si el archivo solicitado existe en los archivos del peer
        if request.file_name in peer_files:
            return p2p_pb2.FileListResponse(files=[request.file_name], message="Archivo encontrado")
        else:
            return p2p_pb2.FileListResponse(files=[], message="Archivo no encontrado")

    def DownloadFile(self, request, context):
        """Maneja la solicitud de descarga de un archivo."""
        with open("peer_config.json") as f:
            data = json.load(f)
            peer_files = data['files']

        # Verificar si el archivo existe y devolverlo
        if request.file_name in peer_files:
            return p2p_pb2.FileResponse(file_name=request.file_name)
        else:
            return p2p_pb2.FileResponse(file_name="")
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    p2p_pb2_grpc.add_P2PServiceServicer_to_server(P2PServerServicer(), server)
    server.add_insecure_port('[::]:50004')  # Reemplazar con el número de puerto deseado
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

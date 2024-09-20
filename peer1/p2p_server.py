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
        # Load peer1 information (assuming data is in peer_config.json)
        with open("peer_config.json") as f:
            data = json.load(f)
            peer_files = data['files']

        # Check if requested file exists in peer1's files
        if request.file_name in peer_files:
            return p2p_pb2.FileListResponse(files=[request.file_name], message="Archivo encontrado")
        else:
            return p2p_pb2.FileListResponse(files=[], message="Archivo no encontrado")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    p2p_pb2_grpc.add_P2PServiceServicer_to_server(P2PServerServicer(), server)
    server.add_insecure_port('[::]:50001')  # Replace with desired port number
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
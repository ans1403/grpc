import grpc
from concurrent.futures import ThreadPoolExecutor
from service.user import UserServiceServicerImpl
from protobuf.user_pb2_grpc import add_UserServiceServicer_to_server


def main():
    server = grpc.server(ThreadPoolExecutor(max_workers=2))

    add_UserServiceServicer_to_server(UserServiceServicerImpl(), server)

    server.add_insecure_port("[::]:3000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()

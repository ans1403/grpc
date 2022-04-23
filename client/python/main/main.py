import argparse
import grpc
import os
import sys
from protobuf.user_pb2 import (
    UserSelectAllRequest,
    UserSelectByIdRequest,
)
from protobuf.user_pb2_grpc import UserServiceStub


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", type=str, required=True, help="Enter method name. ex: UserSelectAll")
    parser.add_argument("-i", "--id", type=int, help="Enter ID")
    args = parser.parse_args()

    method: str = args.method
    id: int = args.id

    grpc_server_host: str = os.getenv("GRPC_SERVER_HOST")
    grpc_server_port: str = str(os.getenv("GRPC_SERVER_PORT"))
    grpc_server_url = grpc_server_host + ":" + grpc_server_port

    with grpc.insecure_channel(grpc_server_url) as channel:
        stub = UserServiceStub(channel)

        if method == "UserSelectAll":
            request = UserSelectAllRequest()
            response = stub.selectAll(request)

        elif method == "UserSelectById":
            if id is not None:
                request = UserSelectByIdRequest(id=id)
                response = stub.selectAll(request)
                print(response.user.name)
            else:
                print("id is none")
                sys.exit(-1)

        else:
            print("unknown method")
            sys.exit(-2)


if __name__ == "__main__":
    main()

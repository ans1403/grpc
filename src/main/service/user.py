from protobuf.user_pb2_grpc import UserServiceServicer
from protobuf.user_pb2 import (
    User,
    UserSelectAllResponse,
    UserSelectByIdResponse,
)


data = {
    "1": {
        "id": 1,
        "name": "USER001",
        "user_type": "ADMIN"
    },
    "2": {
        "id": 2,
        "name": "USER002",
        "user_type": "NORMAL"
    },
    "3": {
        "id": 3,
        "name": "USER003",
        "user_type": "GUEST"
    }
}


class UserServiceServicerImpl(UserServiceServicer):

    def selectAll(self, _request, _context):
        result = []

        for d in data.values():
            user = User()
            user.id = d["id"]
            user.name = d["name"]
            user.user_type = User.UserType.Value(d["user_type"])
            result.append(user)

        return UserSelectAllResponse(error=False, user=result)

    def selectById(self, request, _context):
        id = str(request.id)

        if id not in data:
            return UserSelectByIdResponse(error=True, message="Not Found")

        user = data[id]
        result = User()
        result.id = user["id"]
        result.name = user["name"]
        result.user_type = User.UserType.Value(user["user_type"])

        return UserSelectByIdResponse(error=False, user=result)

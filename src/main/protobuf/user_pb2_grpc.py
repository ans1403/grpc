# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_pb2 as user__pb2


class UserServiceStub(object):
    """ユーザサービス
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.selectAll = channel.unary_unary(
                '/user.UserService/selectAll',
                request_serializer=user__pb2.UserSelectAllRequest.SerializeToString,
                response_deserializer=user__pb2.UserSelectAllResponse.FromString,
                )
        self.selectById = channel.unary_unary(
                '/user.UserService/selectById',
                request_serializer=user__pb2.UserSelectByIdRequest.SerializeToString,
                response_deserializer=user__pb2.UserSelectByIdResponse.FromString,
                )


class UserServiceServicer(object):
    """ユーザサービス
    """

    def selectAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def selectById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'selectAll': grpc.unary_unary_rpc_method_handler(
                    servicer.selectAll,
                    request_deserializer=user__pb2.UserSelectAllRequest.FromString,
                    response_serializer=user__pb2.UserSelectAllResponse.SerializeToString,
            ),
            'selectById': grpc.unary_unary_rpc_method_handler(
                    servicer.selectById,
                    request_deserializer=user__pb2.UserSelectByIdRequest.FromString,
                    response_serializer=user__pb2.UserSelectByIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """ユーザサービス
    """

    @staticmethod
    def selectAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/selectAll',
            user__pb2.UserSelectAllRequest.SerializeToString,
            user__pb2.UserSelectAllResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def selectById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/selectById',
            user__pb2.UserSelectByIdRequest.SerializeToString,
            user__pb2.UserSelectByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

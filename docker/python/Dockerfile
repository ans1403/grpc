FROM python:3.10.4-bullseye

WORKDIR /usr/local/grpc/

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt && \
    \
    useradd -s /bin/bash appuser && \
    \
    echo 'python -m grpc_tools.protoc -I/usr/local/grpc/src/main/proto --python_out=/usr/local/grpc/src/main/protobuf --grpc_python_out=/usr/local/grpc/src/main/protobuf /usr/local/grpc/src/main/proto/user.proto' > /usr/local/bin/grpc-gen && \
    chown appuser:appuser /usr/local/bin/grpc-gen && \
    chmod +x /usr/local/bin/grpc-gen

USER appuser

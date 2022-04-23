FROM python:3.10.4-slim-bullseye

WORKDIR /usr/local/grpc/

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt && \
    \
    useradd -s /bin/bash appuser && \
    \
    { \
        echo 'python -m grpc_tools.protoc \'; \
        echo '    -I/usr/local/grpc/protos \'; \
        echo '    --python_out=/usr/local/grpc/src/main/protobuf \'; \
        echo '    --grpc_python_out=/usr/local/grpc/src/main/protobuf \'; \
        echo '    /usr/local/grpc/protos/$1.proto'; \
    } > /usr/local/bin/grpc-gen && \
    \
    chown appuser:appuser /usr/local/bin/grpc-gen && \
    chmod +x /usr/local/bin/grpc-gen

USER appuser

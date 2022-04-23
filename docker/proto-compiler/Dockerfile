FROM --platform=linux/x86_64 debian:bullseye

ENV PATH="$PATH:/usr/local/go/bin:/root/go/bin"

WORKDIR /usr/local/grpc/

RUN apt-get update && apt-get install -y \
        protobuf-compiler \
        python3 \
        python3-pip \
        wget \
    && \
    \
    wget -P /tmp https://go.dev/dl/go1.18.1.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf /tmp/go1.18.1.linux-amd64.tar.gz && \
    go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28 && \
    go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2 && \
    \
    pip3 install grpcio==1.44.0 grpcio-tools==1.44.0 && \
    \
    { \
        echo 'CURDIR=$(pwd)'; \
        echo 'cd /usr/local/grpc/protos'; \
        echo 'protoc --go_out=../protobufs --go_opt=paths=source_relative \'; \
        echo '    --go-grpc_out=../protobufs --go-grpc_opt=paths=source_relative \'; \
        echo '    *.proto'; \
        echo 'python3 -m grpc_tools.protoc \'; \
        echo '    -I. \'; \
        echo '    --python_out=../protobufs \'; \
        echo '    --grpc_python_out=../protobufs \'; \
        echo '    *.proto'; \
        echo 'cd $CURDIR'; \
    } > /usr/local/bin/proto-compile && \
    \
    chmod +x /usr/local/bin/proto-compile

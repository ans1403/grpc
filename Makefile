
PROTO_COMPILER_IMAGE_NAME := proto-compiler
PROTO_COMPILER_IMAGE_TAG  := 1.0.0


.PHONY: build-proto-complier

build-proto-complier:
	@ docker build -t ${PROTO_COMPILER_IMAGE_NAME}:${PROTO_COMPILER_IMAGE_TAG} ./docker/proto-compiler


.PHONY: proto-compile

proto-compile:
	@ docker run --rm -it \
		--platform linux/x86_64 \
		-v ${CURDIR}:/usr/local/grpc \
		${PROTO_COMPILER_IMAGE_NAME}:${PROTO_COMPILER_IMAGE_TAG} \
		bash -c proto-compile

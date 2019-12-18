# gRPC

### How to start?
- create venv
- pip install -r requirements.txt
- start server from grpc-services/users/run-server.sh     (make it executable incase...)
- start cleint from grpc-services/users/run-client.sh     (In different terminal)
- In third terminal use tcpdump for local host (sudo tcpdump -i lo) to monitor traffic port 50051
















Implemented Client streaming RPCs where the client writes a sequence of messages and sends them to the server, again using a provided stream.

This is better- Bidirectional streaming RPCs where both sides send a sequence of messages using a read-write stream.

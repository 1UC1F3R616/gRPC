# gRPC

### How to start?
- create venv
- pip install -r requirements.txt
- start server from grpc-services/users/run-server.sh     (make it executable incase...)
- start cleint from grpc-services/users/run-client.sh     (In different terminal)
- In third terminal use tcpdump for local host (sudo tcpdump -i lo) to monitor traffic port 50051










Deadlines/Timeouts

gRPC allows clients to specify how long they are willing to wait for an RPC to complete before the RPC is terminated with the error DEADLINE_EXCEEDED. On the server side, the server can query to see if a particular RPC has timed out, or how much time is left to complete the RPC.

How the deadline or timeout is specified varies from language to language - for example, not all languages have a default deadline, some language APIs work in terms of a deadline (a fixed point in time), and some language APIs work in terms of timeouts (durations of time).

--> Terminate as soon as server is triggered



Implemented Client streaming RPCs where the client writes a sequence of messages and sends them to the server, again using a provided stream.

This is better- Bidirectional streaming RPCs where both sides send a sequence of messages using a read-write stream.

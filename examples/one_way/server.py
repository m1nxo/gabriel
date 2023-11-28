# this code appears to set up a server using ZeroMQ and WebSockets, configuring logging settings and defining parameters for the server's operation, including the ports and processing limits

import common
from gabriel_server.network_engine import server_runner

# string format used to create a ZeroMQ (ZMQ) address
ZMQ_ADDRESS_FORMAT = 'tcp://*:{}'

def main():
    # configure logging settings
    common.configure_logging()

    # server will listen for connections
    zmq_address = ZMQ_ADDRESS_FORMAT.format(common.ZMQ_PORT)

    # the port number for WebSocket communication, ZMQ address, control the number of tokens or available processing resources for incoming requests, setting a maximum size for the input queue
    server_runner.run(common.WEBSOCKET_PORT, zmq_address, num_tokens=2, input_queue_maxsize=60)

if __name__ == '__main__':
    main()

# electrum_client.py

import json
import socket


class ElectrumClient:
    def __init__(self, server="rostrum.cauldron.quest", port=50001):
        self.s = socket.create_connection((server, port))
        self.f = self.s.makefile('r')
        self.id = 0

    def call(self, method, *args):
        req = {
            'id': self.id,
            'method': method,
            'params': list(args),
        }
        msg = json.dumps(req) + '\n'
        self.s.sendall(msg.encode('ascii'))

        # Read response
        response = self.f.readline()
        if not response:
            raise ValueError("Empty response from Electrum server")

        return json.loads(response)

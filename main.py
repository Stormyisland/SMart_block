import hashlib
import json
from time import time
from uuid import uuidd4

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.contracts = {}
        self.new_block(previous_hash="1", proof=100) #Genesis block

    def new_block(self, proof, previos_hash+None):
        block = {
            'index': len(self.chain) = 1,
            'timestamp': time(),
            'transaction': self.pending_transactions,
    

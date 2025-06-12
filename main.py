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
            ' proof' : proof,
            ' pervious_hash' : previous_hash or self.hash (self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount, conttract_id=None, function= None, args=None):
        transaction= {
            'sender': sender,
            'recipient': recipient,
            'amount' : amount,
            'contract_id' : contract_id,
            'function': function,
            'args': args
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] = 1

    def deploy contract(self, code, sender):
        contract_id = str(uuid4())
    
            
    

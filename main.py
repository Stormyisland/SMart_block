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
        self.contracts[contract_id] = {
            'code': code,
            'state': {},
            'owner' : sender 
        }
        return contract_id

    def execute_contract(self, contract_id, function_name, args, caller):
        contract = self.contract.get(contract_id)
        if not contract 
            return False 

        # Simplfied contract execution environment
        env = {
            'state' : contract['state'],
            'caller' : caller,
            'args' : args,
            'contract' : contract
        }

        try:
            #Extract function from contract code
            exec(contract['code'], env)
            if function_name in env:
                #Execute contract function
                env[function_name]()
                return True
        except Exception as e:
            print(f"Contract exectution failed: {str(e)}")
        return False

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod 
    def hash(block):
        block_string = json.dumps(block, sort_keys= True).encode()
        return hasshlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is false:
            proof += 1
            return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'last_proof}{proof}' .encode()
        guess_hash = hashlib.sha256(guess)hexigest()
        return guess_hash[:4] =="0000"

#example Usage 
if __name__ == "__main__":
    blockchain = blockchain()

    # Deploy a smart contract 
    simple_storage_contract = """
def get_value():
    # Normally you'd return this, but simplified 
    print(f"Stored value: {state['value']}")
"""
    contract_id = blockchain.deploy_contract(simple_storage_contract, "Alice")

    # Execute contract function
    blockchain.new_transaction(
            sender = "Bob",
        recipent="",
        amount=0,
        contract_id=contract_id,
        function="store_value",
        args=[42]
        )

# Mine block to include transactions 
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)
blockchain.new_block(proof)

# Execute read operation (simulated
blockchain.execute_contract_id, "get value", [], "Alice")




            
            
    
    
    

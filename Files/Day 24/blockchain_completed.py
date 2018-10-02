import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from urllib.parse import urlparse
import requests

class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()
        #calling the set constructor to create a set. (immutable and idempotent)
        #create the genesis block here
        self.new_block(previous_hash = '1', proof = 100)

    
    def new_block(self, proof, previous_hash = None):
        #creating a new block and adding it to the blockchain.
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : self.current_transactions,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1]),
        }
        # reset the current list of transactions.
        self.current_transactions = []

        self.chain.append(block)
        return block
    

    def new_transaction(self, sender, recipient, amount):
        #adding a new transaction to the list of transactions.
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
        })

        return self.last_block['index'] + 1

    def register_node(self, address):
        """
        Add a new node to the list of nodes
        :param address: Address of node. Eg. 'http://192.168.0.5:5000'
        """
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')
    
    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            #check that the hash of block is correct
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False
            
            #check that the proof of work is correct.
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False
            last_block = block
            current_index += 1
        return True

    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.

        :return: <bool> True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None
        # We are only looking for chains longer than ours.
        max_length = len(self.chain)

        #grab and verify the chain from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                #check if the length is longer nad the chian is valid.
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        
        # replace our chain if we discovered a new, valid , longer chain.
        if new_chain:
            self.chain = new_chain
            return True

        return False

    
    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]

    @staticmethod
    def hash(block):
        #hashes a block
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        #make sure the dict is ordered, or we'll have inconsistent hashes.
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def proof_of_work(self, last_block):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof
         
        :param last_block: <dict> last Block
        :return: <int>
        """

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        """
        Validates the Proof
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
        
# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-','')

# Instantiate the Block
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    #we run POW algorithm to get the next proof
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)

    #now, we must receive a reward for finding the proof
    # sender is 0 to signify new coin
    blockchain.new_transaction(
        sender = "0",
        recipient = node_identifier,
        amount = 1,
    )

    #forge the new blockchain be adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response),200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    #check that the req fields are in posted data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    #if everythin is fine, create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to block {index}'}
    return jsonify(response), 201
    

@app.route('/chain', methods = ['GET'])
def full_chain():
    response = {
        'chain' : blockchain.chain,
        'length' : len(blockchain.chain),
    }
    return jsonify(response),200

@app.route('/nodes/register', methods = ['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error! Please supply a valid chain of nodes.", 400
    
    for node in nodes:
        blockchain.register_node(node)
    
    response = {
        'message' : 'New Nodes have been added.',
        'total_nodes' : list(blockchain.nodes),
    }

    return jsonify(response), 201

@app.route('/nodes/resolve', methods = ['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    
    if replaced:
        response = {
            'message' : 'Our chain was replaced.',
            'new_chain' : blockchain.chain
        }
    else:
        response = {
            'message' : 'Our chain is authoritative',
            'chain' : blockchain.chain
        }
    
    return jsonify(response), 200


if __name__=='__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port = 5000)
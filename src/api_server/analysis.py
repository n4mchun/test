from src.utils.etherscan import fetch_account_api, TOKEN_TX_ACTION, TX_LIST_ACTION
from src.utils.constants import CHAIN_ID_MAP, FUNCTION_SIGNATURE_MAP
from src.utils.types import Edge, Node
from dataclasses import dataclass
from typing import List

@dataclass
class Graph:
    nodes: List[Node]
    edges: List[Edge]

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, address: str, chain_id: int):
        chain_name = CHAIN_ID_MAP.get(str(chain_id))
        node_id = f'{chain_name}-{address}'

        if node_id in [_node.id for _node in self.nodes]:
            return
        
        self.nodes.append(Node(
            id=node_id,
            address=address,
            chain=chain_name
        ))

    def add_edge(self, edge: Edge):
        self.edges.append(edge)
    
    def to_dict(self):
        return {
            'nodes': [node.to_dict() for node in self.nodes],
            'edges': [edge.to_dict() for edge in self.edges],
        }

def classify_transaction_type(tx: dict) -> str:
    input_data = tx.get('input', '0x')
    value = int(tx.get('value', 0))

    if input_data == '0x' and value > 0:
        return 'Native'
    
    function_signature = input_data[:10]
    if function_signature in FUNCTION_SIGNATURE_MAP:
        return FUNCTION_SIGNATURE_MAP[function_signature]['type']
    
    return 'Normal'

def analyze_address(address: str, chain_id: int) -> dict:
    graph = Graph()

    graph.add_node(address, chain_id)

    # ERC20
    tx_list = fetch_account_api(address, chain_id, TOKEN_TX_ACTION)
    for tx in tx_list:
        amount_wei = int(tx.get('value', 0))
        if amount_wei == 0:
            continue

        from_address, to_address = tx.get('from'), tx.get('to')
        for address in [from_address, to_address]:
            graph.add_node(address, chain_id)
        
        decimals = int(tx.get('tokenDecimal', 0))
        amount = str(amount_wei / (10 ** decimals))

        graph.add_edge(Edge(
            tx_hash=tx.get('hash'),
            from_address=from_address,
            to_address=to_address,
            amount=amount,
            timestamp=int(tx.get('timeStamp')),
            token_address=tx.get('contractAddress'),
            token_symbol=tx.get('tokenSymbol'),
            tx_type='ERC20_TRANSFER'
        ))
    
    # Normal tx
    tx_list = fetch_account_api(address, chain_id, TX_LIST_ACTION)
    for tx in tx_list:
        tx_type = classify_transaction_type(tx)

        if tx_type == 'ERC20_TRANSFER':
            continue

        from_address, to_address = tx.get('from'), tx.get('to')
        for address in [from_address, to_address]:
            graph.add_node(address, chain_id)
        
        graph.add_edge(Edge(
            tx_hash=tx.get('hash'),
            from_address=tx.get('from'),
            to_address=tx.get('to'),
            amount=str(int(tx.get('value', 0)) / (10 ** 18)),
            timestamp=int(tx.get('timeStamp')),
            token_address='',
            token_symbol='',
            tx_type=tx_type
        ))

    return graph.to_dict()
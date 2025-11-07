from dataclasses import dataclass

@dataclass
class Node:
    id: str
    address: str
    chain: str
    label: str = None
    isContract: bool = False
    riskScore: int = 0
    riskLabels: str = None

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
            'chain': self.chain,
            'label': self.label,
            'isContract': self.isContract,
            'riskScore': self.riskScore,
            'riskLabels': self.riskLabels
        }

@dataclass
class Edge:
    tx_hash: str
    from_address: str
    to_address: str
    amount: str
    timestamp: int
    token_address: str
    token_symbol: str
    tx_type: str

    def to_dict(self):
        return {
            'tx_hash': self.tx_hash,
            'from_address': self.from_address,
            'to_address': self.to_address,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'token_address': self.token_address,
            'token_symbol': self.token_symbol,
            'tx_type': self.tx_type
        }
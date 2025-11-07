from flask import Flask, request, jsonify
from src.api_server import analysis
from src.utils import constants

app = Flask(__name__)

@app.route('/api/fund-flow', methods=['POST'])
def fund_flow_api():
    try:
        data = request.get_json()
        address = data.get('address') if data else None
        chain_name = (data.get('chain') or '').lower() if data else ''

        if not address or not chain_name:
            return jsonify({'error': 'Missing address or chain in request body.'}), 400
        
        chain_id = constants.CHAIN_ID_MAP.get(chain_name)
        if chain_id is None:
            supported_chains = ", ".join(constants.CHAIN_ID_MAP.keys())
            return jsonify({'error': f'Unsupported chain: {chain_name}. Supported chains: {supported_chains}'}), 400
        
        result = analysis.analyze_address(address, chain_id)
        return jsonify({'data': result, 'success': True, 'error': None}), 200
    except Exception as e:
        return jsonify({'data': None, 'success': False, 'error': str(e)}), 500
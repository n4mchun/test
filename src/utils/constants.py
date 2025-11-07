from typing import Any

FUNCTION_SIGNATURE_MAP: dict[str, dict[str, Any]] = {
    '0xa9059cbb': { # ERC20 transfer
        'function': 'transfer(address to,uint256 value)',
        'type': 'ERC20_TRANSFER',
    },
    '0x3593564c': { # Uniswap V4 | PancakeSwap | ...
        'function': 'execute(bytes commands,bytes[] inputs,uint256 deadline)',
        'type': 'SWAP',
    },
    '0x4d8160ba': { # DeBridge
        'function': 'strictlySwapAndCall(address _srcTokenIn,uint256 _srcAmountIn,bytes _srcTokenInPermitEnvelope,address _srcSwapRouter,bytes _srcSwapCalldata,address _srcTokenOut,uint256 _srcTokenExpectedAmountOut,address _srcTokenRefundRecipient,address _target,bytes _targetData)',
        'type': 'BRIDGE',
    },
    '0xc7c7f5b3': { # USDT0 bridge
        'function': 'send(tuple _sendParam,tuple _fee,address _refundAddress)',
        'type': 'BRIDGE',
    },
    '0xae328590': { # Relay bridge (integrated by other bridge -> `integrator` in _bridgeData)
        'function': 'startBridgeTokensViaRelay(tuple _bridgeData,tuple _relayData)',
        'type': 'BRIDGE',
    },
    '0x733214a3': { # LI.FI: LiFi Diamond
        'function': 'swapTokensSingleV3ERC20ToNative(bytes32 _transactionId,string _integrator,string _referrer,address _receiver,uint256 _minAmountOut,tuple _swapData)',
        'type': 'SWAP'
    },
    '0xaf7060fd': { # LI.FI: LiFi Diamond
        'function': 'swapTokensSingleV3NativeToERC20(bytes32 _transactionId,string _integrator,string _referrer,address _receiver,uint256 _minAmountOut,tuple _swapData)',
        'type': 'SWAP'
    },
    '0x4666fc80': { # LI.FI: LiFi Diamond
        'function': 'swapTokensSingleV3ERC20ToERC20(bytes32 _transactionId,string _integrator,string _referrer,address _receiver,uint256 _minAmountOut,tuple _swapData)',
        'type': 'SWAP'
    }
}

ADDRESS_LABEL_MAP: dict[str, dict[str, Any]] = {
    '1': { # Ethereum
        '0x65b382653f7C31bC0Af67f188122035461ec9C76': 'PancakeSwap: Universal Router',
        '0x66a9893cC07D91D95644AEDD05D03f95e1dBA8Af': 'Uniswap V4: Universal Router',
        '0x6C96dE32CEa08842dcc4058c14d3aaAD7Fa41dee': 'USDT0: OAdapterUpgradeable',
    },
    # ...
}

CHAIN_ID_MAP: dict[str, str] = {
    '1': 'Ethereum',
    '999': 'HyperEVM',
    '42161': 'Arbitrum',
}
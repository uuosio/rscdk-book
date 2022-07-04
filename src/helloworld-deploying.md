# Deploying

## Create a test account
```
https://monitor.jungletestnet.io/#account
```

## Receive some test token
```
https://monitor.jungletestnet.io/#faucet
```

## Get Some Free CPU Resource
```
https://monitor.jungletestnet.io/#powerup
```

## Deploy the Contract and Call Action on Chain

Use the following code to deploy the test contract and interact with the test contract with `sayhello` action.
Change private key and `test_account` as demand.

[deploy.py](https://github.com/uuosio/rscdk-book/blob/main/demos/helloworld/deploy.py)

```python
#{
# 'private': '5Hzw656H9s9KUjqPXrSqtHtWVw4VV1YVF2VbKrTUXe65GsYwQgq',
# 'public': 'EOS57ijzHFYRf7ibbfVdzSHN2mzyC8bgrGNDdM4DWPS8XBp39vniX'
# }
import json
import base64
from pyeoskit import eosapi, wallet

eosapi.set_node('https://jungle3.cryptolions.io:443')
wallet.import_key('test', '5Hzw656H9s9KUjqPXrSqtHtWVw4VV1YVF2VbKrTUXe65GsYwQgq')

test_account = 'rusttesttest'

with open('./target/helloworld.wasm', 'rb') as f:
    wasm = f.read()
with open('./target/helloworld.abi', 'r') as f:
    abi = f.read()

info = eosapi.get_account(test_account)
ram_quota = info['ram_quota']

if len(wasm) * 10 + 4000 > ram_quota:
    ram_bytes = len(wasm) * 10 + 4000 - ram_quota
    print('ram_bytes:', ram_bytes)
    ram_bytes += 1000
    args = {
        'payer': test_account,
        'receiver': test_account,
        'bytes': ram_bytes,
    }
    eosapi.push_action('eosio', 'buyrambytes', args, {test_account: 'active'})

code = eosapi.get_raw_code_and_abi(test_account)['wasm']
if not base64.standard_b64decode(code) == wasm:
    eosapi.deploy_contract(test_account, wasm, abi)

r = eosapi.push_action(test_account, 'sayhello', {'name': 'rust'}, {test_account: 'active'})
print(r['processed']['elapsed'])
print(r['processed']['action_traces'][0]['console'])
```


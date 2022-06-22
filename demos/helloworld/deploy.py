
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
# print(json.dumps(info, indent=' '))
ram_quota = info['ram_quota']

# eosapi.transfer('rusttest1113', test_account, 100.0, payer=test_account)
# import sys;sys.exit(0)

if info['cpu_limit']['available'] < 1000:
    args = {
        'from': test_account,
        'receiver': test_account,
        'stake_net_quantity': '50.0000 EOS',
        'stake_cpu_quantity': '10.0000 EOS',
        'transfer': False,
    }
    eosapi.push_action('eosio', 'delegatebw', args, {test_account: 'active'})

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
    eosapi.deploy_contract('rusttesttest', wasm, abi)

r = eosapi.push_action('rusttesttest', 'sayhello', {'name': 'rust'}, {test_account: 'active'})
print(r['processed']['elapsed'])
print(r['processed']['action_traces'][0]['console'])

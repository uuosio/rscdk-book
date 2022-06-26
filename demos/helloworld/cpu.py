
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

info = eosapi.get_account(test_account)
# print(json.dumps(info, indent=' '))
ram_quota = info['ram_quota']

args = {
    'from': test_account,
    'receiver': test_account,
    'stake_net_quantity': '290.0000 EOS',
    'stake_cpu_quantity': '10.0000 EOS',
    'transfer': False,
}
eosapi.push_action('eosio', 'delegatebw', args, {test_account: 'active'})

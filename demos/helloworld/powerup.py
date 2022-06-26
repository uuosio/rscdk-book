import json
import base64
from pyeoskit import eosapi, wallet

eosapi.set_node('https://jungle3.cryptolions.io:443')
wallet.import_key('test', '5Hzw656H9s9KUjqPXrSqtHtWVw4VV1YVF2VbKrTUXe65GsYwQgq')

test_account = 'rusttesttest'
info = eosapi.get_account(test_account)

args = dict(
    payer = test_account,
    receiver = test_account,
    days = 1,
    net_frac = 2000000000,
    cpu_frac = 8000000000,
    max_payment = '1.0000 EOS',
)

eosapi.push_action('eosio', 'powerup', args, {test_account: 'active'})

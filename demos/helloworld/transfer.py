
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
eosapi.transfer('rusttest1111', test_account, 100.0, payer=test_account)
eosapi.transfer('rusttest1112', test_account, 100.0, payer=test_account)
eosapi.transfer('rusttest1113', test_account, 100.0, payer=test_account)

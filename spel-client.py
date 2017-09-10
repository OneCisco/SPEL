from note import Note # à coder
from crypto import sign, verify # à coder
import requests

# pour l'exemple
URL_SERVER = 'http://localhost' 
MY_PRIVATE_KEY = 'XXXX'

# get data for payment # à coder
merchant_key = 'YYYY'
data = {'montant': 1, 'cle': merchant_key}

# send a request to the server and get back the note
r = requests.get(url, data = data)
response_from_server = r.content() # ou r.json() ?
note = Note(response_from_server) # il faudra surement reformater response

# verify note signature
if not verify(note, note.transactions[-1]['signature']):
    raise SignatureError # à coder

# create new transaction and sign
new_transaction = {'cle': merchant_key, 'hash_info_payment': None, 'signature': None}
note.transactions.append(new_transaction)
my_sig = sign(note, MY_PRIVATE_KEY)
note.transactions[-1]['signature'] = my_sig

# send to merchant
note.display_QR_code() # une manière de faire parmi d'autres

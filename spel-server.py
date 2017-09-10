from note import Note # à coder
from crypto import sign # à coder
from bottle import Bottle, run # pour faire un mini-serveur web

# pour l'exemple
MY_PRIVATE_KEY = 'ZZZZZ'

# j'ai jamais fait de site de ma vie, j'ai piqué ca sur sametmax
app = Bottle()

@app.route('/')
def return_note(client_data):
    """
    Create a promissory note from data, sign it with the private key, and send it back to the client.
    :param data: dictonnary (or json file?) containing data provided by the client
    :return: some object (json file?) representing the note, send to the client via internet
    """
    
    # some formatting/checking of "client_data"
    pass
    
    # create note
    note = Note(client_data)
    
    # create first transaction and sign
    new_transaction = {'cle': client_data['public_key'], 'hash_info_payment': None, 'signature': None}
    note.transactions.append(new_transaction)
    my_sig = sign(note, MY_PRIVATE_KEY)
    note.transactions[-1]['signature'] = my_sig
    
    # return to client
    return note.display_web_format() # dans un format qui va bien dans tuyau internet, genre json

if __name__ == "__main__":
    run(app, host='localhost', port=8080)
    

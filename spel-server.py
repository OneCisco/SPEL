from note import Note # à coder
from crypto import sign # à coder
from bottle import Bottle, run # pour faire un mini-serveur web

# j'ai jamais fait de site de ma vie, j'ai piqué ca sur sametmax

app = Bottle()

@app.route('/')
def return_note(client_data):
    """
    Create a promissory note from data, sign it with the private, and send it back to the client.
    :param data: dictonnary (or json file?) containing data provided by the client
    :return: some object (json file?) representing the note, send to the client via internet
    """
    
    # some formatting/checking of "client_data"
    pass
    
    # create note
    note = Note(client_data)
    
    # sign note
    my_sig = sign(note, key)
    note.set_signature(my_sign)
    
    # return to client
    return note.send() # faut que ca aille dans le tuyau internet

if __name__ == "__main__":
    run(app, host='localhost', port=8080)
    

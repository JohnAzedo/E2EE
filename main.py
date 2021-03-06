# %%
from typing import List
from datetime import datetime as Datetime


# %%
class Client:
    _private_key: str
    public_key: str
    address: str


# %%
# Encrypted fields : [text, date]

class Message:
    text: str
    date: Datetime
    sender: Client


# %%
class Chat:
    _messages: List[Message]
    _participants: List[Client]

    

# %%
class Server:
    _chats: List[Chat]
    _clients: List[Client]


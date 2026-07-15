from os import environ 

class Config:
    API_ID = environ.get("API_ID", "36739180")
    API_HASH = environ.get("API_HASH", "a4974292591c16f7d28ad09c16501f9c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8697819852:AAH9xXxO-yFDve6hIWwPhV1_paGG8EsL0p0) 
    BOT_SESSION = environ.get("1BVts0I8BuxHIhsAxeCq9IRWl0yEhILCC-uE_fNudtIVCetY_N0w00M78vvbW35_N N700fYeAMnJASsSPiDh9Z9Sz4MLB9c5ssvjkvpyqAh_fkHmn1YW7KHgzFqWgd65sC BIGWG-NrV1H1uzwXbgbPUWPHUJj-nHy7ySQ7W6dNqWxRy8NhDFLzeha6jN1xffS6P ne_ORDe5uDu7HuIAUu02S9KOcHkMEHa1Fxw1FlZcSTVNrlxBgjvQzku8J4q-FNSXH R6l8WiXQ2turGxf0088Ket_dhZaaQ2RCHzft2EqNH7CtSoDzzJduJIf0KVcd0P_OD o-COR6C2W3L6RMIcz6AZXQraQjw=", "bot") 
    DATABASE_URI = environ.get(
    "DATABASE",
    "mongodb+srv://Myboosbot:teramerasath24@cluster0.xowzpr4.mongodb.net/forward-bot?retryWrites=true&w=majority"
)
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8215283099').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    

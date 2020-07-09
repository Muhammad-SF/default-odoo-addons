{
    "name": """Always show reply button""",
    "summary": """Got a message out of a Record? Now you can reply to it too!""",
    "category": "Discuss",
    "version": "1.0.0",
    "author": "Yevhen Pechurin",
    "license": "LGPL-3",
    "price": 0.0,
    "currency": "EUR",
    "depends": [
        "mail",
    ],
    "data": [
        'views/assets_backend.xml'
    ],
    "qweb": [
        "static/src/xml/mail_message_reply.xml",
    ],
    "installable": True,
}

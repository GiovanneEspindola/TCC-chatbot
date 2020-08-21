import nltk
from nltk.chat.util import Chat, reflections
reflections_pt = {'eu': 'você',
                  'eu sou': 'você é',
                  'eu era': 'você era',
                  "eu iria": 'você iria',
                  "eu irei": 'você irá',
                  'meu': 'seu',
                  'você': 'eu',
                  'você é': 'eu sou',
                  'você era': 'eu era',
                  "você irá": 'eu irei',
                  'seu': 'meu'}
pares = [
    [
     r'oi|olá',
     ['olá', 'como vai?', 'tudo bem?']
    ],
    [
        r'tudo bem?',
        ['bom saber']
    ],
    [
     r'qual é o seu nome?',
     ['Meu nome é Chat e eu sou um chatbot']
    ],
    [
     r'(.*) idade?|(.*)anos',
     ['Não tenho idade pois sou um chatbot']
    ],
    [
     r'meu nome é (.*)',
     ['Olá %1, como você está hoje?']
    ],
    [
     r'eu trabalho na empresa (.*)',
     ['Eu conheço a empresa %1']
    ],
    [
     r'(.*) (cidade|país)',
     ['Porto União, Brasil']
    ],
    [
     r'quit',
     ['Até breve', 'Foi bom conversar com você. Até breve!']
    ]
]
print('Olá, sou o chat!')
chat = Chat(pares, reflections_pt)
chat.converse()
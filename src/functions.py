import re
from random import random

def idiotizer_i_char(text) -> str:
    idiot_text = re.sub('[aeou]', 'i', text)
    idiot_text = re.sub('[áéóú]', 'í', idiot_text)
    idiot_text = re.sub('[àèòù]', 'ì', idiot_text)
    idiot_text = re.sub('[AEOU]', 'I', idiot_text)
    idiot_text = re.sub('[ÁÉÓÚ]', 'Í', idiot_text)
    idiot_text = re.sub('[ÀÈÒÙ]', 'Ì', idiot_text)
    return idiot_text


def idiotizer_casing_random(text) -> str:
    idiot_text = ''.join(c.upper() if random() > 0.5 else c for c in text)
    idiot_text = ''.join(c.lower() if random() >
                        0.5 else c for c in idiot_text)
    return idiot_text

def idiotizer_casing(text) -> tuple[str, str]:

    idiot_text_1 = ''
    idiot_text_2 = ''
    for index, item in enumerate(text):
        if index % 2 == 0:
            idiot_text_1 += item.upper()
            idiot_text_2 += item.lower()
        else:
            idiot_text_1 += item.lower()
            idiot_text_2 += item.upper()

    return idiot_text_1, idiot_text_2
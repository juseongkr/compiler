#data = "hanguk woigukweo"
#data = "hangukwoigukweodaehakgyo keompyuteogowhakbu"
data = "hangukwoigukweodaehakgyo keompyuteogowhakbu keompawilreoneun jaemiwitneun goamokwida. wyulsimhi gowbuhaewyagetda."

J = {'g', 'n', 'd', 'r', 'm', 'b', 's', 'w', 'j', 'z', 'k', 't', 'p', 'h', 'q', 'f'}
M = {'a', 'e', 'i', 'o', 'u', 'y'}
O = {' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '[', ']', '.', ','}

idx = 0
data += '$'
token = []
buf = 'O'

def state00():
    global buf
    if data[idx] in J:
        token.append(' ')
        buf = 'J'
    elif data[idx] in O:
        token.append(data[idx])
        buf = 'O'

def state01():
    global buf
    if data[idx] in M:
        buf += 'M'

def state02():
    global buf
    if data[idx] in J:
        buf += 'J'
    elif data[idx] in M:
        buf += 'M'
    elif data[idx] in O:
        token.append(data[idx-len(buf):idx])
        buf = 'O'

def state03():
    global buf
    if data[idx] in J:
        buf += 'J'
    elif data[idx] in M:
        token.append(data[idx-len(buf):idx-1])
        buf = 'JM'
    elif data[idx] in O:
        token.append(data[idx-len(buf):idx])
        buf = 'O'

def state04():
    global buf
    if data[idx] in J:
        buf += 'J'
    elif data[idx] in O:
        token.append(data[idx-len(buf):idx])
        buf = 'O'

def state05():
    global buf
    if data[idx] in J:
        token.append(data[idx-len(buf):idx])
        buf = 'J'
    elif data[idx] in M:
        token.append(data[idx-len(buf):idx-1])
        buf = 'JM'
    elif data[idx] in O:
        token.append(data[idx-len(buf):idx])
        buf = 'O'

switch = {
    'O': state00,
    'J': state01,
    'JM': state02,
    'JMJ': state03,
    'JMM': state04,
    'JMMJ': state05,
    'JMJJ': state05,
}

while True:
    if data[idx] == '$':
        token.append(data[idx-len(buf):idx])
        break

    switch[buf]()
    idx += 1

result = '|'.join(token[1:]) + '|'
print(result)

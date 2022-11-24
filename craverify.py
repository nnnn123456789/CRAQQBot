from Crypto.Hash import CMAC
from Crypto.Cipher import AES
import base64
import time


cmac_read = False
cmac_secret = b''
def get_serect():
    global cmac_read;
    global cmac_secret;
    if not cmac_read:
        cmac_read = True
        with open("cmac_secret.txt", "r") as f:
            cmac_secret = f.read().strip('\n').encode()
    return cmac_secret


def verify(Token, qqid):
    try:
        raw_token = base64.b64decode(Token).decode()
        timestamp_s, mac = raw_token.split("|")
    except:
        return False
    if int(timestamp_s) < int(time.time()) - 3600:
        return False

    msg = str(qqid) + "|" + str(int(timestamp_s))
    cmac_secret = get_serect();
    cobj = CMAC.new(cmac_secret, ciphermod=AES)
    cobj.update(msg.encode())
    return cobj.hexdigest()[0:9] == mac


def generate_token(qqid, timestamp = time.time()):
    ## for debug only
    hmac_str = str(qqid) + "|" + str(int(timestamp))
    cobj = CMAC.new(get_serect(), ciphermod=AES)
    print(hmac_str)
    cobj.update(hmac_str.encode())
    hmac=cobj.hexdigest()
    print(hmac)
    token = str(int(timestamp)) + "|" + hmac[0:9]
    base64_token = base64.b64encode(token.encode('ascii'))
    print(base64_token)
    return base64_token


def Test():
    qqid = 12345
    timestamp = '10000'
    Token = generate_token(qqid, timestamp)
    return verify(Token, qqid)

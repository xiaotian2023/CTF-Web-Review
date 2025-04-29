from app import parse_cookie,users,generate_cookie
import base64

# p1 = aes_decrypt(c1) ^ iv
# p1' = aes_decrypt(c1) ^ iv'
# iv' = iv ^ p1 ^ p1'

def cbc_bitflip(ciphertext:str,index:int) -> str:
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    new_index = bytearray(iv)
    new_index[index]=iv[index]^ord("1")^ord('n')
    return base64.b64encode(new_index+ciphertext).decode()



if __name__ == '__main__':
    cookie = open('../.idea/httpRequests/http-client.cookies',"r").readlines()[2].split('\t')[-2]
    index='{"name": "admin", "password_raw": "admin", "register_time": -1}'.find('n"')
    admin_cookie = cbc_bitflip(cookie,index)
    print(parse_cookie(admin_cookie))


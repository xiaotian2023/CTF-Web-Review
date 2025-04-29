from app import parse_cookie
import base64
if __name__ == '__main__':
    cookie_b64 = open('../.idea/httpRequests/http-client.cookies', "r").readlines()[2].split('\t')[-2]
    cookie = base64.b64decode(cookie_b64, validate=True).decode()
    new_cookie = cookie.replace('1', 'n',1)
    print(base64.b64encode(new_cookie.encode()).decode())
    print(parse_cookie(base64.b64encode(new_cookie.encode()).decode()))

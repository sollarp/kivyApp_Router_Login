from bs4 import BeautifulSoup
from temp3 import start_page
import requests
import hashlib


def get_password(admin_pass):
    return admin_pass


def admin_login():
    with requests.Session() as s:
        # admin_pass = '9H4NPE3A'
        admin_pass = get_password()
        url1 = "http://192.168.1.254/?active_page=9101"
        r = s.get(url1)
        soup = BeautifulSoup(r.text, "html.parser")
        # print(soup.prettify())
        request_id = soup.find('input', {'type': 'HIDDEN'}, {'name': 'request_id'}).get('value')
        auth_key = soup.find('input', {'name': 'auth_key'}).get('value')
        post_token = soup.find('input', {'name': 'post_token'}).get('value')
        password_id = soup.find('input', {'type': 'PASSWORD'}).get('name')

        md5_pass = admin_pass + auth_key
        pass_md5 = bytes(md5_pass, 'utf-8')
        m = hashlib.md5()
        m.update(pass_md5)
        get_md5_pass = m.hexdigest()

        data = {
            'request_id': request_id,
            'active_page': '9121',
            'active_page_str': 'bt_login',
            'mimic_button_field': 'submit_button_login_submit: .., 1',
            'button_value': '',
            'post_token': post_token,
            password_id: '',
            'md5_pass': get_md5_pass,
            'auth_key': auth_key,
        }

        s.post(url1, data=data)
        page_connection = s.get('http://192.168.1.254/index.cgi?active_page=9122')
        # doc = BeautifulSoup(page_connection.text, 'html.parser')
        # print(doc.prettify())
        return page_connection


def bt_connection_page():
    page_resource = admin_login()
    soup = BeautifulSoup(page_resource.text, 'html.parser')

    scr = soup.find_all("td", {"class": "bt_border"})

    src1 = (scr[1])  # connection status
    src2 = (scr[5])  # down stream
    src3 = (scr[7])  # upstream
    src4 = (scr[3])  # run up time
    one_v1 = (src1.text)
    one_v2 = (src2.text)
    one_v3 = (src3.text)
    one_v4 = (src4.text)

    return one_v1, one_v2, one_v3, one_v4

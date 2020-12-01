from bs4 import BeautifulSoup
import requests
import hashlib


class Hub_5():

    def get_password(self, admin_pass):
        self.admin_pass = admin_pass
        return self.admin_pass

    def admin_login(self):
        with requests.Session() as s:
            # admin_pass = '9H4NPE3A'
            admin_pass_get = self.admin_pass
            url1 = "http://192.168.1.254/?active_page=9101"
            r = s.get(url1)
            soup = BeautifulSoup(r.text, "html.parser")
            # print(soup.prettify())
            request_id = soup.find('input', {'type': 'HIDDEN'}, {'name': 'request_id'}).get('value')
            auth_key = soup.find('input', {'name': 'auth_key'}).get('value')
            post_token = soup.find('input', {'name': 'post_token'}).get('value')
            password_id = soup.find('input', {'type': 'PASSWORD'}).get('name')

            md5_pass = admin_pass_get + auth_key
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


    def bt_connection_page(self):
        page_resource = self.admin_login()
        soup = BeautifulSoup(page_resource.text, 'html.parser')
        scr = soup.find_all("td", {"class": "bt_border"})
        ## find router uptime value in javascript
        time_run = soup.findAll('script')
        js_time = time_run[1]
        delimiters = ['\n']
        for delimiter in delimiters:
            for word in js_time:
                js_time = word.split(delimiter)
        wait = "wait"
        values = [value for value in js_time if wait in value]
        passed = (values[0])
        time_in_js = passed.strip('wait =')
        wait = time_in_js.strip(';') # router uptime in seconds

        # 249984
        t_days = int(wait) / (24 * 60 * 60)
        total_hours = int(wait) / (60 * 60)
        total_minute = int(wait) / 60
        days = int(float(t_days))

        hours_in_days = int(float(t_days)) * 24
        hours = int(float(total_hours - hours_in_days))

        minutes_in_hours = int(float(total_hours)) * 60
        minutes = int(float(total_minute - minutes_in_hours))

        one_v4 = f" {days} Days {hours}:{minutes}"
        ## find other elements on connection page
        src1 = (scr[1])  # connection status
        src2 = (scr[5])  # down stream
        src3 = (scr[7])  # upstream
        one_v1 = (src1.text)
        one_v2 = (src2.text)
        one_v3 = (src3.text)

        return one_v1, one_v2, one_v3, one_v4

from bs4 import BeautifulSoup
import requests
import hashlib


class Hub_5():
    error_returned = None

    def get_password(self, admin_pass):
        self.admin_pass = admin_pass
        return self.admin_pass
    #get_password = lambda admin_pass: admin_pass

    def admin_login(self):

        with requests.Session() as s:
            # admin_pass = '9H4NPE3A'
            admin_pass_get = self.admin_pass
            try:
                url1 = "http://192.168.1.254/?active_page=9101"
                r = s.get(url1)
            except:
                print("check your wifi connection 1")
                return False
            else:
                soup = BeautifulSoup(r.text, "html.parser")
                # print(soup.prettify())
                # admin_pass = '7A64M949'
                admin_pass = admin_pass_get
                try:
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
                    doc = BeautifulSoup(page_connection.text, 'html.parser')
                    current_title = doc.find('title').text
                    #print(current_title)  ## incorrect password or no access to router
                    if 'BT Home Hub Manager - Login' in current_title:
                        print("incorrect passwod")
                        return False
                    else:
                        pass
                    # print(page_connection)
                    # return page_connection
                except:
                    print("this router is not supported")
                    return False
                else:
                    return page_connection

    def bt_connection_page(self):

        page_resource = self.admin_login()
        try:
            soup = BeautifulSoup(page_resource.text, 'html.parser')
            current_title = soup.find('title').text  ##
            #print(current_title)  ##
            scr = soup.find_all("td", {"class": "bt_border"})
            ## find router uptime value in javascript
            time_run = soup.findAll('script')
            js_time = time_run[1]
            delimiters = ['\n']
            for delimiter in delimiters:
                for word in js_time:
                    js_time = word.split(delimiter)
        except AttributeError:
            print("router not supported 1")
            return None
        else:
            wait = "wait"
            values = [value for value in js_time if wait in value]
            #print(f"talalt {scr[1]}")
            try:
                passed = (values[0])

                time_in_js = passed.strip('wait =')
                wait = time_in_js.strip(';')  # router uptime in second
                # scrip for display time in format
                t_days = int(wait) / (24 * 60 * 60)
                total_hours = int(wait) / (60 * 60)
                total_minute = int(wait) / 60
                days = int(float(t_days))
                hours_in_days = int(float(t_days)) * 24
                hours = int(float(total_hours - hours_in_days))
                minutes_in_hours = int(float(total_hours)) * 60
                minutes = int(float(total_minute - minutes_in_hours))
                one_v4 = f"{days} Days {hours}:{minutes}"
                # find other elements on connection page
                src1 = (scr[1])  # connection status
                src2 = (scr[5])  # down stream
                src3 = (scr[7])  # upstream
                one_v1 = (src1.text)
                one_v2 = (src2.text)
                one_v3 = (src3.text)
            except IndexError:
                print("incorrect password 1 or disconnected")
                return scr[1].text, '-', '-', '-'
            else:
                print("incorrect password 2")
                return one_v1, one_v2, one_v3, one_v4

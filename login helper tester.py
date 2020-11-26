from bs4 import BeautifulSoup

def bt_connection_page():
    #x = requests.get('https:192.168.1.254')
    #print(x.status_code)
    #use## x.content
    soup = BeautifulSoup(open("HTML_container/BT Hub 5 login screen.html"), features="lxml")
    #print(soup.prettify())
    #soup = BeautifulSoup(x, 'html.parser')
    scr = soup.find(id='password')
    scr.insert(new_child='pass')
    print(scr)
    #src1 = (scr[1]) # connection status
    #src2 = (scr[5])  # down stream
    #src3 = (scr[7]) # upstream
    #src4 = (scr[3]) # run up time
    #one_v1 = (src1.text)
    #one_v2 = (src2.text)
    #one_v3 = (src3.text)
    #one_v4 = (src4.text)
#
    #return one_v1, one_v2, one_v3, one_v4

bt_connection_page()
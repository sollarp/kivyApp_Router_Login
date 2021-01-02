# KivyApp_Router_Login

Apllication allowes to scrape VDSL router (BT HUB5 and HUB4 'UK version') and login than parse through router HTML and get download, upload speed with  uptime.

This project was build on UBUNTU 20.04 and works only Linux enviroment.

ISSUES:
Unable to create APK with Builtdozer for a following reassons:
 - Normal Python request library not supported use Kivy 'urlrequest' instead.. see in Kivy Doc.
 - hashlib and Beautifulsoup4 not supported by Builtdozer was not able to build APK.
 
 

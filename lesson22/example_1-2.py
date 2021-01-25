import paramiko
import urllib3
import mysql.connector
import sys
import time

host = '127.0.0.1'
user = 'test'
secret = '#123'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret)

#рестарт контейнера opencart
def restart_opencart(param_opencart):
    stdin, stdout, stderr = client.exec_command(f"/docker container restart /{param_opencart}")

#рестарт контейнера maria_db
def restart_opencart(param_db):
    stdin1, stdout1, stderr1 = client.exec_command(f"/docker container restart /{param_db}")

time.sleep(5)
client.close()


def test_restart_opencart():
    http = urllib3.PoolManager()
    url = '127.0.0.1'
    resp = http.request('GET', url)
    assert resp.status == 200

def test_restart_db():
    try:
        status = True
        connection = mysql.connector.connect(
            user="bn_opencart",
            password="",
            host="0.0.0.0",
            port=3307
        )
        connection.close()
        assert status is True
    except mysql.connector.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

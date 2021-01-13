import paramiko

host = '0.0.0.0'
user = 'tanya'
secret = '1234'
port = 23

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
sftp = client.open_sftp()
files = sftp.listdir()
print(files)
client.close()

import socket

print("| /====\\  /====\\  |   | |==== |====\\ |    /|==== |===\\")
print("| |     |  |      |   | |     |      |   / |     |     |")
print("| |====/   |      ===== |==== |      |==<  |==== |====/")
print("| |        |      |   | |     |      |   \\ |     |   \\ ")
print("| |       \\====/  |   | |==== |====/ |    \\|==== |    |")
print("========================CUKIDers========================")
hostname = input('Silahkan masukan Nama Domain: ')
ipaddress = socket.gethostbyname(hostname)

print(f'Nama Domain: {hostname}')
print(f'Alamat IP: {ipaddress}')
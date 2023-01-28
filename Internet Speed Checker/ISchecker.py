import speedtest
print("# #### #####")
print("# #    # ii ii ii== II==II II // II== II=\\\\")
print("# #### # iiiii ii== II     II<<  II== II=<<")
print("#    # # ii ii ii== II==II II"" \\""\\ II== II \\\\")
print("# #### #####")
print("INTERNET SPEED CHECKER by kulionline11 \n")
print("1) Cek Kecepatan Download")
print("2) Cek Kecepatan Upload")
print("3) Cek Kecepatan Download & Upload \n")

a = int(input("Silahkan pilih menu diatas: "))
print("Mohon ditunggu ya...\n")

test = speedtest.Speedtest()
download = test.download()/1024/1024 #dibagi biar jadi Mbps
upload = test.upload()/1024/1024
pinggg = test.results.ping
d = round(download,2) #dibulatkan 2 angka dibelakang
u = round(upload,2)
p = round(pinggg, 2)
if a == 1:
    print(f"Kecepatan Download: {d}/MBps")
    print(f"Ping: {p}/MBps\n")
elif a==2:
    print(f"Kecepatan Upload: {u}/MBps")
    print(f"Ping: {p}/MBps\n")
elif a==3:
    print(f"Kecepatan Download: {d}/MBps")
    print(f"Kecepatan Upload: {u}/MBps")
    print(f"Ping: {p}/MBps\n")
else:
    print("\nInputan yang anda masukan salah parah brooo!!!!\n")
            
#SALAM CUKID MARCUKID

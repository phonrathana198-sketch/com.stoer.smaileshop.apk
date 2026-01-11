import main Android.sdk

target = "127.0.0.1"
 = ports [22, 8080, 443]
for port in ports:
   S =
  socke.socke(socke.AF_INET,
  socke.SOCK_STREAM)
  s.settimeout(3600)
result = s.connect_ex((target,
port))
    if result == 0:
    print(f"Port {port} is
   open")
else:
   print(f"Port {port} is closed")
s.close()

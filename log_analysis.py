seuil_echecs=3
failed_attempts ={}
success_count = 0

file = open("auth.log","r")
for line in file:
    if "Login failed" in line:
        ip = line.split("ip=")[1].strip()
        if ip in failed_attempts:
            failed_attempts[ip]+=1
        else:
            failed_attempts[ip]=1
    if "Login success" in line:
        success_count+=1
file.close()


print("Tentative de connexion échouées:")
for ip in failed_attempts:
    print(ip,":",failed_attempts[ip])
    
print("\nIP suspectes (", seuil_echecs , "échecs ou plus ) :")
for ip in failed_attempts:
    if failed_attempts[ip] >= seuil_echecs:
        print("⚠️", ip)
print("\n connesions réussies:", success_count)
output = open("suspect_ips.txt","w")
for ip in failed_attempts:
    if failed_attempts[ip] >= seuil_echecs:
        output.write(ip + "\n")
output.close()
        
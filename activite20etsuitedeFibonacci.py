
adresses_ip = [
    "192.168.0.1",
    "10.0.0.1",
    "172.16.0.1",
    "200.100.50.1",
    "169.254.0.1"
]
print(f"la 1ere adresse dans la liste est {adresses_ip[0]}")
print(f"la derniere adresse dans la liste est {adresses_ip[len(adresses_ip) - 1]}")
print(f"la 3eme adresse dans la liste est {adresses_ip[2]}")
adresses_ip.append("172.31.0.1")
print(adresses_ip)
adresses_ip.remove("200.100.50.1")
print(f"il reste {len(adresses_ip)} adresses dans la liste ")
if "192.168.0.1" in adresses_ip :
    print(" l'adresse 192.168.0.1 existe dans la liste")
else : print(" l'adresse 192.168.0.1 n'existe pas dans la liste")

class Classe :
    def __init__(self,name,ip_address):
        self.name = name
        self.ip_address = ip_address
    def class_name(self):
        print(f" la classe est {self.name}")
classe_A = Classe("A","10.0.0.1")
classe_B = Classe("B","172.16.0.1")
classe_C = Classe("C","192.168.0.1")
IP_publique= Classe("PUBLIC","200.100.50.1")
IP_local = Classe("LOCAL","169.254.0.1")
classe_A.class_name()
ordered_list = sorted(adresses_ip)
print(ordered_list)
listc = []
nbr = 0
for ip in adresses_ip :
    if ip == classe_C.ip_address :
        listc.append(ip)
    if ip == IP_publique.ip_address :
        nbr += 1
if listc == adresses_ip :
    print("toutes les elements de la liste des ip_adresses appartient a la classe C")
else :
    print(f"voila les elements de la liste des ip_adresses qui appartient a la classe C: {listc} ")

print(f"il y a {nbr}  de ip publiques dans la liste")
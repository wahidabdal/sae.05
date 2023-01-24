def readfile(fichier):
    try:
        with open(fichier, encoding="utf8") as file:

            return file.read().splitlines()
    except:
        print("desole le fichier en question n'existe pas\n.")
       
lire=readfile('C:/Users/wahid/OneDrive/Bureau/tor/Exam.txt')
fichiercsv=[]
fic=open("C:/Users/wahid/OneDrive/Bureau/tor/trames.csv", "w",encoding="utf8")            
colone = "DATE ; IP ; SOURCE ; DESTINATION ; PORT ; FLAG ; SEQ ; ACK ; WIN ; OPTIONS ; VAL ; ECR ; LENGTH"
fic.write(colone + "\n")
for ligne in lire:
    if ligne.startswith("07:48"):      
        donnee=[" "]*12
        separer=ligne.replace("[","").replace("]","").replace(",","").split(" ")
        donnee[0]=separer[0]
        for index,word in enumerate(separer):  
            if word==">":
                donnee[2]=separer[index-1]
                ip_port = separer[index+1]
                parts = ip_port.split(".")
                port = parts[-1]
                ip = ".".join(parts[:-1])
                donnee[3] = ip + ";" + port        
            if word=="Flags":
                donnee[4]=separer[index+1]
            if word=="seq":
                donnee[5]=separer[index+1]
            if word=="ack":
                donnee[6]=separer[index+1]
            if word=="win":
                donnee[7]=separer[index+1]
            if word=="options":
                donnee[8]=separer[index+1]
            if word=="val":
                donnee[9]=separer[index+1]
            if word=="ecr":
                donnee[10]=separer[index+1]
            if word=="length":
                donnee[11]=separer[index+1]
            csvline=";".join(donnee)
            #fichiercsv.append(csvline)+
        colone=csvline
        fic.write(colone +"\n")
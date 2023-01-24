def readfile(fichier):
    try:
        with open(fichier, encoding="utf8") as file:

            return file.read().splitlines()
    except:
        print("desole le fichier en question n'existe pas\n.")
cool=readfile('C:/Users/wahid/OneDrive/Bureau/tor/Exam.txt')
fichiercsv=[]
for ligne in cool:

    if ligne.startswith("07:48"):       
        donnee=[" "]*13
        separer=ligne.split(" ")
        donnee[0]=separer[0]
        for index,word in enumerate(separer):   
            if word=="IP":
                donnee[1]=word
            if word==">":
                donnee[2]=separer[index-1]
                donnee[3]=separer[index+1]
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
            if word=="HTTP":
                donnee[12]=word
            csvline=";".join(donnee)
            fichiercsv.append(csvline)
            print(csvline)      
def writefile(fichier,contenu):
     with open(fichier,"w") as fic:
        for ligne in contenu:
            fic.write(ligne+"\n")
writefile("tv.csv",fichiercsv)
writefile("fichiers_markdown.md",fichiercsv)

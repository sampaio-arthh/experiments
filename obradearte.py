fla=0
vas=0
flu=0
bota=0
ban=0
mad=0
#Gols feitos ↓
flagf=0
vasgf=0
flugf=0
botagf=0
bangf=0
madgf=0
#Gols sofridos ↓
flags=0
vasgs=0
flugs=0
botags=0
bangs=0
madgs=0
#Jogos ↓
vasgf, flagf = input("Vas x Fla: ").split()
vasgf = int(vasgf)
flagf = int(flagf)
vasgs += flagf
flags += vasgf
if vasgf > flagf:
    vas +=1
elif vasgf == flagf:
    vas += 0
    fla +=0
else:
    fla += 1

vasgf, flugf = input("Vas x Flu: ").split()
vasgf = int(vasgf)
flugf = int(flugf)
vasgs += flugf
flugs += vasgf
if vasgf > flugf:
    vas +=1
elif vasgf == flugf:
    vas += 0
    flu +=0
else:
    flu += 1

vasgf, botagf = input("Vas x Bot: ").split()
vasgf = int(vasgf)
botagf = int(botagf)
vasgs += botagf
botags += vasgf
if vasgf > botagf:
    vas +=1
elif vasgf == botagf:
    vas += 0
    bota += 0
else:
    bota += 1

vasgf, bangf = input("Vas x Ban: ").split()
vasgf = int(vasgf)
bangf = int(bangf)
vasgs += bangf
bangs += vasgf
if vasgf > bangf:
    vas +=1
elif vasgf == bangf:
    vas += 0
    ban +=0
else:
    ban += 1
    
vasgf, madgf = input("Vas x Mad: ").split()
vasgf = int(vasgf)
madgf = int(madgf)
vasgs += madgf
madgs += vasgf
if vasgf > madgf:
    vas +=1
elif vasgf == madgf:
    vas += 0
    mad +=0
else:
    mad += 1
    
flagf, flugf = input("Fla x Flu: ").split()
flagf = int(flagf)
flugf = int(flugf)
flugs += flagf
flags += flugf
if flugf > flagf:
    flu +=1
elif flugf == flagf:
    flu += 0
    fla +=0
else:
    fla += 1

flagf, botagf = input("Fla x Bot: ").split()
flagf = int(flagf)
botagf = int(botagf)
botags += flagf
flags += botagf
if botagf > flagf:
    bota +=1
elif botagf == flagf:
    bota += 0
    fla +=0
else:
    fla += 1
    
flagf, bangf = input("Fla x Ban: ").split()
flagf = int(flagf)
bangf = int(bangf)
bangs += flagf
flags += bangf
if bangf > flagf:
    ban +=1
elif bangf == flagf:
    ban += 0
    fla +=0
else:
    fla += 1
    
flagf, madgf = input("Fla x Mad: ").split()
flagf = int(flagf)
madgf = int(madgf)
madgs += flagf
flags += madgf
if madgf > flagf:
    mad +=1
elif madgf == flagf:
    mad += 0
    fla +=0
else:
    fla += 1
    
flugf, botagf = input("Flu x Bot: ").split()
flugf = int(flugf)
botagf = int(botagf)
flugs += botagf
botags += flugf
if flugf > botagf:
    flu +=1
elif flugf == botagf:
    flu += 0
    bota +=0
else:
    bota += 1
    
flugf, bangf = input("Flu x Ban: ").split()
flugf = int(flugf)
bangf = int(bangf)
flugs += bangf
bangs += flugf
if flugf > bangf:
    flu +=1
elif flugf == bangf:
    flu += 0
    ban +=0
else:
    ban += 1
    
flugf, madgf = input("Flu x Mad: ").split()
flugf = int(flugf)
madgf = int(madgf)
flugs += madgf
madgs += flugf
if flugf > madgf:
    flu +=1
elif flugf == madgf:
    flu += 0
    mad +=0
else:
    mad += 1
    
botagf, bangf = input("Bot x Ban: ").split()
botagf = int(botagf)
bangf = int(bangf)
botags += bangf
bangs += botagf
if bangf > botagf:
    ban +=1
elif bangf == botagf:
    ban += 0
    bota +=0
else:
    bota += 1
    
botagf, madgf = input("Bot x Mad: ").split()
botagf = int(botagf)
madgf = int(madgf)
botags += madgf
madgs += botagf
if madgf > botagf:
    mad +=1
elif madgf == botagf:
    mad += 0
    bota +=0
else:
    bota += 1
    
bangf, madgf = input("Ban x Mad: ").split()
bangf = int(bangf)
madgf = int(madgf)
madgs += bangf
bangs += madgf
if bangf > madgf:
    ban +=1
elif bangf == madgf:
    mad += 0
    ban +=0
else:
    mad += 1
    
maior=0
maior2=0

if vas > fla and vas > flu and vas > bota and vas > ban and vas > mad :
    maior='Vasco'
    if fla > flu and fla > bota and fla > ban and fla > mad :
        maior2="Flamengo"
    if flu > fla and flu > bota and flu > ban and flu > mad :
        maior2="Fluminense"
    if bota > flu and bota > fla and bota > ban and bota > mad :
        maior2="Botafogo"
    if ban > flu and ban > fla and ban > bota and ban > mad :
        maior2="Bangu"
    if mad > flu and mad > fla and mad > ban and mad > bota :
        maior2="Madureira"
    
if fla > vas and fla > flu and fla > bota and fla > ban and fla > mad :
    maior="Flamengo"
    if vas > flu and vas > bota and vas > ban and vas > mad :
        maior2="Vasco"
    if flu > vas and flu > bota and flu > ban and flu > mad :
        maior2="Fluminense"
    if bota > flu and bota > vas and bota > ban and bota > mad :
        maior2="Botafogo"
    if ban > flu and ban > vas and ban > bota and ban > mad :
        maior2="Bangu"
    if mad > flu and mad > vas and mad > ban and mad > bota :
        maior2="Madureira"
    
if flu > vas and flu > fla and flu > bota and flu > ban and flu > mad :
     maior="Fluminense"
     if vas > fla and vas > bota and vas > ban and vas > mad :
         maior2="Vasco"
     if fla > vas and fla > bota and fla > ban and fla > mad :
         maior2="Flamengo"
     if bota > fla and bota > vas and bota > ban and bota > mad :
         maior2="Botafogo"
     if ban > fla and ban > vas and ban > bota and ban > mad :
         maior2="Bangu"
     if mad > fla and mad > vas and mad > ban and mad > bota :
         maior2="Madureira"
if bota > vas and bota > flu and bota > fla and bota > ban and bota > mad :
    maior="Botafogo"
    if vas > fla and vas > flu and vas > ban and vas > mad :
        maior2="Vasco"
    if flu > vas and fla > flu and fla > ban and fla > mad :
        maior2="Flamengo"
    if flu > fla and flu > vas and flu > ban and flu > mad :
        maior2="Fluminense"
    if ban > fla and ban > vas and ban > flu and ban > mad :
        maior2="Bangu"
    if mad > fla and mad > vas and mad > ban and mad > flu :
        maior2="Madureira"
if ban > vas and ban > flu and ban >  fla and ban > bota and ban > mad :
    maior="Bangu"
    if vas > fla and vas > flu and vas > bota and vas > mad :
        maior2="Vasco"
    if flu > vas and fla > flu and fla > bota and fla > mad :
        maior2="Flamengo"
    if flu > fla and flu > vas and flu > bota and flu > mad :
        maior2="Fluminense"
    if bota > fla and bota > vas and bota > flu and bota > mad :
        maior2="Botafogo"
    if mad > fla and mad > vas and mad > bota and mad > flu :
        maior2="Madureira"
if mad > vas and mad > flu and mad > fla and mad > ban and mad > bota :
    maior="Madureira"
    if vas > fla and vas > flu and vas > bota and vas > ban :
        maior2="Vasco"
    if flu > vas and fla > flu and fla > bota and fla > ban :
        maior2="Flamengo"
    if flu > fla and flu > vas and flu > bota and flu > ban :
        maior2="Fluminense"
    if bota > fla and bota > vas and bota > flu and bota > ban :
        maior2="Botafogo"
    if ban > fla and ban > vas and ban > bota and ban > flu :
        maior2="Bangu"



if vasgs > flags and vasgs > flugs and vasgs > botags and vasgs > bangs and vasgs > madgs :
    print("Vasco sofreu mais gols")
if flags > vasgs and flags > flugs and flags > botags and flags > bangs and flags > madgs :
    print("Flamengo sofreu mais gols")
if flugs > vasgs and flugs > flags and flugs > botags and flugs > bangs and flugs > madgs :
    print("Fluminense sofreu mais gols")
if botags > vasgs and botags > flugs and botags > flags and botags > bangs and botags > madgs :
    print("Botafogo sofreu mais gols")
if bangs > vasgs and bangs > flugs and bangs > botags and bangs > flags and bangs > madgs :
    print("Bangu sofreu mais gols")
if madgs > vasgs and madgs > flugs and madgs > botags and madgs > bangs and madgs > flags :
    print("Madureira sofreu mais gols")

if vasgf > flagf and vasgf > flugf and vasgf > botagf and vasgf > bangf and vasgf > madgf:
    print("Vasco fez mais gols")
if flagf > vasgf and flagf > flugf and flagf > botagf and flagf > bangf and flagf > madgf :
    print("Flamengo fez mais gols")
if flugf > vasgf and flugf > flagf and flugf > botagf and flugf > bangf and flugf > madgf :
    print("Fluminense fez mais gols")
if botagf > vasgf and botagf > flugf and botagf > flagf and botagf > bangf and botagf > madgf :
    print("Botafogo fez mais gols")
if bangf > vasgf and bangf > flugf and bangf > botagf and bangf > flagf and bangf > madgf :
    print("Bangu fez mais gols")
if madgf > vasgf and madgf > flugf and madgf > botagf and madgf > bangf and madgf > flagf :
    print("Madureira fez mais gols")

print(f"Vasco fez {vasgf} gols")
print(f"Flamengo fez {flagf} gols")
print(f"Fluminense fez {flugf} gols")
print(f"Botafogo fez {botagf} gols")
print(f"Madureira fez {madgf} gols")
print(f"Bangu fez {bangf} gols")

print(f"Vasco sofreu {vasgs} gols")
print(f"Flamengo sofreu {flags} gols")
print(f"Fluminense sofreu {flugs} gols")
print(f"Botafogo sofreu {botags} gols")
print(f"Madureira sofreu {madgs} gols")
print(f"Bangu sofreu {bangs} gols")

print(f'O campeão é {maior}')
print(f'O vice-campeão é {maior2}')    
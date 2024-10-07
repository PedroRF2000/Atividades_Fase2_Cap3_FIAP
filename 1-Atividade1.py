# dias estao em letras minusculas , se não der certo mudar para maiu
dias=["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira"].upper()
contSeg=0
contTer=0
contQua=0
contQui=0
contSex=0
colaboradores=int(input("Informe o número de colaboradores: "))
for colaborador in colaboradores:
    diaPreferencia=input("Informe o dia de sua preferência (segunda-feira,terça-feira,quarta-feira,quinta-feira ou sexta-feira): ").upper().strip()
    while diaPreferencia not in dias:
        diaPreferencia=input("Valor inválido, informe o dia de sua preferência (segunda-feira,terça-feira,quarta-feira,quinta-feira ou sexta-feira): ").upper().strip()
    if diaPreferencia=="SEGUNDA-FEIRA" or diaPreferencia=="SEGUNDA":
        contSeg+=1
    elif diaPreferencia=="TERÇA-FEIRA" or diaPreferencia=="TERÇA":
        contTer+=1
    elif diaPreferencia=="QUARTA-FEIRA" or diaPreferencia=="QUARTA":
        contQua+=1
    elif diaPreferencia=="QUINTA-FEIRA" or diaPreferencia=="QUINTA":
        contQui+=1
    else:
        contSex+=1
    
    if maior==:
    
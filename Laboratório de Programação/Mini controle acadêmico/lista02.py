from testeda02 import*
opç = 0       
listcod=[]
cads = 'registro.txt'
if not existe(cads):
    criaarq(cads)

while(opç != 9):
    while True:
     menu()
     try:
         opç = int(input('Digite uma opção:'))
         print() 
         break
     except:
         print('Erro>>> A entrada deve ser um valor numérico!!! \n')
         continue
   
    if opç == 1:
        listcod.append(cadastra_disciplina(listcod))
    if opç == 2:
        pesquisa_disci(listcod)
    if opç == 3:
        lista_disci(listcod)
    if opç == 4:
        cadast_prof(listcod)
        if len(listcod) != 0:
            o = str(input('Deseja listar os professores cadastrados desta disciplina?s/n')).lower()
            if o!= 'n' and o!= 's':
                while True:
                    o = str(input('Deseja listar os professores cadastrados desta disciplina?s/n')).lower()
                    if o == 's':
                        listaprof(listcod)
                        break
                    else:
                        if o == 'n':
                           break
            elif o == 's':
                listaprof(listcod)
            else:
                continue        
    if opç == 5:
        matric_alun(listcod)     
    if opç == 6:
        joga_notaindiscip(listcod)
    if opç == 7:
        if len(listcod) != 0:
            lista_alun(listcod)
        else:
            print('Sem disiciplinas existentes! CADASTRE UMA DISICIPLINA PRIMEIRO!!!')         
    if opç == 8:
        lista_notasalunindisciplin(listcod)
    if opç == 9:
        salvaaqr(cads,listcod)
        print('Obrigado por usar este serviço :)!')
          
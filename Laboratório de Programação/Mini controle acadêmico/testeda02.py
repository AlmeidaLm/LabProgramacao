def menu():
    print('===Mini Controle Acadêmico===\n')
    print('1._Cadastrar disciplina_')
    print('2._Pesquisar disciplina_')
    print('3._Listar disciplinas cadastradas_')
    print('4._Cadastrar professor em disciplina_')
    print('5._Matricular aluno em disciplina_')
    print('6._Lançar notas do aluno em uma disciplina_')
    print('7._Listar alunos de uma disciplina_')
    print('8._listar notas dos alunos de uma disciplina_')
    print('9.Sair>')
    
def cadastra_disciplina(listcod):
    aluns =[]
    profis=[]
    semana=[]
    while True:    
        try:
            a = 2
            codi = int(input('Digite um código para a disciplina:'))
            for i in listcod:
                if codi == i[0]:
                    print('O código já está associado a uma disciplina !!! Tente novamente>>>')
                    a = 1
            if a == 2:
                break
        except :
            print('ERRO!!!< DIGITE UM NÚMERO INTEIRO')
    while True:    
        try:
            b = 2
            materi = str(input('Digite o nome da disciplina [Máx 255caracters] :'))
            if len(materi) <= 255:
                for i in listcod:
                    if materi == i[1]:
                        print('O Disciplina já cadastrada !!! Tente novamente>>>')
                        b = 1
            else:
                b = 1
            if b == 2:
                break
        except :
            print('ERRO!!!< DIGITE UM NOME PARA A DISCIPLINA >')
    while True:
        try:
            b = 2
            semist = int(input('Digite o ano da disciplina 1971 ao ano atual [Formato AAAA] :'))
            period = int(input('Digite o período de ingresso 1(primeiro),(2 segundo):'))
            if 1970 < semist <= 2023 and period == 1 or 1970 < semist <= 2023 and period == 2: 
                semis_entr = str(semist) +'.'+ str(period)
            else:
                print('Ano fora do escopo 1971 -> today ou período de ingresso inválido \n ')
                b = 1
            if b == 2:
                break
        except :
            print('ERRO!!!< O VALOR PARA O ANO/PERÍODO É INVÁLIDO >')         
    while True:
        try:
            carghr = int(input('Digite a Carga horária[ mín 15 hrs, máx 72hrs]:'))
            if carghr < 15 or carghr > 72:
                print('Carga horária fora do escopo estabelecido !!!')
            else:
                carg_hr = str(carghr) + 'h'
                break          
        except:
            print('ERRO!!!< O VALOR PARA O ANO/PERÍODO É INVÁLIDO >')
    semana=[]
    i = 0
    a = 0
    while True:
        try: 
            print('Dias da semana, 1-segunda,2-terça,3-quarta,4-quinta,5-sexta,6-sábado \n')
            dia = int(input('Digite um dia para sua disciplina:')) 
            if 0 < dia < 7:
                if len(semana) == 0:
                    semana.append(dia)
                    i = i + 1
                else:
                    for h in range(len(semana)):
                        if dia == semana[h]:
                            print('Dia já cadastrado') 
                        else:
                            if i <= 2:
                                semana.append(dia)
                                i = i + 1 
                            else:
                                print('Limites de dia para disciplina atingido!!!\n')   
            else:       
                print('Digite um valor dentro do especificado')
            if i >= 3:
                if semana[1] == semana[2]:
                    while True:
                        try :
                            dia = int(input('Digite um dia para sua disciplina:'))
                            semana[2] = dia
                            if 0 < dia < 7:
                                if semana [1] != semana [2] and semana[2] != semana[0]:
                                    break
                                else:
                                    print('Dia já cadastrado')           
                            else:
                                print('Digite um valor dentro do especificado 1 a 6\n')
                        except:
                           print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO >')          
                break 
            else:
                resp = str(input('Adicionar mais um dia para a disciplina?(N-parar, S-adicionar):')).upper()
                if resp != 'S' and resp != 'N':
                    while True:
                        resp = str(input('Adicionar mais um dia para a disciplina?(N-parar,S-adicionar):')).upper()
                        if resp == 'N' or resp == 'S':
                            break
                if resp == 'N':
                    break
        except:
            print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO >')
    while True:
        try:
            hora = int(input('Digite um horário para a disciplina 1 a 7:'))
            if 0 < hora < 8:
                break
            else:
                print('Valor fora do range determinado!!!')
        except:
            print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO >')  
    
    hora_dis = (semana,hora)
    
    return codi,materi,semis_entr,profis,aluns,carg_hr,hora_dis

def pesquisa_disci(listcod):
    if listcod != 0:
        try:
            disc = int(input('Digite o código da disciplina desejada(apenas números):'))
            for i in listcod:
                if disc == i[0]:
                    print(f' nome da disciplina : {i[1]} \n \nSemestre  {i[2]} \n')
                    for b in listcod:
                        g = len(b[3])
                        if g > 1:
                            print(f'código do professor : {b[0]} \n Nome do professor : {b[1]} \n') 
                        elif g == 1:
                            print(f'código do professor : {i[3][0][0]} \n Nome do professor : {i[3][0][1]} \n') 
                        else:
                            print('Disciplina sem professor registrado!!!\n') 
                        print(f'Carga horária da disciplina {i[5]} \n Dias e horários em que é realizada : {i[6]} \n')
                else:
                    print('DISCIPLINA INEXISTENTE!!!')                             
        except:     
            print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO >')
    else:
        print('Não há disciplinas cadastradas!!!!')
    
def lista_disci(listcod):
    print('Lista de disciplinas cadastradas até o momento: \n')
    for i in listcod:
        print(f'Código {i[0]} : Nome da disciplina [{i[1]}] : carga horária :[{i[5]}]\n')
a = 0
def cadast_prof(listcod):
    if len(listcod)!=0:
        try:
            codisp = int(input('Digite o código da disciplina>:'))
            print()
            for i in listcod:
                if codisp == i[0]:
                    if len(i[3]) == 0:
                        while True:
                            try:
                                pronum = int(input('Digite um código para o professor:'))
                            except:
                                print('ERRO!!!< O VALOR ATRIBUÍDO AO CÓDIGO É INVÁLIDO >')
                            disc = str(input('Digite o nome do professor(MÁX255 caracteres):'))
                            if len(disc) < 256:
                                info = (pronum,disc)
                                i[3].append(info)
                                a = 1
                                break
                            else:       
                                print('Nome muito longo por favor abrevie>') 
                    else:       
                        while True:
                            a = 0
                            try:
                                pronum = int(input('Digite um código para o professor:'))
                            except:
                                print('ERRO!!!< O VALOR ATRIBUÍDO AO CÓDIGO É INVÁLIDO >')
                            for h in i[3]:
                                if pronum == h[0]:
                                    a = 1
                                    break
                            if a == 0:
                                break
                            else:
                                print('Já existem professores registrados com este código!!!!')
                        while True:
                            disc = str(input('Digite o nome do professor(MÁX255 caracteres):'))
                            if len(disc) < 256:
                                info = (pronum,disc)
                                i[3].append(info)
                                break
                            else:       
                                print('Nome muito longo por favor abrevie>')                                           
                else:
                    print('O código não está associado a uma disciplina!!!')
        except:
            print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO <><><><>') 
    else:
        print('Cadastre uma disciplina para matricular um professor!!!')
 
def listaprof(listcod):
    print()
    for i in listcod:
        print(f'O professores da Disciplina {i[1]} do Semestre {i[2]}\n')
        for c in i[3]:
            print(f'{c[1]} : código : {c[0]}')
     
def matric_alun(listcod):
    if len(listcod)!=0:
        try:
            codisp = int(input('Digite o código da disciplina>:'))
            print()
            for i in listcod:
                if codisp == i[0]:
                    if len(i[4]) == 0:
                        while True:
                            alunum = str(input('Digite uma matrícula para o aluno(máx 11 carcteres):')) 
                            nom_al = str(input('Digite o nome do aluno (MÁX255 caracteres):'))
                            curs = str(input('Digite o nome do curso (MÁX255 caracteres):'))
                            if len(nom_al) < 256 and len(alunum) <= 11 and len(curs) < 256:
                                info_a = (alunum,nom_al,curs,[])
                                i[4].append(info_a)
                                break
                            else:       
                                print('A string digitada foi muito longa por favor abrevie>') 
                    else:       
                        while True:
                            a = 0
                            b = 0
                            alunum = str(input('Digite uma matrícula para o aluno(máx 11 carcteres):'))
                            for h in i[4]:
                                if alunum == h[0]:
                                    a = 1
                                    break
                            if len(alunum) > 11:
                                print('A string digitada foi muito longa por favor abrevie>')
                                b = 1
                            if a == 0 and b == 0:
                                break
                            else:
                                if a == 1:
                                    print('Já existem alunos registrados com a matrícula digitada!!!!')
                        while True:
                            nom_al = str(input('Digite o nome do aluno(MÁX255 caracteres):'))
                            curs = str(input('Digite o nome do curso (MÁX255 caracteres):'))
                            if len(nom_al) < 256 and len(curs) < 256:
                                info_a = (alunum,nom_al,curs,[])
                                i[4].append(info_a)
                                break
                            else:       
                                print('A string digitada foi muito longa por favor abrevie>')                                           
                else:
                    print('O código não está associado a uma disciplina!!!')
        except:
            print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO <><><><>') 
    else:
        print('Cadastre uma disciplina para matricular um Aluno!!!')

def lista_alun(listcod):
    try:
        elcod = int(input('Digite o código da disciplina:'))
        for i in listcod:
            if elcod == i[0]:
                print(f'Disciplina : {i[1]} do Semestre {i[2]}\n')
                print(f'Os alunos registrados são : \n')
                for c in i[4]:
                    print(f'Código : {c[0]} Nome : {c[1]} Curso : {c[2]}')
                break
            else:
                print('O código não está associado a uma disciplina!!!')   
    except:
        print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO <><><><>')      
k = 0
m = 0
def joga_notaindiscip(listcod):
    if len(listcod)!=0:
        try:
            elcod = int(input('Digite o código da disciplina:'))
            for i in listcod:
                if elcod == i[0]:
                    if len(i[4]) != 0 :
                        while True:
                            an_cod = str(input('Digite o código do aluno(MÁX 11 caracteres)'))
                            if len(an_cod) <= 11:
                                o = 0
                                for c in i[4]:
                                    if an_cod == c[0]:
                                        for h in range(0,3):
                                            o = o+1
                                            print(f'insira a {o}º nota :')
                                            nota = int(input(''))
                                            c[3].append(nota)
                                        k = 1
                            else:
                                print('A string digitada foi muito longa')
                            if k == 1:
                                break
                    else:
                        print('Sem alunos nesta disiciplina! Cadastre os alunos antes de inserir notas!')
                else:
                    print('O código não está associado a uma disciplina!!!')     
        except:
            print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO <><><><>') 
    else:
        print(' ERRO Cadastre uma disciplina antes de inserir as notas de um Aluno!!!')
n = 0
def lista_notasalunindisciplin(listcod):
    
    if len(listcod)!= 0:
        try:
            elcod = int(input('Digite o código da disciplina:'))
            for i in listcod:
                if elcod == i[0]:
                    if len(i[4]) != 0 :
                        print('Os alunos desta disciplina são : \n')
                        for b in i[4]:
                            print(f'Matrícula : {b[0]} Nome : {b[1]} Curso : {b[2]} ')
                            print(f'Notas : {b[3]}')
                            somi = sum(b[3])
                            somi = somi/3.0
                            print(f'Média final:{somi:.1f}')           
                    else:
                        print('Sem alunos nesta disiciplina! Cadastre os alunos antes de inserir notas!')
                else:
                    print('O código não está associado a uma disciplina!!!') 
        except:
            print('ERRO!!!< O VALOR ATRIBUÍDO É INVÁLIDO <><><><>') 
    else:
       print(' ERRO Cadastre uma disciplina antes de visualizar as notas de um Aluno!!!') 

def existe(arqui):
    try:
        o = open(arqui, 'rt')
        o.close()
    except FileNotFoundError:
       return False
    else:
       return True

def criaarq(arqui):
    try:
        o = open(arqui,'wt+')
        o.close()
    except:
        print('Ocorreu um erro ao criar o arquivo para salvar os dados!!!')

def salvaaqr(arqui,listcod):
    try:
        o = open(arqui, 'at')
    except:
        print('Ocorreu um problema ao abrir um arquivo!')
    else:
        try:
            o.write(f'{listcod}\n')
            o.close()
        except:
            print('Ocorreu um erro ao efetuar a gravação em arquivo!')
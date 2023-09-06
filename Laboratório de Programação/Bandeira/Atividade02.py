from PIL import Image
import math
import numpy as np
def filipins(tam):
    BLUE = (0,56,168)
    RED = (206,17,38)
    WHITE = (255, 255, 255)
    ima = 2*tam
    nova_img = Image.new('RGB',(ima,tam),RED)
    nov = (int(ima*(2/5)))
    cat = tam/2
    cat = math.pow(cat,2)
    cat2 = math.pow(nov,2)
    hips = math.sqrt(cat + cat2)
    for x in range(ima):
        for y in range(tam):
            if y >= (tam/2) and y <= tam:
                nova_img.putpixel((x,y),BLUE)
            if x <= nov and y <= (tam/2):
                if x/1.6 <= y:
                    nova_img.putpixel((x,y),WHITE)
    new_img = nova_img.transpose(Image.FLIP_TOP_BOTTOM)                    
    for x in range(ima):
        for y in range(tam):
            if x <= nov and y <= (tam/2):
                if x/1.6 <= y:
                    new_img.putpixel((x,y),WHITE)
    new_img.save('img.png',format ='PNG')                      
    return new_img

def negati(img):
    #saber a escala de cada cor e diminuir 255: 
    img_arry = np.array(img) 
    max = 255
    img_arry = max - img_arry 
    inverte_img = Image.fromarray(img_arry)
    return inverte_img  
while True:
    try:
        i = int(input('Digite 1 para a bandeira das filipinas e 2 para o negativo de uma imagem:'))
        if i == 1:
            di = 320
            t = filipins(di)
            t.show()
            break
        if i == 2:
            try:
                img = Image.open('img.png')
                t = negati(img)
                t.show()
                break
            except:
                print('Execute a primeira função para ter uma imagem!')
    except:
        print('Valor fora do escopo!')
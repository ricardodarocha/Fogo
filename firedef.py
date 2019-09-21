import time, random
    
def updatemodel(altura, largura, model):
    return [ model[i+largura] - random.randint(0,3) if model[i+largura] > 0 else 0 for i in range(largura * (altura-1)) ]

def rendermodel(altura, largura, model, firevalues):
    time.sleep(0.4)
    print(chr(27) + "[2J")
    for i in range(altura):
        row = '' 
        for j in range(largura):
            row += firevalues[ model[ j + i * largura] ]
        print(row) 
        
if __name__ == "__main__":
    altura, largura = 20, 80
    firevalues = [char for char in " ´`.:*sS"] 
    firesource = [ len(firevalues)- 1 for i in range(largura) ]
    model =  [ 0 for i in range(altura * largura -1 ) ] + firesource
    while True:
        model = updatemodel( altura, largura, model + firesource ) 
        rendermodel( altura, largura, model + firesource, firevalues )
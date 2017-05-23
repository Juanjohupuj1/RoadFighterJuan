import tkinter
import time
import random
import math
# Crea la ventana que tendrá el mapa la asocia a la variable v
ventana = tkinter.Tk()
ventana.title("Road Fighter")
ventana.geometry("1890x1000")
v = tkinter.Toplevel()
v.geometry("1890x1000")
imagen1 = tkinter.PhotoImage(file="fondoprincipal.png")
fondo = tkinter.Label(ventana, image=imagen1).place(x=0 ,y=0)



x=tkinter.StringVar()
fondojuego =tkinter.Canvas(v,height=600,width=900,bg="black")

ho= []

#var=tkinter.StringVar()#charge textvariable
#fondotextos= tkinter.Label(ventana,textvariable =var,bg="black",fg="white")
#cargo las imágenes a usar
fondomarder=tkinter.PhotoImage(file="marderecha.png")
fondomarizq=tkinter.PhotoImage(file="marizq.png")
centro1=tkinter.PhotoImage(file="centermar.png")
#u=tkinter.PhotoImage(file="TryFont3m.png")#carga imagen mapa
#entradas nameplayers
#nombre= tkinter.Label(ventana,text="Nombre del jugador 1", font=("Tempus Sans ITC",12)).place(x=20, y=395)
#entrada1 = tkinter.Entry(ventana,font=("Tempus Sans ITC",12)).place(x=180, y = 395)

#photopo=tkinter.PhotoImage(file="Tryfont3m.png")
carrov1 = tkinter.PhotoImage(file="UserCare.png")#carro verde
carrov2 = tkinter. PhotoImage(file="UserCare.png")#carro verde
explosion = tkinter. PhotoImage(file="explosion1.png")#explosion de choque
photo=tkinter.PhotoImage(file="BlueCare.png")#CarroRunnerAzul
vancar=tkinter.PhotoImage(file="RedCare.png")#Carro Minivan rojo
fighter=tkinter.PhotoImage(file="YellowCare.png")

user2=tkinter.PhotoImage(file="usercar2e.png")

minivan2=tkinter.PhotoImage(file="RedCare.png")

run2=tkinter.PhotoImage(file="BlueCare.png")


fi2=tkinter.PhotoImage(file="YellowCare.png")

chargegas=tkinter.PhotoImage(file="Recarga.png")

#cargo las imagenes de los botones
imagen_2boton=tkinter.PhotoImage(file="Level1.png")
imagen_3boton=tkinter.PhotoImage(file="Level2.png")
imagen_4boton=tkinter.PhotoImage(file="Level3.png")
imagen_5boton=tkinter.PhotoImage(file="Level4.png")
imagen_6boton=tkinter.PhotoImage(file="Level5.png")
imagen_1boton = tkinter.PhotoImage(file="BotonSalir.png")

#movimientofondo
#photopo=tkinter.PhotoImage(file="Tryfont3m.png")

#Doy título a mi Juego

Imagen = tkinter.Label(ventana,text="Road Fighter", font=("Tempus Sans ITC",72)).place(x=450, y=20)

#defino las variables abiertas (no definidas dentro de las funciones)que voy a usar dentro de mis funciones
presiono = False
x = None
i = 0
j = 0
m= 0
i=0
z=0
q=0
g = 0
c = 0
d = 5






#defino canvas principal
fondojuego=tkinter.Canvas(v, width=1350, height=700,bd=0,highlightthickness=0)





#widgest que se crearán a partit de las imágenes con canvas
#mapajuego= fondojuego.create_image(680,200, image=u)#carga
mard=fondojuego.create_image(1145,55, image=fondomarder)
mari=fondojuego.create_image(230,55, image=fondomarizq)
c1=fondojuego.create_image(695,370, image=centro1)#centro estático
x = fondojuego.create_image(100,600,image=carrov1)
k = fondojuego.create_image(97,50,image=vancar)
h=fondojuego.create_image(150,55, image=photo)
f=fondojuego.create_image(250, 55, image=fighter)
van2=fondojuego.create_image(1220,50,image=minivan2)
u2=fondojuego.create_image(1250,600, image= user2)
f2=fondojuego.create_image(1250, 55, image=fi2)
r2=fondojuego.create_image(1100,55, image=run2)
ga=fondojuego.create_image(200,55, image=chargegas)


#movimientofondo
#po=fondojuego.create_image(680,200, image=photopo)


#defino las funciones que van a dinamizar mi juego

def MiniVan(s):
    """
    Esta función mueve verticalmente la MiniVan, un carro de color rojo, cuyo objetivo es moverse verticalmente hacia abajo, siendo un   obstáculo
    para el jugador, que por cierto es el menos peligroso, ya que no cambia de carril mientras se mueve, es decir, su movimiente es constante.
    
    """
    x=random.randint(0,50)
    global fondojuego, m
    
    fondojuego.move(k, 0, s)
        
    if(fondojuego.coords(k)[1]>700):
        fondojuego.move(k,x,-700)

    if(fondojuego.coords(k)[0]>=310):
        fondojuego.move(k,-203,0)

def MiniVan2(s):
    """
    Esta función mueve verticalmenta la MiniVan, un carro de color rojo, cuyo objetivo es moverse verticalmente hacia abajo, siendo un   obstáculo
    para el jugador, que por cierto es el menos peligroso, ya que no cambia de carril mientras se mueve, es decir, su movimiente es constante.
    
    """
    global fondojuego, m

    x=random.randint(0,50)
  
    
    fondojuego.move(van2, 0, s)
        
    if(fondojuego.coords(van2)[1]>700):
        fondojuego.move(van2,x,-700)

    if(fondojuego.coords(van2)[0]>=1220):
        fondojuego.move(van2,-203,0)

def Fighter2(X,Y):
        """
        Esta función mueve al carro de color amarillo , cuyo objetivo es perseguir al carro del jugador para chocarlo, es el enemigo más peligroso de los tres,
        ya que ataca directamente al carro del jugador.
        
        """
     
        if(fondojuego.coords(u2)[0]<fondojuego.coords(f2)[0]):
            fondojuego.move(f2,-X,Y)
            
        if(fondojuego.coords(u2)[0]>fondojuego.coords(f2)[0]):
            fondojuego.move(f2,X,Y)
            
        if(fondojuego.coords(u2)[0]==fondojuego.coords(f2)[0]):
            fondojuego.move(f2,0,Y)
        if(fondojuego.coords(f2)[1]>700):
            fondojuego.move(f2,0,-700)


def Fighter(X,Y):
        """
        Esta función mueve al carro de color amarillo , cuyo objetivo es perseguir al carro del jugador para chocarlo, es el enemigo más peligroso de los tres,
        ya que ataca directamente al carro del jugador.
        
        """
     
        if(fondojuego.coords(x)[0]<fondojuego.coords(f)[0]):
            fondojuego.move(f,-X,Y)
            
        if(fondojuego.coords(x)[0]>fondojuego.coords(f)[0]):
            fondojuego.move(f,X,Y)
            
        if(fondojuego.coords(x)[0]==fondojuego.coords(f)[0]):
            fondojuego.move(f,0,Y)
        if(fondojuego.coords(f)[1]>700):
            fondojuego.move(f,0,-700)

def charge(s):
    """
    Esta función mueve verticalmenta la MiniVan, un carro de color rojo, cuyo objetivo es moverse verticalmente hacia abajo, siendo un   obstáculo
    para el jugador, que por cierto es el menos peligroso, ya que no cambia de carril mientras se mueve, es decir, su movimiente es constante.
    
    """
    global fondojuego, m

    x=random.randint(0,50)
  
    
    fondojuego.move(ga, 0, s)
        
    if(fondojuego.coords(ga)[1]>700):
        fondojuego.move(ga,x,-700)

    if(fondojuego.coords(ga)[0]>=1220):
        fondojuego.move(ga,-203,0)


#usercar

def keyup(e):
  global x,ho

  if(e.keycode in ho):
    ho.pop(ho.index(e.keycode))
   

def keydown(e):
  global x,ho
  if not e.keycode in ho:
      
    ho.append(e.keycode)
  
     
def key():
  global ho
  if(65 in ho):  #letra A en código ascii
    fondojuego.move(x,-5,0)
  if(37 in ho):
    fondojuego.move(u2,-5,0) #flecha de dirección izquiera en código ascii
  if(68 in ho):
    fondojuego.move(x,5,0) #letra D en código ascii
  if(39 in ho):
    fondojuego.move(u2,5,0) #flecha de dirección derecha en código ascii



def Runner():
    """
    Esta función se encarga de mover el carro azul, cuyo objetivo es tratar de chocar al carro del jugador,ncambiando de carril constantemente
    mientras se mueve verticalmente hacia abajo y horizontalmente de derecha a izquierda y visceversa.
    """
    vv=3
    z =fondojuego.coords(h)[0]
    b= 7
    
    y= math.sin(2*fondojuego.coords(h)[1]*math.pi/(300))*b
    if(fondojuego.coords(h)[1]>600):
        fondojuego.move(h,100-z,-600)
        q=0
    fondojuego.move(h,y,vv)


def Runner2():
    """
    Esta función se encarga de mover el carro azul, cuyo objetivo es tratar de chocar al carro del jugador,ncambiando de carril constantemente
    mientras se mueve verticalmente hacia abajo y horizontalmente de derecha a izquierda y visceversa.
    """
    vv=3
    z =fondojuego.coords(r2)[0]
    b= 7
    
    y= math.sin(2*fondojuego.coords(r2)[1]*math.pi/(300))*b
    if(fondojuego.coords(r2)[1]>=600):
        fondojuego.move(r2,1015-z,-600)
        q=0
    fondojuego.move(r2,y,vv)
def colisionesbor():
    """
    Esta función se encarga de hacer el efecto de explosión cuando el carro del jugador toca alguno de los dos extremos de la carretera, implicando
    que si esto sucede, el jugador habrá perdido la partida.
    
    """
    
    x1=fondojuego.coords(x)[0]
    y1=fondojuego.coords(x)[1]
    x2= fondojuego.coords(u2)[0]
    y2=fondojuego.coords(u2)[1]
   

    if(x1<=90):
        coli=fondojuego.create_image(x1,y1,image=explosion)
        return True
    if(x1>=335):
        coli=fondojuego.create_image(x1,y1,image=explosion)
        return True
    if(x2<=1010):
        coli=fondojuego.create_image(x2,y2,image=explosion)
        return True
    if(x2>=1260):
        coli=fondojuego.create_image(x2,y2,image=explosion)
        return True
    
        
    
    """
    
    if(x1>=x2 and x1<=x2+40 and y1>=y2 and y1<=y2+81):
           coli=fondojuego.create_image(x1,y1,image=explosion)
           return True
    if(x1+40>=x2 and x1<=x2+40 and y1+40>=y2 and y1<=y2+81):
           coli=fondojuego.create_image(x1,y1,image=explosion)
           return True
    """
"""
def colisionescarros():
    ""
    Esta función se encarga de hacer el efecto de choque entre el carro del jugador y los enemigos
    ""
    x1=fondojuego.coords(x)[0]
    x2=fondojuego.coords(f)[0]
    x3=fondojuego.coords(k)[0]
    x4=fondojuego.coords(h)[0]
    y1=fondojuego.coords(x)[1]
    y2=fondojuego.coords(f)[1]
    y3=fondojuego.coords(k)[1]
    y4=fondojuego.coords(h)[1]
"""    
    


def fondomoving():
    """
    Esta función se encarga de mover el fondo para que la carretera tenga vida
    """

    global fondojuego, v
    
    if  (colisionesbor()):
        return 0
    else:
        
        fondojuego.move(mard, 0, 15)
        if(fondojuego.coords(mard)[1]>2500):
            fondojuego.move(mard,0,-fondojuego.coords(mard)[1])

def fondomoving2():
    """
    Esta función se encarga de mover el fondo para que la carretera tenga vida
    """

    global fondojuego, v
    
    if  (colisionesbor()):
        return 0
    else:
        
        fondojuego.move(mari, 0, 15)
        if(fondojuego.coords(mari)[1]>2500):
            fondojuego.move(mari,0,-fondojuego.coords(mari)[1])

        
  
           


    
    


    
    
  

v1=0
v2=0
v3=0
F=0

#llamado de funciones
def principal():
    global entrada1
    """
    Esta función se encarga de llamar a todas las funciones antes creadas para que al momento de ser llamada empiecen todos los movimientos y se
    pueda iniciar el juego en el respectivo nivel
    
    """
    if not colisionesbor():
        Fighter(F,v2)
        Fighter2(F,v2)
        Runner()
        Runner2()
        MiniVan(v1)
        MiniVan2(v1)
        charge(v1)
        key()
        fondomoving()
        fondomoving2()
        #var.set(entrada1.get())
        v.after(15,principal)
    else:
        return False
    
#RunnerCar()
def lvl1():
    """
    En esta función se hará el llamado de la función principal, se darán valores para las funciones que tienen parámetros( los cuales se han creado con el fin de
    controlar totalmente, y especialmente para poder darle dificultad a cada nivel , en este caso, al nivel 1), además se agregan condicionales que paran el juego
    en caso de que el jugador pierda la partida
    """
    global v1,v2,F,po
    fondojuego.focus_set()
    
    v.deiconify()
    ventana.iconify()
    v1=2
    v2=3
    F=1
    principal()
    if not (fondomoving()):
        return 0
    if not (fondomoving2()):
        return 0
    #principal()
    #colisiones()
v.iconify()
boton2=tkinter.Button(ventana, image=imagen_2boton,command=lvl1).place(x=1200, y=300)

def lvl2():
    global v1,v2,F
    fondojuego.focus_set()
    v.deiconify()
    ventana.iconify()
    v1=3
    v2=4
    F=1.5
    principal()
v.iconify()
boton3=tkinter.Button(ventana, image=imagen_3boton,command=lvl2).place(x=1200, y=350)

def lvl3():
    global v1,v2,F
    fondojuego.focus_set()
    v.deiconify()
    ventana.iconify()
    v1=5
    v2=7
    F=2
    principal()
v.iconify()
boton4=tkinter.Button(ventana, image=imagen_4boton,command=lvl3).place(x=1200, y=400)

def lvl4():
 global v1,v2,F
 fondojuego.focus_set()
 v.deiconify()
 ventana.iconify()
 v1=6
 v2=8
 F=5
 principal()
v.iconify()
boton5=tkinter.Button(ventana, image=imagen_5boton,command=lvl4).place(x=1200, y=450)

def lvl5():
 global v1,v2,F
 fondojuego.focus_set()
 v.deiconify()
 ventana.iconify()
 v1=10
 v2=10
 F=5
 principal()
v.iconify()
boton6=tkinter.Button(ventana, image=imagen_6boton,command=lvl5).place(x=1200, y=500)

boton1 = tkinter.Button(ventana, image=imagen_1boton,command=ventana.destroy).place(x=1200, y=600)
    


# Liga el evento key al canvas
fondojuego.bind("<KeyPress>",keydown)
fondojuego.bind("<KeyRelease>",keyup)

# Pone el foco en el canvas


#enpaquetado( mostrar lo hecho con canvas)
#entrada1.focus_Set()
fondojuego.pack()
#fondotextos.pack()



#ciclo para escuchar los eventos
v.mainloop()
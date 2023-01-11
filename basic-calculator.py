from tkinter import *

def btn_select(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
 
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""

def clear():
    global operador
    operador=("")
    input_text.set("0")
   

if __name__ == "__main__":
    ventana=Tk()
    ventana.title("Calculadora Sencilla")
    ventana.geometry("392x500")
    ventana.configure(background="chocolate")
    
    color_boton_number=("coral")
    color_boton_op=("coral4")
    ancho_boton=11
    alto_boton=3

    input_text=StringVar()
    operador=""
    
    Salida=Entry(ventana,font=('arial',20,'bold'),width=22,
    textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
    Salida.place(x=10,y=60)
    Button(ventana,text="1",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(1)).place(x=17,y=180)
    Button(ventana,text="2",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(2)).place(x=107,y=180)
    Button(ventana,text="3",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(3)).place(x=197,y=180)
    Button(ventana,text="+",bg=color_boton_op,width=ancho_boton,height=alto_boton,command=lambda:btn_select("+")).place(x=287,y=180)
    Button(ventana,text="4",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(4)).place(x=17,y=240)
    Button(ventana,text="5",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(5)).place(x=107,y=240)
    Button(ventana,text="6",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(6)).place(x=197,y=240)
    Button(ventana,text="-",bg=color_boton_op,width=ancho_boton,height=alto_boton,command=lambda:btn_select("-")).place(x=287,y=240)
    Button(ventana,text="7",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(7)).place(x=17,y=300)
    Button(ventana,text="8",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(8)).place(x=107,y=300)
    Button(ventana,text="9",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select(9)).place(x=197,y=300)
    Button(ventana,text=",",bg=color_boton_op,width=ancho_boton,height=alto_boton,command=lambda:btn_select(".")).place(x=287,y=300)
    Button(ventana,text="0",bg=color_boton_number,width=ancho_boton,height=alto_boton,command=lambda:btn_select("0")).place(x=107,y=360)
    Button(ventana,text="*",bg=color_boton_op,width=ancho_boton,height=alto_boton,command=lambda:btn_select("*")).place(x=197,y=360)
    Button(ventana,text="/",bg=color_boton_op,width=ancho_boton,height=alto_boton,command=lambda:btn_select("/")).place(x=287,y=360)
    Button(ventana,text="C",bg=color_boton_op,width=ancho_boton,height=alto_boton,command=clear).place(x=17,y=360)
    Button(ventana,text="=",bg="coral3",width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=420)
    print("->Calculadora lanzada correctamente")
    
    clear()
    ventana.mainloop()
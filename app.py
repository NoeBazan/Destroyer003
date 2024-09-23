import streamlit as st
import random

# Inicializar variables en la sesión
if 'a1' not in st.session_state:
    st.session_state['a1'] = None
if 'b1' not in st.session_state:
    st.session_state['b1'] = None
if 'c1' not in st.session_state:
    st.session_state['c1'] = None
if 'a2' not in st.session_state:
    st.session_state['a2'] = None
if 'b2' not in st.session_state:
    st.session_state['b2'] = None
if 'c2' not in st.session_state:
    st.session_state['c2'] = None
    
# Función para generar la primera ecuación de primer grado
def generar_ecuacion1():
    # Generar coeficientes aleatorios para la ecuación a1.x + b1.y = c1
    a1 = random.randint(1, 10)
    b1 = random.randint(-10, 10)
    c1 = random.randint(-10, 10)
    st.session_state['a1'] = a1
    st.session_state['b1'] = b1
    st.session_state['c1'] = c1

# Función para generar la segunda ecuación de primer grado
def generar_ecuacion2():
    # Generar coeficientes aleatorios para la ecuación a2.x + b2.y = c2
    a2 = random.randint(1, 10)
    b2 = random.randint(-10, 10)
    c2 = random.randint(-10, 10)
    st.session_state['a2'] = a2
    st.session_state['b2'] = b2
    st.session_state['c2'] = c2

# Función para resolver las ecuaciones
def resolver_ecuacionx(a1, b1, c1, a2, b2, c2):
    if (a1*b1-a2*b1) != 0: 
        return (c1*b2-c2*b1)/(-b1*a2+b2*a1) 
    else:
        return None
        
def resolver_ecuaciony(a1, b1, c1, a2, b2, c2):
    if (a1*b1-a2*b1) != 0: 
        return (c1*a2-c2*a1)/(b1*a2-b2*a1)
    else:
        return None
# Título de la aplicación
st.title("Generador y Solucionador de Ecuaciones de Primer Grado con dos incógnitas")

# Botón para generar una nueva ecuación
if st.button("Proporcionar 2 Ecuaciones con 2 incógnitas"):
    generar_ecuacion1()
    generar_ecuacion2()
    st.write(f"La ecuación generada es: {st.session_state['a1']}.x + {st.session_state['b1']}.y = {st.session_state['c1']}")
    st.write(f"La ecuación generada es: {st.session_state['a2']}.x + {st.session_state['b2']}.y = {st.session_state['c2']}")
# Botón para mostrar la solución
if st.button("¿Quieres conocer la Solución? Presiona aquí"):
    a1 = st.session_state['a1']
    b1 = st.session_state['b1']
    c1 = st.session_state['c1']
    a2 = st.session_state['a2']
    b2 = st.session_state['b2']
    c2 = st.session_state['c2']
    #if a1 is not None and b1 is not None and a2 is not None and b2 is not None:
    if (a1*b2-a2*b1) !=0:
        st.write(f"La solución para las ecuaciones:")
        st.write(f"{a1}.x + {b1}.y = {c1}")
        st.write(f"y")
        st.write(f"{a2}.x + {b2}.y = {c2}")
        solucionx = resolver_ecuacionx(a1, b1, c1, a2, b2, c2)
        soluciony = resolver_ecuaciony(a1, b1, c1, a2, b2, c2)
        if solucionx is not None:
            st.write(f"La solución es: x = {solucionx}")
        else:
            st.write("La ecuación no tiene solución, ya que a = 0.")

        if soluciony is not None:
            st.write(f"La solución es: y = {soluciony}")
        else:
            st.write("La ecuación no tiene solución, ya que a = 0.")        
    else:
        st.write("Primero genera las ecuaciones.")

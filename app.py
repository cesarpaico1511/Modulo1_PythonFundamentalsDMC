
import streamlit as st
import pandas as pd
import numpy as np
import math
from datetime import datetime

# Importación de librerías externas
import libreria_funciones_proyecto1 as funciones
from libreria_clases_proyecto1 import Empleado

# Configuración de la página y Estilo (Azules y Plomo)
st.set_page_config(
    page_title="Proyecto Prototipo Python - Julio Paico",
    page_icon="🐍",
    layout="wide"
)

# Inicialización de estados de sesión (Persistent Data)
if 'movimientos' not in st.session_state:
    st.session_state.movimientos = []
if 'inventario_np' not in st.session_state:
    st.session_state.inventario_np = []
if 'historial_roi' not in st.session_state:
    st.session_state.historial_roi = []
if 'db_empleados' not in st.session_state:
    st.session_state.db_empleados = []

# NAVEGACIÓN LATERAL
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/5968/5968350.png", width=100) # Imagen representativa de Python
    st.title("Panel de Control")
    seleccion = st.sidebar.selectbox(
        "Ir a:",
        ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    )
    st.divider()
    st.info(f"Fecha Actual: {datetime.now().strftime('%d/%m/%Y')}")

# SECCIÓN: HOME 
if seleccion == "Home":
    st.title("🚀 Proyecto Final: Especialización en Python")
    st.subheader("Módulo 1: Desarrollo de Aplicaciones con Streamlit e IA")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Nota: Asegúrate de tener 'innovacion.png' en tu carpeta local. 
        # Aquí uso un placeholder por seguridad.
        st.image("https://via.placeholder.com/200x200.png?text=Logo+Innovacion", caption="Innovación & Tecnología")
    
    with col2:
        st.markdown(f"""
        ### Información del Estudiante
        **Nombre Completo:** Julio Cesar Paico Jaime  
        **Profesión:** Ingeniero de Sistemas  
        **Año:** 2026
        
        ### Descripción del Proyecto
        Esta aplicación integra conceptos avanzados de programación en Python, incluyendo el manejo de estructuras de datos (listas, diccionarios), 
        computación numérica con **NumPy**, análisis de datos con **Pandas**, y Programación Orientada a Objetos (**POO**). 
        Todo esto empaquetado en una interfaz reactiva utilizando **Streamlit**.
        """)

    st.markdown("---")
    st.subheader("🛠️ Tecnologías Utilizadas")
    st.write("- **Python 3.12+**: Lenguaje base.")
    st.write("- **Streamlit**: Framework para el frontend.")
    st.write("- **NumPy & Pandas**: Procesamiento de datos.")
    st.write("- **Programación Modular**: Integración de funciones y clases externas.")

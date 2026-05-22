import streamlit as st
import pandas as pd
import numpy as np
import math
from datetime import datetime

# Importación de librerías externas
#import libreria_funciones_proyecto1 as funciones
#from libreria_clases_proyecto1 import Empleado


# Configuración de la página y Estilo (Azules y Plomo)
st.set_page_config(
    page_title="Proyecto Prototipo Python - Julio Paico",
    page_icon="🐍",
    layout="wide"
)

st.markdown(
    """
    <style>
        .main-card {
            background-color: #F7F9FC;
            padding: 22px;
            border-radius: 14px;
            border: 1px solid #E3E8EF;
            margin-bottom: 18px;
        }
        .info-text {
            font-size: 16px;
            color: #333333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if "actividades" not in st.session_state:
    st.session_state.actividades = []


def formatear_moneda(valor):
    return f"S/ {valor:,.2f}"


def obtener_estado_presupuesto(presupuesto, gasto_real):
    if gasto_real <= presupuesto:
        return "Dentro del presupuesto"
    return "Presupuesto excedido"


def cargar_datos_ejemplo():
    st.session_state.actividades = [
        {
            "nombre": "Campaña digital",
            "tipo": "Marketing",
            "presupuesto": 1500.00,
            "gasto_real": 1200.00
        },
        {
            "nombre": "Compra de materiales",
            "tipo": "Operaciones",
            "presupuesto": 2000.00,
            "gasto_real": 2300.00
        },
        {
            "nombre": "Capacitación Python",
            "tipo": "Formación",
            "presupuesto": 900.00,
            "gasto_real": 850.00
        }
    ]


def calcular_retorno(actividad, tasa, meses):
    return actividad["presupuesto"] * tasa * meses


class Actividad:
    def __init__(self, nombre, tipo, presupuesto, gasto_real):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

    def esta_en_presupuesto(self):
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self):
        diferencia = self.presupuesto - self.gasto_real
        return (
            f"Actividad: {self.nombre} | "
            f"Tipo: {self.tipo} | "
            f"Presupuesto: {formatear_moneda(self.presupuesto)} | "
            f"Gasto real: {formatear_moneda(self.gasto_real)} | "
            f"Diferencia: {formatear_moneda(diferencia)}"
        )


def mostrar_home():
    st.title("Módulo 1")
    st.write("Especialización Python for Analytics")

    banner_path = Path("assets/banner.png")

    if banner_path.exists():
        st.image(str(banner_path), use_container_width=True)

    st.markdown(
        """
        <div class="main-card">
            <h3>Presentación del proyecto</h3>
            <p class="info-text">
                Esta aplicación interactiva integra los fundamentos de programación
                en Python desarrollados en el Módulo 1. El proyecto permite aplicar
                variables, condicionales, estructuras de datos, funciones,
                programación funcional y programación orientada a objetos mediante
                ejercicios prácticos orientados al análisis de actividades financieras.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Datos del trabajo")
        st.write("**Título del proyecto:** Módulo 1")
        st.write("**Estudiante:** Julio Cesar Paico Jaime")
        st.write("**Especialización:** Python for Analytics")
        st.write("**Curso / Módulo:** Python Fundamentals") 
        st.write("**Docente:** MSc. Carlos Carrillo Villavicencio")
        st.write("**Año:** 2026")

    with col2:
        st.subheader("Tecnologías utilizadas")
        st.write("- Python")
        st.write("- Streamlit")
        st.write("- Pandas")
        st.write("- HTML y CSS mediante `st.markdown()`")

    st.info("Utilice el menú lateral para navegar por los ejercicios.")


def mostrar_ejercicio_1():
    st.subheader("Ejercicio 1 - Variables y Condicionales")

    st.write(
        "Ingrese un presupuesto y un gasto. El sistema evaluará si el gasto "
        "está dentro o fuera del presupuesto."
    )

    col1, col2 = st.columns(2)

    with col1:
        presupuesto = st.number_input(
            "Presupuesto",
            min_value=0.0,
            value=1000.0,
            step=50.0
        )

    with col2:
        gasto = st.number_input(
            "Gasto",
            min_value=0.0,
            value=800.0,
            step=50.0
        )

    if st.button("Evaluar presupuesto"):
        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto.")
        else:
            st.warning("El gasto excede el presupuesto.")

        st.write(f"**Presupuesto:** {formatear_moneda(presupuesto)}")
        st.write(f"**Gasto:** {formatear_moneda(gasto)}")
        st.write(f"**Diferencia:** {formatear_moneda(diferencia)}")


def mostrar_ejercicio_2():
    st.subheader("Ejercicio 2 - Listas y Diccionarios")

    st.write(
        "Registre actividades financieras. Cada actividad será almacenada "
        "como un diccionario dentro de una lista."
    )

    with st.form("formulario_actividad"):
        nombre = st.text_input("Nombre de la actividad")

        tipo = st.selectbox(
            "Tipo de actividad",
            [
                "Marketing",
                "Operaciones",
                "Formación",
                "Ventas",
                "Administración",
                "Otro"
            ]
        )

        presupuesto = st.number_input(
            "Presupuesto",
            min_value=0.0,
            value=0.0,
            step=50.0
        )

        gasto_real = st.number_input(
            "Gasto real",
            min_value=0.0,
            value=0.0,
            step=50.0
        )

        agregar = st.form_submit_button("Agregar actividad")

    if agregar:
        if nombre.strip() == "":
            st.warning("Debe ingresar el nombre de la actividad.")
        else:
            actividad = {
                "nombre": nombre.strip(),
                "tipo": tipo,
                "presupuesto": float(presupuesto),
                "gasto_real": float(gasto_real)
            }

            st.session_state.actividades.append(actividad)
            st.success("Actividad agregada correctamente.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Cargar datos de ejemplo"):
            cargar_datos_ejemplo()
            st.success("Datos de ejemplo cargados.")

    with col2:
        if st.button("Limpiar actividades"):
            st.session_state.actividades = []
            st.info("La lista de actividades fue limpiada.")

    if len(st.session_state.actividades) > 0:
        tabla = pd.DataFrame(st.session_state.actividades)

        tabla["estado"] = tabla.apply(
            lambda fila: obtener_estado_presupuesto(
                fila["presupuesto"],
                fila["gasto_real"]
            ),
            axis=1
        )

        tabla["diferencia"] = tabla["presupuesto"] - tabla["gasto_real"]

        st.write("### Lista de actividades registradas")
        st.dataframe(tabla, use_container_width=True)

        st.write("### Evaluación de cada actividad")

        for actividad in st.session_state.actividades:
            estado = obtener_estado_presupuesto(
                actividad["presupuesto"],
                actividad["gasto_real"]
            )
            diferencia = actividad["presupuesto"] - actividad["gasto_real"]

            st.write(
                f"- **{actividad['nombre']}** ({actividad['tipo']}): "
                f"{estado}. Diferencia: {formatear_moneda(diferencia)}"
            )
    else:
        st.info("Aún no existen actividades registradas.")


def mostrar_ejercicio_3():
    st.subheader("Ejercicio 3 - Funciones y Programación Funcional")

    st.write(
        "Se calculará el retorno esperado de cada actividad utilizando una "
        "función, `map()` y `lambda`."
    )

    if len(st.session_state.actividades) == 0:
        st.warning(
            "Primero registre actividades en el Ejercicio 2 o cargue datos de ejemplo."
        )
        return

    tasa_porcentaje = st.slider(
        "Tasa mensual esperada (%)",
        min_value=0.0,
        max_value=20.0,
        value=5.0,
        step=0.5
    )

    meses = st.number_input(
        "Cantidad de meses",
        min_value=1,
        max_value=60,
        value=6,
        step=1
    )

    if st.button("Calcular retorno esperado"):
        tasa_decimal = tasa_porcentaje / 100

        resultados = list(
            map(
                lambda actividad: {
                    "nombre": actividad["nombre"],
                    "tipo": actividad["tipo"],
                    "presupuesto": actividad["presupuesto"],
                    "retorno_esperado": calcular_retorno(
                        actividad,
                        tasa_decimal,
                        meses
                    )
                },
                st.session_state.actividades
            )
        )

        tabla_resultados = pd.DataFrame(resultados)

        st.write("### Resultados")
        st.dataframe(tabla_resultados, use_container_width=True)

        for resultado in resultados:
            st.write(
                f"- **{resultado['nombre']}**: "
                f"retorno esperado de {formatear_moneda(resultado['retorno_esperado'])}"
            )


def mostrar_ejercicio_4():
    st.subheader("Ejercicio 4 - Programación Orientada a Objetos")

    st.write(
        "Se convertirán las actividades registradas en objetos de la clase "
        "`Actividad`."
    )

    if len(st.session_state.actividades) == 0:
        st.warning(
            "Primero registre actividades en el Ejercicio 2 o cargue datos de ejemplo."
        )
        return

    objetos_actividad = list(
        map(
            lambda actividad: Actividad(
                actividad["nombre"],
                actividad["tipo"],
                actividad["presupuesto"],
                actividad["gasto_real"]
            ),
            st.session_state.actividades
        )
    )

    st.write("### Información de los objetos creados")

    for objeto in objetos_actividad:
        st.write(objeto.mostrar_info())

        if objeto.esta_en_presupuesto():
            st.success("La actividad cumple con el presupuesto.")
        else:
            st.warning("La actividad excede el presupuesto.")


st.sidebar.title("Menú de navegación")

opcion = st.sidebar.selectbox(
    "Seleccione un módulo",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("**Proyecto:** Módulo 1")
st.sidebar.write("**Curso:** Python Fundamentals")
st.sidebar.write("**Año:** 2026")

if opcion == "Home":
    mostrar_home()
elif opcion == "Ejercicio 1":
    mostrar_ejercicio_1()
elif opcion == "Ejercicio 2":
    mostrar_ejercicio_2()
elif opcion == "Ejercicio 3":
    mostrar_ejercicio_3()
elif opcion == "Ejercicio 4":
    mostrar_ejercicio_4()

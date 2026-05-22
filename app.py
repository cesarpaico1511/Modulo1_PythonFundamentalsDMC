import streamlit as st
import pandas as pd
import numpy as np
import math
from datetime import datetime

# Importación de librerías externas
import libreria_funciones_proyecto1 as funciones
#from librería_clases_proyecto1 import Empleado


# Configuración de la página y Estilo (Azules y Plomo)
st.set_page_config(
    page_title="Python Módulo 1 - Julio Cesar Paico Jaime",
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
    st.image("https://images/Python_logo.png.flaticon.com/512/5968/5968350.png", width=100) # Imagen representativa de Python
    st.title("Panel de Control")
    seleccion = st.sidebar.selectbox(
        "Ir a:",
        ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    )
    st.divider()
    st.info(f"Fecha Actual: {datetime.now().strftime('%d/%m/%Y')}")

# SECCIÓN: HOME 
if seleccion == "Home":
    st.title("🚀 Especialización en Python Potenciado con IA - Edición 58")
    st.subheader("Módulo 1: Desarrollo de Aplicaciones con Python y Streamlit")
    
    col1, col2 = st.columns([1, 2])
    with col1:
       st.image("images/innovacion.png", caption="Innovación & Tecnología")
            
    with col2:
        st.markdown(f"""
        ### Información del Estudiante
        **Nombre Completo:** Julio Cesar Paico Jaime  
        **Profesión:** Ingeniero de Sistemas  
        **Año:** 2026
        
        ### Descripción del Proyecto
        Esta aplicación integra conceptos de programación en Python, incluyendo el manejo de estructuras de datos (listas, diccionarios), 
        computación numérica con **NumPy**, análisis de datos con **Pandas**, y Programación Orientada a Objetos (**POO**). 
        Todo esto empaquetado en una interfaz reactiva utilizando **Streamlit**.
        """)

    st.markdown("---")
    st.subheader("🛠️ Tecnologías Utilizadas")
    st.write("- **Python 3.12+**: Lenguaje base.")
    st.write("- **Streamlit**: Framework para el frontend.")
    st.write("- **NumPy & Pandas**: Procesamiento de datos.")
    st.write("- **Programación Modular**: Integración de funciones y clases externas.")

# --- SECCIÓN: EJERCICIO 1 (LISTAS Y FLUJO DE CAJA) ---
elif seleccion == "Ejercicio 1":
    st.title("💰 Gestión de Flujo de Caja")
    st.markdown("> Registro de movimientos financieros utilizando estructuras de listas dinámicas.")
    
    col_f1, col_f2 = st.columns([1, 2])
    
    with col_f1:
        st.subheader("Nuevo Movimiento")
        concepto = st.text_input("Concepto", placeholder="Ej. Pago de Alquiler")
        tipo = st.selectbox("Tipo de Movimiento", ["Ingreso", "Gasto"])
        valor = st.number_input("Monto (S/.)", min_value=0.0, step=10.0)
        
        if st.button("➕ Agregar Movimiento"):
            if concepto:
                st.session_state.movimientos.append({
                    "Concepto": concepto,
                    "Tipo": tipo,
                    "Monto": valor if tipo == "Ingreso" else -valor
                })
                st.success("Registrado correctamente.")
            else:
                st.error("Debe ingresar un concepto.")

    with col_f2:
        st.subheader("Historial y Resultados")
        if st.session_state.movimientos:
            df_movs = pd.DataFrame(st.session_state.movimientos)
            st.dataframe(df_movs, use_container_width=True)
            
            ingresos = sum(m['Monto'] for m in st.session_state.movimientos if m['Tipo'] == "Ingreso")
            gastos = sum(abs(m['Monto']) for m in st.session_state.movimientos if m['Tipo'] == "Gasto")
            saldo = ingresos - gastos
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Ingresos Total", f"S/ {ingresos:,.2f}")
            c2.metric("Gastos Total", f"S/ {gastos:,.2f}", delta_color="inverse")
            c3.metric("Saldo Final", f"S/ {saldo:,.2f}")
            
            if saldo >= 0:
                st.success("✅ El flujo de caja está A FAVOR.")
            else:
                st.error("⚠️ El flujo de caja está EN CONTRA.")
        else:
            st.info("No hay movimientos registrados aún.")

# --- SECCIÓN: EJERCICIO 2 (NUMPY Y DATAFRAMES) ---
elif seleccion == "Ejercicio 2":
    st.title("📦 Registro de Inventario con NumPy")
    st.markdown("Uso de arreglos multidimensionales para optimizar el almacenamiento de datos de productos.")
    
    with st.form("form_inventario"):
        c1, c2 = st.columns(2)
        nombre = c1.text_input("Producto")
        cat = c1.selectbox("Categoría", ["Electrónica", "Hogar", "Oficina"])
        precio = c2.number_input("Precio Unitario", min_value=0.1)
        cantidad = c2.number_input("Cantidad en Stock", min_value=1)
        
        enviado = st.form_submit_button("Registrar Producto")
        if enviado and nombre:
            total = precio * cantidad
            # Guardamos como una fila de datos
            nuevo_registro = [nombre, cat, precio, cantidad, total]
            st.session_state.inventario_np.append(nuevo_registro)

    if st.session_state.inventario_np:
        # Convertimos la lista de registros a un Array de NumPy
        np_data = np.array(st.session_state.inventario_np, dtype=object)
        
        # Convertimos el Array a DataFrame para visualización
        df_inv = pd.DataFrame(np_data, columns=["Nombre", "Categoría", "Precio", "Cantidad", "Total"])
        
        st.subheader("Vista General del Inventario")
        st.dataframe(df_inv, use_container_width=True)
        
        # Operación adicional con NumPy: Sumar el total de la última columna
        gran_total = np.sum(np_data[:, 4])
        st.write(f"**Valor total del inventario:** S/ {gran_total:,.2f}")
    else:
        st.warning("El inventario está vacío.")

# --- SECCIÓN: EJERCICIO 3 (LIBRERÍA DE FUNCIONES) ---
elif seleccion == "Ejercicio 3":
    st.title("📊 Análisis Financiero (Funciones)")
    st.markdown("Integración de la función `calcular_rentabilidad_esperada` desde `libreria_funciones_proyecto1.py`.")
    
    st.subheader("Calculadora de Rentabilidad")
    capital = st.number_input("Capital Invertido (S/.)", min_value=0.1, key="cap_roi")
    utilidad = st.number_input("Utilidad Esperada (S/.)", min_value=0.0, key="ut_roi")
    
    if st.button("🚀 Ejecutar Cálculo"):
        try:
            # Llamada a la función de la librería externa
            resultado = funciones.calcular_rentabilidad_esperada(capital, utilidad)
            pct = resultado["rentabilidad_esperada_pct"]
            
            st.write(f"### Rentabilidad Estimada: {pct}%")
            
            # Guardar en histórico
            st.session_state.historial_roi.append({
                "Fecha": datetime.now().strftime("%H:%M:%S"),
                "Capital": capital,
                "Utilidad": utilidad,
                "Resultado %": pct
            })
        except ValueError as e:
            st.error(f"Error en validación: {e}")

    if st.session_state.historial_roi:
        st.markdown("---")
        st.subheader("📜 Histórico de Consultas")
        st.dataframe(pd.DataFrame(st.session_state.historial_roi), use_container_width=True)

# --- SECCIÓN: EJERCICIO 4 (POO Y CRUD) ---
elif seleccion == "Ejercicio 4":
    st.title("👥 Gestión de Empleados (CRUD & POO)")
    st.markdown("Implementación de la clase `Empleado` con operaciones de creación, lectura, actualización y eliminación.")

    tab1, tab2, tab3 = st.tabs(["🆕 Crear / Ver", "📝 Actualizar", "🗑️ Eliminar"])

    with tab1:
        st.subheader("Nuevo Registro")
        with st.form("crear_empleado"):
            nom_emp = st.text_input("Nombre del Empleado")
            sal_base = st.number_input("Salario Base", min_value=1.0)
            bono_pct = st.slider("Bono (%)", 0, 100, 0)
            desc_pct = st.slider("Descuento (%)", 0, 100, 0)
            
            if st.form_submit_button("Registrar"):
                # Instanciación de Clase
                emp = Empleado(nom_emp, sal_base, bono_pct, desc_pct)
                st.session_state.db_empleados.append(emp)
                st.success(f"Empleado {nom_emp} añadido.")

        st.subheader("Lista de Empleados")
        if st.session_state.db_empleados:
            data_resumen = [e.resumen() for e in st.session_state.db_empleados]
            st.dataframe(pd.DataFrame(data_resumen), use_container_width=True)
        else:
            st.info("Sin registros.")

    with tab2:
        if st.session_state.db_empleados:
            nombres = [e.nombre for e in st.session_state.db_empleados]
            seleccion_edit = st.selectbox("Seleccione empleado a editar", nombres)
            
            # Buscar el objeto
            idx = nombres.index(seleccion_edit)
            emp_obj = st.session_state.db_empleados[idx]
            
            new_sal = st.number_input("Nuevo Salario", value=float(emp_obj.salario_base))
            if st.button("Actualizar Datos"):
                st.session_state.db_empleados[idx].salario_base = new_sal
                st.success("Salario actualizado correctamente.")
                st.rerun()
        else:
            st.write("No hay datos para editar.")

    with tab3:
        if st.session_state.db_empleados:
            nombres_del = [e.nombre for e in st.session_state.db_empleados]
            seleccion_del = st.selectbox("Seleccione empleado a eliminar", nombres_del)
            
            if st.button("❗ Confirmar Eliminación"):
                idx_del = nombres_del.index(seleccion_del)
                st.session_state.db_empleados.pop(idx_del)
                st.warning("Registro eliminado.")
                st.rerun()
        else:
            st.write("No hay datos para eliminar.")

# 🚗 Sistema Básico de Gestión de Garaje

Aplicación de escritorio desarrollada en Python con Tkinter para registrar y visualizar vehículos en un garaje.

## 📋 Descripción

Esta aplicación permite:
- ✅ Registrar vehículos con placa, marca y propietario
- ✅ Visualizar todos los vehículos registrados en una tabla
- ✅ Limpiar el formulario de registro
- ✅ Eliminar vehículos registrados
- ✅ Validar campos vacíos y placas duplicadas

## 🏗️ Arquitectura del Proyecto

garaje_app/.
├── main.py # Punto de entrada.
├── modelos/ # Clases de datos.
│ └── vehiculo.py.
├── servicios/ # Lógica de negocio.
│ └── garaje_servicio.py.
└── ui/ # Interfaz gráfica.
└── app_tkinter.py.


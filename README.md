# Sistema Integral de Gestión de Clientes, Servicios y Reservas

Proyecto desarrollado para la Fase 4 del curso **Programación 213023** de la Universidad Nacional Abierta y a Distancia — UNAD.

## Autor

**Johan Camilo Forero Prieto**

## Descripción

Este proyecto implementa un sistema integral orientado a objetos para la empresa ficticia **Software FJ**.

El sistema permite gestionar:

- Clientes.
- Reservas de salas.
- Alquiler de equipos.
- Asesorías especializadas.
- Confirmación, procesamiento y cancelación de reservas.
- Registro de servicios y reservas mediante listas internas.
- Manejo controlado de errores.
- Registro de eventos y excepciones en un archivo de logs.

La solución no utiliza bases de datos. La información se administra mediante objetos y listas durante la ejecución del programa.

## Objetivo

Desarrollar una aplicación estable, modular y extensible que implemente los principios de programación orientada a objetos y manejo avanzado de excepciones.

## Principios de programación orientada a objetos

El proyecto demuestra los siguientes principios:

### Abstracción

Se implementan las clases abstractas:

- `Entidad`
- `Servicio`

Estas clases definen características y comportamientos generales que deben implementar las clases derivadas.

### Herencia

Las clases especializadas heredan características de las clases abstractas:

- `Cliente` hereda de `Entidad`.
- `ReservaSala` hereda de `Servicio`.
- `AlquilerEquipo` hereda de `Servicio`.
- `AsesoriaEspecializada` hereda de `Servicio`.

### Encapsulación

Los atributos principales se protegen utilizando nombres precedidos por guion bajo, por ejemplo:

```python
self._nombre
self._correo
self._telefono
```

El acceso a estos atributos se realiza mediante propiedades.

### Polimorfismo

Los servicios especializados implementan de forma diferente los métodos:

```python
calcular_costo()
describir_servicio()
validar_parametros()
```

Cada tipo de servicio utiliza reglas particulares para calcular su costo.

## Servicios implementados

### Reserva de salas

Permite:

- Definir una tarifa por hora.
- Establecer la capacidad máxima.
- Validar la cantidad de personas.
- Aplicar descuentos e impuestos.
- Controlar la disponibilidad.

### Alquiler de equipos

Permite:

- Definir una tarifa diaria.
- Registrar la cantidad disponible.
- Validar la cantidad solicitada.
- Calcular costos según días y cantidad de equipos.
- Aplicar descuentos e impuestos.

### Asesorías especializadas

Permite:

- Definir una especialidad.
- Asignar un nivel de experiencia.
- Calcular costos según el nivel del asesor.
- Aplicar un descuento automático por duración.
- Aplicar impuestos.

Los niveles disponibles son:

- Junior.
- Semisenior.
- Senior.

## Gestión de reservas

La clase `Reserva` integra:

- Cliente.
- Servicio.
- Duración.
- Descuento.
- Impuesto.
- Costo total.
- Estado de la reserva.

Los estados utilizados son:

```text
PENDIENTE
CONFIRMADA
PROCESADA
CANCELADA
```

La reserva permite ejecutar las siguientes operaciones:

```python
confirmar()
procesar()
cancelar()
mostrar_resumen()
```

También impide operaciones no permitidas, como:

- Procesar una reserva sin confirmar.
- Confirmar una reserva que no está pendiente.
- Cancelar una reserva procesada.
- Cancelar dos veces la misma reserva.
- Crear una reserva para un servicio no disponible.

## Manejo de excepciones

El sistema utiliza excepciones propias para controlar los errores:

- `SistemaFJError`
- `ClienteInvalidoError`
- `ServicioInvalidoError`
- `ServicioNoDisponibleError`
- `ReservaInvalidaError`
- `OperacionNoPermitidaError`

Se implementan estructuras como:

```python
try
except
else
finally
```

También se utiliza encadenamiento de excepciones mediante:

```python
raise ReservaInvalidaError(...) from error_original
```

Esto permite conservar la causa original de un error de conversión.

## Registro de logs

Los errores y eventos importantes se almacenan automáticamente en:

```text
logs/sistema.log
```

El archivo registra:

- Fecha y hora.
- Nivel del evento.
- Mensaje informativo.
- Errores controlados.
- Rastreo de excepciones encadenadas.

## Gestión mediante listas internas

La clase `SistemaReservas` utiliza tres listas privadas:

```python
self._clientes
self._servicios
self._reservas
```

El gestor permite:

- Registrar clientes.
- Registrar servicios.
- Registrar reservas.
- Buscar registros.
- Evitar códigos e identificaciones duplicadas.
- Consultar la cantidad de elementos almacenados.

## Simulaciones realizadas

El proyecto contiene 19 pruebas secuenciales:

1. Excepción personalizada.
2. Clase abstracta `Entidad`.
3. Cliente válido.
4. Cliente con correo inválido.
5. Clase abstracta `Servicio`.
6. Reserva de sala válida.
7. Sala con capacidad inválida.
8. Alquiler de equipo válido.
9. Cantidad de equipos no disponible.
10. Asesoría especializada válida.
11. Asesoría sin especialidad.
12. Reserva válida.
13. Procesamiento de reserva sin confirmar.
14. Servicio no disponible.
15. Cancelación doble.
16. Gestor con listas internas.
17. Cliente duplicado.
18. Conversión válida de duración.
19. Encadenamiento de excepciones.

Los casos inválidos son controlados sin detener la ejecución general del programa.

## Estructura del proyecto

```text
software-fj-fase-4/
│
├── main.py
├── README.md
├── .gitignore
│
├── excepciones/
│   ├── __init__.py
│   └── excepciones_personalizadas.py
│
├── gestor/
│   ├── __init__.py
│   └── sistema_reservas.py
│
├── modelos/
│   ├── __init__.py
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   ├── asesoria_especializada.py
│   └── reserva.py
│
├── pruebas/
│   ├── __init__.py
│   └── simulaciones.py
│
├── utilidades/
│   ├── __init__.py
│   ├── configuracion_logs.py
│   └── validadores.py
│
└── logs/
    └── sistema.log
```

## Requisitos

Para ejecutar el proyecto se requiere:

- Python 3.12 o una versión posterior.
- Visual Studio Code u otro editor compatible.
- Git, en caso de utilizar control de versiones.

No se requieren librerías externas ni una base de datos.

## Ejecución

Abrir una terminal ubicada en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

El programa ejecutará secuencialmente las 19 simulaciones y mostrará al final:

```text
Ejecución finalizada correctamente.
```

## Repositorio

El proyecto se encuentra disponible en GitHub:

```text
https://github.com/operjohancamilof-cell/software-fj-fase-4
```

## Conclusión

El proyecto demuestra la implementación de una arquitectura modular orientada a objetos, utilizando abstracción, herencia, encapsulación y polimorfismo.

El manejo de excepciones permite controlar datos inválidos, operaciones no permitidas, servicios no disponibles y errores de conversión sin interrumpir la ejecución general de la aplicación.

El uso de listas internas permite gestionar clientes, servicios y reservas sin utilizar una base de datos, mientras que el archivo de logs conserva la trazabilidad de los eventos y errores relevantes.
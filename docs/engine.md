# Core Engine & Algorithmic Loop

El módulo `core` contiene el motor de ejecución (`Engine`) que orquesta la simulación del backtest. Este documento explica su arquitectura y flujo de ejecución.

## The Event Loop (Bucle de Eventos)

A diferencia de los backtesters vectorizados que calculan todo de golpe, este motor utiliza una arquitectura **Event-Driven** (dirigida por eventos). Esto significa que el sistema itera sobre los datos históricos vela a vela (o tick a tick), simulando el paso del tiempo real.

### Ciclo de Ejecución

1.  **Inicialización (`Strategy.init`)**:
    *   Se ejecuta **una sola vez** al inicio.
    *   Aquí es donde la estrategia pre-calcula indicadores técnicos de forma eficiente (usando Polars).
    *   Se configuran parámetros y artefactos.

2.  **Bucle Principal (`Engine.run`)**:
    *   El motor itera desde el índice `0` hasta `N` (longitud de los datos).
    *   En cada paso `i`:
        1.  **Actualización de Contexto**: El `Engine` actualiza el puntero interno del `DataModel` al índice `i`.
        2.  **Chequeo de Órdenes (OMS)**: (Pendiente) Se verifica si hay órdenes pendientes que deban ejecutarse con el precio actual.
        3.  **Lógica de Estrategia (`Strategy.next`)**: Se invoca el método `next()` de la estrategia.

3.  **Finalización**:
    *   Se cierran posiciones abiertas (opcional).
    *   Se generan reportes.

## Prevención de Sesgo de Futuro (Look-Ahead Bias)

Para garantizar la integridad de la simulación, la estrategia no tiene acceso directo al DataFrame completo de Polars durante el bucle `next()`.

*   **Acceso Controlado**: La clase `DataModel` expone propiedades (`.close`, `.open`, etc.) que devuelven **exclusivamente** el valor en el índice actual `_current_index`.
*   Esto impide que una estrategia consulte accidentalmente el precio de cierre de mañana para tomar una decisión hoy.

```python
# Ejemplo en Strategy.next()
def next(self):
    # Correcto: Obtiene el precio de cierre de la vela actual
    current_price = self.data.close 
    
    # Incorrecto (No permitido/No accesible fácilmente): 
    # self.data.data['close'][i+1]
```

## Referencia de Clases

### `core.engine.Engine`
*   `__init__(self, strategy, data)`: Vincula la estrategia con los datos.
*   `run(self)`: Inicia la simulación.

### `Strategy.strategy.Strategy`
*   `init(self)`: Definición de indicadores.
*   `next(self)`: Lógica de trading por evento.

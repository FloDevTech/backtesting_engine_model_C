# Documentación de Modelos

Este documento proporciona una guía detallada sobre los modelos utilizados en el sistema de backtesting.

## Tabla de Contenidos

1. [CommissionModel](#commissionmodel)
2. [DataModel](#datamodel)
3. [Instrument](#instrument)
4. [SlippageModel](#slippagemodel)
5. [SwapModel](#swapmodel)
6. [Enums](#enums)

---

## CommissionModel

El módulo `commission_model.py` define clases para manejar diferentes tipos de comisiones aplicables a las operaciones.

### Clase Base: `CommissionModel`

Clase base para todos los modelos de comisión.

**Atributos:**
- `commision` (float): Valor de la comisión.
- `name` (str): Nombre del modelo.
- `type` (TypeChange): Tipo de comisión (MONEY, PERCENTAGE, POINT).

### Subclases

#### `CommissionMoney`
Calcula la comisión como un monto fijo monetario por operación/lote.
- **Constructor**: `__init__(commission: float)`

#### `CommissionPorcentage`
Calcula la comisión como un porcentaje del valor de la operación.
- **Constructor**: `__init__(commission: float)`

#### `CommissionPoint`
Calcula la comisión basada en puntos o pips.
- **Constructor**: `__init__(commission: float)`

#### `CommissionNone`
Representa la ausencia de comisiones (comisión cero).

---

## DataModel

El módulo `data_model.py` contiene la clase `DataModel`, responsable de cargar y manipular los datos históricos de los instrumentos.

### Clase: `DataModel`

Maneja la carga de datos desde CSV y operaciones como el remuestreo (resampling).

**Atributos:**
- `name` (str): Nombre del modelo de datos.
- `instrument` (Instrument): Instrumento asociado.
- `data` (pl.DataFrame): Datos cargados (Polars DataFrame).
- `time_frame` (TimeFrame): Timeframe de los datos.

**Métodos Principales:**

#### `load_data_from_csv(path_txt: str, has_header: bool = True)`
Carga datos históricos desde un archivo CSV. Soporta detección automática de ciertos formatos de fecha y hora.

- **Parámetros:**
  - `path_txt`: Ruta al archivo CSV.
  - `has_header`: Indica si el archivo tiene cabecera.

#### `resample_data(target_timeframe: TimeFrame, time_col: str, resampling_forward: bool)`
Realiza el remuestreo de los datos a un timeframe superior (ej. de 1 minuto a 1 hora).

- **Parámetros:**
  - `target_timeframe`: Timeframe objetivo.
  - `time_col`: Columna de tiempo a usar.
  - `resampling_forward`: Dirección del remuestreo.

---

## Instrument

El módulo `instrument_model.py` define la clase `Instrument`.

### Clase: `Instrument`

Representa un instrumento financiero con todas sus propiedades y reglas de negociación.

**Atributos y Constructor:**

- `name` (str): Nombre del instrumento.
- `description` (str): Descripción.
- `data_type` (DataType): Tipo de activo (ej. STOCK, FOREX).
- `point_value` (float): Valor monetario de un punto.
- `pip_tick_size` (float): Tamaño mínimo de movimiento de precio.
- `pip_tick_step` (float): Paso del movimiento.
- `default_spread_pip` (float): Spread por defecto en pips.
- `default_slippage_pip` (float): Slippage por defecto en pips.
- `commission_model` (CommissionModel): Modelo de comisión asociado.
- `swap` (SwapModel): Modelo de swap asociado.
- `slippage_model` (SlippageModel): Modelo de slippage asociado.

---

---

## SlippageModel

El módulo `slippage_model.py` define clases para simular el deslizamiento (slippage) en las ejecuciones de órdenes.

### Clase Base: `SlippageModel`

**Atributos:**
- `slippage` (float): Valor del slippage.
- `name` (str): Nombre del modelo.
- `type` (TypeChange): Tipo de slippage (MONEY, PERCENTAGE, POINT).

### Subclases

#### `SlippageMoney`
Aplica un slippage fijo monetario.
- **Constructor**: `__init__(slippage: float)`

#### `SlippagePercentage`
Aplica un slippage como porcentaje del precio.
- **Constructor**: `__init__(slippage: float)`

#### `SlippagePoint`
Aplica un slippage basado en puntos o pips.
- **Constructor**: `__init__(slippage: float)`

#### `SlippageNone`
Sin slippage.

---

## SwapModel

El módulo `swap_model.py` define clases para calcular el swap (interés nocturno) de las posiciones abiertas.

### Clase Base: `SwapModel`

**Atributos:**
- `type` (TypeChange): Tipo de swap.
- `swap_long` (float): Valor del swap para posiciones largas.
- `swap_short` (float): Valor del swap para posiciones cortas.
- `day_swap` (Days): Día de la semana donde se cobra el triple swap.
- `rollover_swap_hour` (float): Hora del rollover.

### Subclases

- `SwapMoney`: Swap como monto fijo.
- `SwapPorcentage`: Swap como porcentaje.
- `SwapPoint`: Swap en puntos.
- `SwapNone`: Sin swap.

---

## Enums

El módulo `model.py` define enumeraciones utilizadas en todo el sistema.

### `DataType`
Tipos de instrumentos soportados:
- `STOCK`, `FUTURES`, `FOREX`, `CFD`, `ETF`, `INDEX`, `CRYPTO`.

### `TypeChange`
Tipos de ajustes para comisiones y swaps:
- `NONE`, `PERCENTAGE`, `MONEY`, `POINT`.

### `Days`
Días de la semana (MON-SUN).

### `TimeFrame`
Timeframes estándares para datos y operaciones:
- `M1`, `M5`, `M15`, `M30`
- `H1`, `H2`, `H3`, `H4`, `H6`, `H8`, `H12`
- `D`, `W`, `MO`

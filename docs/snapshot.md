# 📸 Snapshot del Proyecto

Este archivo documenta el estado actual del desarrollo del **Strategy Factory Backtesting Engine**. Su objetivo es servir como punto de restauración conceptual en caso de necesitar retroceder o re-evaluar la dirección del proyecto.

## Estado Actual: **Fase 2 - Core Engine (En Progreso)**

**Fecha:** 2026-01-06
**Hash del Commit (aprox):** `Event Loop Implemented`

### ✅ Lo Logrado
1.  **Definición de Modelos (`models/`)**:
    *   Estructura clara para `Instrument`, `DataModel`, `Commission` y `Swap`.
    *   Uso de `Enums` para tipificación fuerte (`DataType`, `TimeFrame`, etc.).
    *   Docstrings completos en inglés (estilo Google).
2.  **Core Engine (`core/`)**:
    *   **Event Loop**: Implementado en `Engine`. Soporta iteración vela a vela.
    *   **Strategy Interface**: Clase abstracta `Strategy` con ciclo `init` vs `next`.
    *   **Prevención de Sesgo**: `DataModel` con acceso indexado seguro.
3.  **Documentación (`docs/`)**:
    *   `models.md`: Explicación de modelos.
    *   `engine.md`: Arquitectura del motor de eventos.
    *   `snapshot.md`: Bitácora de proyecto.
4.  **Configuración**:
    *   Entorno listo (polars, plotly, etc.).

### 🚧 En Progreso / Pendiente Inmediato
*   **OMS (Order Management System)**: Gestión de órdenes, ejecución y mantenimiento de posiciones.

### 🔮 Futuro (Roadmap Extendido)
*   **Risk Manager**: Control de riesgo pre y post-trade.
*   **Position Sizing**: Módulos dinámicos de gestión de capital (Kelly, % Risk, etc.).
*   **Métricas**: Reportes detallados y visualización (Plotly).
*   **Robustness Testing**:
    *   Monte Carlo Simulations.
    *   Monkey Tests (Entradas aleatorias para stress test).

---

## Recursos de Referencia
Existen libros clave en el directorio `docs/` para consulta continua sobre mejores prácticas cuantitativas:
*   *Algorithmic Trading: Winning Strategies via Ernest P. Chan*
*   *Building Algorithmic Trading Systems*
*   *Machine Learning for Algorithmic Trading via Stefan Jansen*

# 📸 Snapshot del Proyecto

Este archivo documenta el estado actual del desarrollo del **Strategy Factory Backtesting Engine**. Su objetivo es servir como punto de restauración conceptual en caso de necesitar retroceder o re-evaluar la dirección del proyecto.

## Estado Actual: **Fase 1 - Cimientos Completada**

**Fecha:** 2026-01-06
**Hash del Commit (aprox):** `Initial Commit`

### ✅ Lo Logrado
1.  **Definición de Modelos (`models/`)**:
    *   Estructura clara para `Instrument`, `DataModel`, `Commission` y `Swap`.
    *   Uso de `Enums` para tipificación fuerte (`DataType`, `TimeFrame`, etc.).
    *   Docstrings completos en inglés (estilo Google).
2.  **Documentación (`docs/`)**:
    *   `models.md`: Explicación detallada de todos los modelos en español.
    *   Referencias bibliográficas añadidas (Chan, Jansen).
3.  **Configuración del Entorno**:
    *   `.gitignore` configurado para Python, CSVs y Notebooks.
    *   `requirements.txt` con `polars`, `plotly`, `pandas`, etc.
4.  **README**:
    *   Descripción profesional del proyecto.
    *   Roadmap inicial definido.

### 🚧 En Progreso / Pendiente Inmediato (Fase 2 - Core Engine)
*   **Event Loop**: El corazón de la simulación.
*   **OMS (Order Management System)**: Gestión de órdenes y posiciones.

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

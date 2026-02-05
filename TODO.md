# TODO: Reestructurar Gestión de Inventario con Sidebar y Backend Python

## Información Recopilada
- Archivo existente: `index.html` con funcionalidad completa en JS (login, ventas/stock, rifas, pedidos, escáner QR, gráficos, exportación).
- Usuario quiere: Sidebar izquierdo con secciones (ventas, compras, pedidos, productos, inventario, facturación, reportes), backend Python con Flask para CRUD, mantener todo existente, agregar gráficos multicolores 3D, pantallitas para cada sección, efectos en botones/secciones.

## Plan Detallado
- **Backend Python (Flask)**: Crear `app.py` con rutas CRUD para todas las secciones, usar SQLite para persistencia, reemplazar localStorage.
- **Frontend**: Reestructurar `index.html` con sidebar izquierdo, pantallitas (modales/formularios) para cada sección, mantener funcionalidad existente, agregar efectos (hover, animaciones), gráficos 3D multicolores.
- **Integración**: Usar fetch para comunicación frontend-backend.
- **Secciones CRUD**:
  - Ventas: CRUD de transacciones de venta.
  - Compras: CRUD de compras de productos.
  - Pedidos: Ya existe, mejorar con backend.
  - Productos: CRUD de productos.
  - Inventario: Vista de stock, ajustes.
  - Facturación: Generar facturas.
  - Reportes: Gráficos y exportaciones.

## Pasos de Implementación
- [x] Crear `app.py` con Flask, rutas básicas, modelo de datos (usar SQLAlchemy o dicts simples).
- [x] Agregar rutas CRUD para productos, ventas, compras, pedidos, facturación, reportes.
- [x] Modificar `index.html`: Agregar sidebar, modales para cada sección, efectos CSS (hover, transitions).
- [x] Integrar gráficos 3D multicolores (usar Chart.js con plugins o efectos CSS).
- [ ] Migrar lógica JS a usar backend (reemplazar localStorage con fetch).
- [ ] Probar funcionalidad completa.
- [ ] Agregar efectos visuales adicionales (animaciones en botones, secciones).

## Dependencias
- Instalar Flask, SQLAlchemy (opcional), CORS para frontend.
- Mantener librerías JS existentes.

## Seguimiento
- Actualizar este TODO a medida que se completen pasos.

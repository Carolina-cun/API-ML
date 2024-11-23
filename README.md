# API REST de Mercado Libre

## Descripción
Este proyecto crea una API REST en Python usando Flask que interactúa con la API de Mercado Libre. La API replicará 5 métodos seleccionados de la API oficial de Mercado Libre.

## Endpoints
- `GET /api/items_by_category`: Obtiene ítems por categoría.
- `GET /api/search`: Busca productos por palabra clave.
- `GET /api/product_details`: Obtiene detalles de un producto.
- `GET /api/category_prices`: Muestra los precios de productos por categoría.
- `GET /api/seller_info`: Obtiene información sobre un vendedor.

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install Flask requests  

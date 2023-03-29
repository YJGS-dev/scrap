
# Scrap

API Menú de Despensa
extrae la información del menú de despensa del sitio web de Walmart México y la presenta en formato JSON.

API Extracción de Productos recibe una URL del sitio web https://www.tiendasjumbo.co/ como parámetro de entrada y extrae los productos. La información se presenta en formato JSON.


## Instalación

Para instalar y ejecutar este proyecto en su máquina local, siga los siguientes pasos:

Clone el repositorio en su máquina local.
```bash
  git clone https://github.com/YJGS-dev/scrap.git
```

Entre al directorio del proyecto

```bash
  cd scrap
```

Cree un entorno virtual de Python utilizando el siguiente comando

```bash
  python -m venv venv
```

Active el entorno virtual utilizando el siguiente comando

```bash
  source venv/bin/activate
```

Instale las dependencias necesarias utilizando el siguiente comando

```bash
  pip install -r requirements.txt
```

Inicie el servidor

```bash
  uvicorn main:app --reload
```

## Referencia de la API

#### Obtener el menú de despensa de Walmart

```http
  GET /api/walmart
```

#### Extraer productos de una URL del sitio tiendas jumbo

```http
  GET /api/tiendas_jumbo/${URL}
```

| Parametro | Tipo     | Descripción                       |
| :-------- | :------- | :-------------------------------- |
| `URL`      | `string` | **Requerido**. ejemplo https://www.tiendasjumbo.co/jugueteria |


## Uso
Después de ejecutar el proyecto, puede acceder a la documentación de la API en su navegador a través de la dirección http://localhost:8000/docs o http://localhost:8000/redoc. Desde aquí, puede ver la información de la API y probar las diferentes funciones utilizando el panel de pruebas.
## License

[MIT](https://choosealicense.com/licenses/mit/)


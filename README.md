# Procesamiento de Imágenes

## Funcionamiento de la Aplicación

Este proyecto es una aplicación Python que permite aplicar transformaciones a imágenes, como ajustar brillo y contraste. Está diseñado utilizando patrones de diseño como **Template Method**, **Decorator** y **Facade** para garantizar un código modular, flexible y fácil de mantener.

## Características

- Ajuste dinámico de **brillo** y **contraste** en imágenes.
- Procesamiento automatizado siguiendo un flujo predefinido.
- Código estructurado usando patrones de diseño.

## Instalación de Dependencias en un Entorno Virtual

Para instalar las dependencias necesarias en un entorno virtual, siga los siguientes pasos:

1. Cree un entorno virtual:
  ```bash
  python -m venv venv
  ```

2. Active el entorno virtual:
  - En Windows (cmd):
    ```bash
    .\venv\Scripts\activate
    ```
  - En Windows (Powershell): 
    ```bash
    .\venv\Scripts\Activate.ps1
    ```
  - En macOS y Linux:
    ```bash
    source venv/bin/activate
    ```

3. Instale las dependencias desde el archivo `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

4. Verifique que las dependencias se hayan instalado correctamente:
  ```bash
  pip list
  ```
5. Para desactivar el entorno virtual:
  ```bash
  deactivate
  ```

Ahora su entorno virtual está configurado y listo para usar con todas las dependencias necesarias para la aplicación de procesamiento de imágenes.

# Ejecución de la aplicación

Con el entorno virtual activato ejecutar:
```bash
python main.py
```
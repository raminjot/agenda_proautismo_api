REQUISITOS
------------

El proyecto requiere las siguientes dependencias:

 * [Python 3](https://www.python.org/downloads/)


OPCIONAL
------------

 * [MySQL](https://dev.mysql.com/downloads/installer/) - Dependencia requerida si se quiere utilizar una instancia de base de datos local.


CONFIGURACIÓN
-------------

 * Instalación **virtualenv**:

   - Instalar de manera global el paquete **virtualenv** ejecutando ```pip install virtualenv``` en una terminal.

     Verificar que la instalación fue existosa revisando que el paquete este listado al ejecutar el comando ```pip list``` en una terminal.

     NOTA: Si se presentan dificultades, abrir una terminal en modo administrador, desinstalar **virtualenv** (```pip uninstall virtualenv```) y volver a instalar.

 * Creación y uso de entorno virtual:

    - Abrir una terminal en el directorio del proyecto y ejecutar el comando ```virtualenv venv```.

    - Dentro de la misma terminal, navegar hacia la carpeta Scripts: ```cd venv/Scripts/```.

    - Dentro del directorio de Scripts, ejecutar el comando ```activate```.

 * Instalación de dependencias del proyecto:

    - Una vez en uso el entorno virtual en la terminal, navegar hasta la carpeta raíz del proyecto ```cd ../..```.

    - Ejecutar el comando ```pip install -r requirements.txt```.

 * Inicializar el servidor:

    - Copiar el archivo **.env.sample** y pegar en el mismo directorio con el nombre de **.env**.

    - Configurar las variables de entorno del archivo **.env**.

    - En la terminal, estando en la raíz del proyecto mientras esta en uso el entorno virtual, ejecutar el comando ```python main.py```.

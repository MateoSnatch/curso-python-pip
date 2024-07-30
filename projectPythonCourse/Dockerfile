#version instalada en el entorno
FROM python:3.10 

#carpeta que alojará todo el entorno
WORKDIR /app
#se lleva una copia de las dependencias a la carpeta con el mismo nombre
COPY requirements.txt /app/requirements.txt
#se corre la instalacion de las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#se hace una copia de todo el archivo actual (projectPythonCourse) y se aloja en app
COPY . /app/

CMD bash -c "while true; do sleep 1; done"
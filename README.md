# Python Telegram Bot: Toggl Alarm!

Bot para Telegram que coneca con tu cuenta de Toggl y te envía una recompensa o castigo en función de si el día anterior has imputado las horas en Toogl.

Es de uso personal ya que depende de la API TOKEN de Toggl del usuario

Más información en https://fenomenomutante.com/8

<!-- TOC -->

- [Python Telegram Bot: Toggl Alarm!](#python-telegram-bot-toggl-alarm)
    - [Requerimientos previos](#requerimientos-previos)
        - [Telegram Token](#telegram-token)
        - [Toggl API Key](#toggl-api-key)
    - [Instalación](#instalación)
        - [Dependencias](#dependencias)
        - [Variables de entorno](#variables-de-entorno)
        - [Ejecución](#ejecución)
    - [Modo de uso](#modo-de-uso)
    - [TODO](#todo)

<!-- /TOC -->

## Requerimientos previos

### Telegram Token
Debes conseguir un token para el bot que vayas a enganchar con esta aplicación.

Sigue las instrucciones del "padre de los bots" en Telegram, utilizando el bot @BotFather

Más info en [telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

### Toggl API Key

La API Key de Toggl te da acceso a los informes de registros del usuario. 

Más info en https://github.com/toggl/toggl_api_docs

## Instalación

Necesitamos un sistema conectado a internet y el repositorio descargado. El programa funciona con python 3

### Dependencias

Primero instalamos las dependencias ejecutando este comando del gestor de paquetes `pip`

```bash
pip install -r requirements.txt
```

### Variables de entorno

Copiamos el fichero .env.example y lo convertimos en .env

```bash
cp .env.example .env
```

Sustituimos los valores de los token y API key para el bot de telegram y la cuenta de toggl

### Ejecución

```bash
python main.py
```

## Modo de uso

Abrimos una conversación con el bot de telegram.

Tenemos estos comandos disponibles

- /set arrancará la alarma. Se ejecutará cada día a esta misma hora
- /unset detiene la alarma
- /help Muestra la ayuda

El bot se conectará a toggl y devolverá un emoticono de 💩 si no se han imputado las horas en el día anterior y un emoticono 💃🏻 si se ha ejecutado correctamente.

## TODO
- [x] Tarea ejecutada diariamente
- [ ] Log optativo
- [ ] Elegir la hora de la alarma
- [ ] Elegir los días para recibir la alarma
- [ ] Acumulado de días o método Jerry Seinfeld


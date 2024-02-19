# ElBechuanoBot ⚙️

La idea principal de este proyecto es crear un Bot simple para servidores de Discord con funcionalidades básicas.

### Prerequisitos 📋

Para poder trabajar con ElBechuanoBot, debemos tener en cuenta los siguientes recursos/herramientas:

* Python
* Docker
* Fly.io

### Requisitos de instalación 🔧

Tras clonar el repositorio, en el directorio 'ElbechuanoBot\FFmpeg\bin' deben haber tres ejecutables .exe los cuales deberán añadirse manualmente, estos som **ffmpeg.exe**, **ffplay.exe** y **ffprobe.exe**.

En caso de no tenerlos descargados en nuestro equipo local, podemos descargarlos desde la web oficial de [ffmpeg](https://ffmpeg.org/download.html). También, podemos clonar su repositorio.

git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
```

#### Uso 🚀

Actualmente, ElBechuanoBot tiene un total de cuatro funcionalidades, que son las siguienters:

1ro. Muestra un mensaje aleatorio tomado del canal que definamos del servidor de Discord.

!frases
```

2do. Muestra un mensaje que definamos previamente.

!pxg
```

3ro. Reproduce música en un canal de voz mediante enlaces de YouTube

!play
```

4to. Detiene la reproducción de música.

!stop
```
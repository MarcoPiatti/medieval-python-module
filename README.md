# Qué cambiar de este template?
- El Puerto utilizado en la app y mencionado en los archivos de docker, que por defecto es 8080 pero puede y debería ser cualquier otro.
- Nombre del módulo referenciado en docker y docker compose.

# Cómo ejecutar la aplicación
Si bien esta aplicación esta diseñada para levantarse junto al servidor de medieval, es posible iniciarla de forma individual.

Localmente: 

```bash
flask run --host=0.0.0.0 --port=8080
```

Localmente a través de docker:

```bash
#buildear la imagen
docker build . -t gibio/medieval:nombre-del-modulo-X.Y.Z

#ejecutarla
docker run gibio/medieval:nombre-del-modulo-X.Y.Z
```

# Release de nueva versión
Ante cambios en la aplicación, es recomendado generar un nuevo tag en el repositorio con la nueva versión X.Y.Z. Luego se buildea y se sube la imagen al repositorio de docker.
```bash
#buildear la imagen
docker build . -t gibio/medieval:nombre-del-modulo-X.Y.Z

#subirla
docker push gibio/medieval:nombre-del-modulo-X.Y.Z
```

Luego desde el servidor de gibio.
```bash
#descargar la nueva imagen
docker pull gibio/medieval:nombre-del-modulo-X.Y.Z
```

Una vez agregada la imagen al repositorio de docker, es posible agregarla como un servicio al docker-compose de medieval, para que inicialice con los otros servicios de la aplicación.

Tambien puede ser levantado como servicio dentro de ubuntu de forma independiente a través de systemd.

# Integración con medieval
Con una cuenta administradora, navegar a la pestaña de validadores externos, click en crear uno nuevo y copiar/pegar la url donde esté hosteado Para agregar el módulo a medieval.

Considerando las distintas formas de desplegar la solución, la url del nuevo módulo puede variar. En caso de tener medieval encendido a través de docker compose, habrá una red medieval-default creada, la cual ya está agregada al docker compose de este repositorio. Pero esto podría cambiar en un futuro.

Bajo esa consideración, la url para acceder a este módulo desde medieval debería ser:
```
http://medieval-nombre-del-modulo-1:8080
```

Si la url es correcta, medieval establece comunicación con el módulo y obtiene los datos necesarios para luego poder usarlo.
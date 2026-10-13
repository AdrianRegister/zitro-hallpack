## Migración de la aplicación CLI a una aplicación WEB

### Cambios estructurales

- Se necesitaría un framework web para escribir un API REST. Para este caso de uso, optaría por Flask. No hace falta toda la funcionalidad de Django, y tampoco una interfaz compleja. Por lo tanto, las plantillas HTML que Flask ofrece serán suficientes.

### API

- Se expondría rutas que corresponden con los requisitos de la tarea, por ejemplo `/plan`
- Los argumentos se pasarían como query string parameters, por ejemplo `/plan?p1=param1,p2=param2`
- Dado que el índice real está remoto, se necesitarán integraciones con este sistema.

### Preocupaciones

- La seguridad. Habrá que asegurarse de que la aplicación sólo se pueda acceder desde el VPN de la empresa. Encima, quizás sólo por usuarios específicos de la empresa, lo que implicaría implementar autenticación/autorización.

- Se necesita una capa robusta de cómo gestionar llamadas perdidas al sistema remote del índice real. Dado que puede tardar minutos, hay que implementar timeout, max_retries, y quizás un exponential backoff.

- Se necesita una solución robusta de almacenamiento, para asegurar a largo plazo la fiabilidad de almacenar los archivos `tar.gz`

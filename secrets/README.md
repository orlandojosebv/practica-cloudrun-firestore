# Instrucciones para agregar tu cuenta de servicio

En este directorio debes pegar el contenido de la **cuenta de servicio** (archivo `.json`) que generes en Google Cloud Platform (GCP).

---

A continuación tienes el flujo paso a paso, totalmente desde la consola web de GCP, para crear una cuenta de servicio y otorgarle permisos sobre todos los servicios de tu proyecto:

1. **Accede a la consola de Google Cloud**
    - Ve a [https://console.cloud.google.com/](https://console.cloud.google.com/)
    - Asegúrate de tener seleccionado el proyecto correcto en el selector de la barra superior.

2. **Ir a “IAM y administración” → “Cuentas de servicio”**
    - En el menú de la izquierda, despliega *IAM y administración*.
    - Haz clic en *Cuentas de servicio*.

3. **Crear una nueva cuenta de servicio**
    - Pulsa el botón **+ CREAR CUENTA DE SERVICIO** en la parte superior.
    - Completa los campos:
      - *Nombre de la cuenta*: p. ej. `lab-svc`
      - *ID de la cuenta*: se autogenera, pero puedes ajustarlo.
      - *Descripción* (opcional): describe su propósito.

4. **Otorgar permisos (roles) a la cuenta de servicio**
    - En la sección *Grant this service account access to project* (Conceder acceso al proyecto):
      - Haz clic en *Seleccionar un rol*.
      - En el desplegable, ve a *Project* → *Owner*.
      - *Owner* le da acceso completo a todos los recursos y APIs del proyecto.
      - Si prefieres un permiso algo más restringido, podrías usar *Editor*, pero para “todos los servicios” el rol *Owner* es el adecuado.

5. **Omitir (o añadir) permisos de usuarios finales**
    - La siguiente sección pregunta si quieres conceder a usuarios específicos la capacidad de actuar con esta cuenta de servicio.
    - Puedes omitirla si no necesitas delegar este acceso directamente.

6. **Finalizar la creación**
    - Haz clic en *Crear y continuar* o directamente en *Listo* si no agregaste delegados.
    - Verás tu nueva cuenta de servicio listada.

7. **(Opcional) Generar y descargar una clave JSON**
    - En la lista de cuentas de servicio, haz clic sobre la que acabas de crear.
    - Ve a la pestaña *Claves*.
    - Pulsa *Agregar clave* → *Crear nueva clave*.
    - Selecciona *JSON* y haz clic en *Crear*.
    - Se descargará el archivo `*.json` con las credenciales; guárdalo en un lugar seguro.

---
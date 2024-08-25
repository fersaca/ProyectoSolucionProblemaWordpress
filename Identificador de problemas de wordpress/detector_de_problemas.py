import re

# Datos de problemas conocidos
wordpress_problems = [
    "unable to create directory",
    "wc ajax get refreshed fragments",
    "error 403",
    "error 404",
    "error 500",   
    "pantalla blanca",
    "error base de datos", 
    "error actualizar",   
    "connection timed out",  
    "ERR_TOO_MANY_REDIRECTS",  
    "allowed memory size", 
    "unexpected",
    "object cache",
    "hidewpadmin",
    "smtp",
    "phpversion",
    "alerta de google",
    "instalar wordpress",
    "instalar plugin",
    "instalar tema",
    "clave wordpress",
    "error guru",
    "cambio de dominio",
]

# Datos de soluciones a los problemas
wordpress_solutions = [
    "Si observas el error: Unable to create directory guia con solucion paso a paso: <a href='https://help.wnpower.com/hc/es/articles/360046757771-Error-Unable-to-create-directory-Is-its-parent-directory-writable-by-the-server-de-WordPress'>Click Aquí</a>",
    "Puedes solucionar o mejorar Woocommerce solucionando el exceso de procesos del wx ajax refreshes de la siguiente forma: <a href='https://www.wnpower.com/blog/reparar-lentitud-woocommerce-wc-ajaxget_refreshed_fragments/'>Click Aquí</a>",
    "Los problemas de error 403 son muy comunes y muy genericos te dejo guia con solucion paso a paso: <a href='https://www.wnpower.com/blog/que-es-error-403-forbidden-como-solucionarlo/'>Click Aquí</a>",
    "Los problemas de error 404 son muy comunes y muy genericos te dejo guia con solucion paso a paso: <a href='https://www.wnpower.com/blog/error-404-que-es-arreglar/'>Click Aquí</a>",
    "El error 500 es un error interno del servidor. Puede deberse a múltiples causas, como un plugin o tema incompatible, un archivo .htaccess corrupto, o problemas en la configuracion php. Se recomienda realizar un chequeo con nuestra herramienta WordPress Doctor: <a href='https://help.wnpower.com/hc/es/articles/360053724751-C%C3%B3mo-volver-a-una-versi%C3%B3n-de-WordPress-anterior-sin-reinstalar'>Click Aquí</a> en caso de visualizar algun error diferente, indicarmelo, quedo atento :)",
    "Si no puedes acceder a su sitio debido a una pantalla blanca sin mostrar nada, debes realizar lo siguiente -> <a href='https://www.wnpower.com/blog/solucionar-pantalla-blanca-wordpress/' target='_blank'> Soluciona Pantalla Blanca </a",    
    "El error de conexión a la base de datos puede ser causado por credenciales incorrectas en la configuracion del wp-config.php, asi como tambien puede ser por errores temporales, ya sea mediante un proceso de instalacion o saturacion de los procesos de la base de datos lo cual colgo al tratar de sumar otro proceso, por lo cual se recomienda mejorar el rendimiento de este procesos internos de wordpress, le dejo la siguiente guia paso a paso para realizar esto: <a href='https://www.wnpower.com/blog/query-monitor-plugin-wordpress-rendimiento/'>Query Monitor</a> Por otro lado si el problema es de configuracion del wp-config.php tras mudar tu sitio web, entonces solo debes modificar los datos para que conecte a la base de datos de su cPanel",     
    "Si al tratar de actualizar algun apartado / plugin o tema, esto puede suceder debido a diferentes errores internos, causado en su mayoria de casos debido a plugins, se recomienda desactivar todos los plugins o actualizarlos asi como cambiar el tema esto con nuestra herramienta -> <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower' target='_blank'> Wordpress Doctor </a>",  
    "El error de tiempo de espera de conexión aparece cuando su sitio web intenta hacer más de lo que su servidor puede administrar, por lo cual se recomienda realizar mejoras de rendimiento como, aumentar los valores de -> <a href='https://help.wnpower.com/hc/es/articles/360035683812-C%C3%B3mo-modificar-el-php-ini-de-tu-Hosting-cPanel' target='_blank'> Valores PHP.INI </a> Desactivar todos los plugins para identificar si alguno en particular es el causante -> <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower' target='_blank'> Wordpress Doctor </a>",  
    "El error es debido a una configuracion dentro del sitio web que esta causando multiples redireccionamientos, esto depende de cual fue su ultima modificacion si fuel algun plugin se recomienda desactivar en caso de haber configrado cloudflare debe realizar lo siguiente -> <a href='https://help.wnpower.com/hc/es/articles/360035691452-Error-ERR-TOO-MANY-REDIRECTS-si-est%C3%A1s-usando-CloudFlare-en-tu-Hosting' target='_blank'> CloudFlare error err_to_many_redirects </a> Si el problema fue causado o es causado por un plugin se recomienda desactivar todos directamente con -> <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower' target='_blank'> Wordpress Doctor </a>",  
    "Un error de tamaño de memoria permitido agotado significa que su instalación de WordPress no tiene suficiente memoria para lograr lo que desea. Puedes probar los siguientes pasos: aumento del valor de memory limit de wordpress desde el archivo wp-config adicionar en cualquier apartado ->' define( 'WP_MEMORY_LIMIT', '512M' ); 'aumentar 512M segun el plan que poseas, tambien se debera aumentar los valores de -> <a href='https://help.wnpower.com/hc/es/articles/360035683812-C%C3%B3mo-modificar-el-php-ini-de-tu-Hosting-cPanel' target='_blank'> Valores PHP.INI </a> ",
    "Si recibe un error que dice 'error de análisis: inesperado/unexpected', generalmente significa que olvidó incluir un carácter. Los más comunes son: '=' inesperado : ha olvidado incluir $ al hacer referencia a una variable.. Inesperado ')' : has olvidado incluir el corchete de apertura (... Inesperado '(' : has olvidado incluir el corchete de cierre)... T_STRING inesperado : ha olvidado una comilla o un punto y coma al final de la línea anterior... T_ELSE inesperado : tiene una declaración else sin declaración if de apertura; Si el error persiste se recomienda desactivar todos los plugins para identificar el causante -> <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower' target='_blank'> Wordpress Doctor </a>",  
    "Si deseas configurar el cache object dentro de tu wordpress podras realizar lo siguiente -> <a href='https://help.wnpower.com/hc/es/articles/13061198485773-Mensaje-Deber%C3%ADas-utilizar-una-cach%C3%A9-de-objetos-persistente-en-WordPress-dentro-de-Salud-del-sitio' target='_blank'> cache de objetos persistente en WordPress </a>",
    "Si deseas ocultar el acceso o login de tu administrador wordpres /wp-admin lo puedes realizar de la siguiente forma: <a href='https://www.wnpower.com/blog/como-cambiar-proteger-url-wordpress-wp-admin/'>Paso a Paso Click Aquí</a>",
    "Los correos de tu WordPress ¿no están saliendo? o no le llegan a los destinatario entonces debes realizar el siguiente paso a paso para asegurar el correcto funcionamiento en la salida de mails: <a href='https://www.wnpower.com/blog/wordpress-no-manda-correos-emails-solucion/' target='_blank'>Corrige de la siguiente forma</a> si esto ya lo hiciste y sigue sin funcionar puede ser que estes adicionando un valor erroneo o la clave del correo que usas para el smtp este erroneo, ten en cuenta adicionar es un correo que hayas creado dentro de tu hosting para asegurar la salida de mail (se recomienda utilizar los datos exactos de la guia, siendo un dato erroneo la causa del problema)",
    "Mantener actualizada la versión de PHP es crucial para el rendimiento y seguridad de tu sitio. Si necesitas actualizar o tienes problemas con la compatibilidad, puedes modificar la version php de la siguiente forma: <a href='https://help.wnpower.com/hc/es/articles/360020782451-Cambiar-la-versi%C3%B3n-de-PHP'>Click Aquí</a>",
    "Esto es un filtro de seguridad creado por los propios navegfadores para su sitio web siendo u ncaso escalado con dificultades de solucion, recomiendo seguir los siguiente pasos tal cual la guia: <a href='https://help.wnpower.com/hc/es/articles/360035869731-C%C3%B3mo-arreglar-la-alerta-Este-sitio-web-contiene-software-malicioso-'>Solucionar Alerta en rojo de google</a>",
    "En este caso se debe seguir los siguiente pasos tal cual la guia: <a href='https://help.wnpower.com/hc/es/articles/360020779371-Instala-WordPress-al-instante'> Instala Wordpress </a>",
    "En este caso se debe seguir los siguiente pasos tal cual la guia: <a href='https://help.wnpower.com/hc/es/articles/360025734891-C%C3%B3mo-instalar-un-plugin-en-tu-WordPress'>Instala plugin </a>",
    "En este caso se debe seguir los siguiente pasos tal cual la guia: <a href='https://www.wnpower.com/blog/cambiar-theme-plantilla-wordpress/'>Instala Tema </a>",
    "Si no puedes acceder con tu usuario wordpress, puedes modificar la clave o generar un nuevo usuario con nuestra herramienta -> : <a href='https://help.wnpower.com/hc/es/articles/360035361432-Tour-por-la-herramienta-WordPress-Admin-de-WNPower' target='_blank'> Wordpress Admin </a>, si el problema persiste aun creando un nuevo usuario capaz y requieres checar tu wordpress con nuestra herramienta: <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower' target='_blank'> Wordpress Doctor </a> ",    
    "Si al intentar mudar tu sitio web con Guru Migrator y te devovio un error y no finalizo el proceso puede deberse a vareos problemas internos o del servidor de origen o del wordpress, antes de iniciar el mudado desactiva todos los plugins de wordpress asi como cambia el tema a uno por defecto luego inicia el proceso nuevamente, en caso de persistir puede ser debido a un error del servidor de origen se debe consultar con ellos si hay una regla de firewall que evite el mudado", 
    "Los cambios de dominio principal a nivel cPanel se realiza del lado de soporte, se debe solicitar mediante ticket teniendo en cuenta todo lo explicado enla siguiente guia: <a href='https://help.wnpower.com/hc/es/articles/360016076272-Cambiar-el-dominio-principal-de-una-cuenta-de-hosting' target='_blank'> Cambio de dominio principal </a>",
]


#detect_known_problems se encarga de detectar en el texto del usuario diferentes codigos de error, como fatal error, warning y mas para brindar solucion
def detect_known_problems(user_input):
    

    # Detección de errores fatales en WordPress
    match = re.search(r'fatal error : (.+?) in (.+?/([^/]+)) on line (\d+)', user_input, re.IGNORECASE)
    
    # Manejo de los errores Fatales en wordpress
    if match:
        error_message, full_path, error_file, line_number = match.groups()
        # Verificar directorio específico en error
        if "/wp-content/plugins/" in full_path:
            plugin_name = re.search(r'/wp-content/plugins/([^/]+)', full_path).group(1)
            return f"El error lo está causando el plugin {plugin_name} que presenta un fatal error: {error_message} en el archivo {error_file} en la línea de código #{line_number} se recomienda desactivar o reinstalar, puedes utilizar nuestra herramienta <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower'>Wordpres Doctor</a>"
        elif "/wp-content/themes/" in full_path:
            theme_name = re.search(r'/wp-content/themes/([^/]+)', full_path).group(1)
            return f"El error lo está causando el tema {theme_name} que presenta un fatal error: {error_message} en el archivo {error_file} en la línea de código #{line_number} se recomienda desactivar o reinstalar, puedes utilizar nuestra herramienta <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower'>Wordpres Doctor</a>"
        elif "/wp-includes/" in full_path:
            return f"El error se origina en un archivo core de WordPress, error exacto: {error_message} en el archivo {error_file} en la línea de código #{line_number}. Es posible que una actualización o modificación reciente por plugin/tema/configuracion interna de wordpress haya causado este problema. Puedes utilizar nuestra herramienta <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower'>Wordpres Doctor</a> para diagnosticar y corregir problemas, en caso de no poder te recomendaria restaurar una copia de seguridad con nuestra herramienta <a href='https://help.wnpower.com/hc/es/search?utf8=%E2%9C%93&query=jetbackup+5'>Jetbackup5</a>"
        elif "/wp-admin/" in full_path:
            return f"El error se origina en el área administrativa de WordPress, error exacto: {error_message} en el archivo {error_file} en la línea de código #{line_number}. Esto puede ser causado por incompatibilidades con la versión actual de WordPress, un archivo afectado o infectado o por plugins conflictivos. Te recomendamos desactivar recientes plugins o temas, eliminar el archivo o verificar compatibilidad, puedes usar nuestra herramienta <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower'>Wordpres Doctor</a> para diagnosticar y corregir problemas."
        # Aquí puedes agregar otros directorios y sus mensajes respectivos...
     
    # Detección de Cannot modify header information SEND BY
    header_error_pattern = (
        r'(warning\s*:\s*|php\s+warning\s*:\s*)?can\s+not\s+modify\s+header\s+information\s*[-–—]\s*headers\s+already\s+sent\s*by\s*\(\s*output\s+started\s+at\s+([^\s]+\.php):\s*(\d+)\s*\)\s*in\s+([^\s]+\.php)\s+on\s+line\s+(\d+)')
    # Detección de error "Cannot modify header information" en el texto del usuario
    match2 = re.search(header_error_pattern, user_input, re.IGNORECASE)    
    # Manejo de los Cannot modify header information en wordpress  
    if match2:
        warning, output_start_file, output_start_line, error_file, error_line = match2.groups()
        msg = "Se ha detectado un problema en la configuración o en un archivo PHP. "
        if output_start_file and output_start_line:
            msg += f"El problema parece haber comenzado en {output_start_file} en la línea {output_start_line}. "
        if error_file and error_line:
            msg += f"El error 'Cannot modify header information' se detectó en {error_file} en la línea {error_line}. "
        #El mensaje personalizado para el usuario indicando los puntos o archivos detectados en el texto del usuario.
        msg += ("Este tipo de error suele ser causado por espacios o caracteres adicionales antes o después de las etiquetas PHP. "
                "Revisa y corrige los archivos mencionados. Si el problema persiste, reinstalar la integracion de wordpress con nuestra herramienta <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower' target='_blank'> Wordpress Doctor </a> o considera restaurar una copia de seguridad con nuestra herramienta <a href='https://help.wnpower.com/hc/es/search?utf8=%E2%9C%93&query=jetbackup+5' target='_blank'> Jetbackup 5 </a>")
        return msg
        
    # Detección de Cannot modify header information SEND IN   
    header_error_pattern2 = (
    r'(warning\s*:\s*|php\s+warning\s*:\s*)?can\s+not\s+modify\s+header\s+information\s*[-–—]\s*headers\s+already\s+sent\s*in\s+([^\s]+\.php)\s+on\s+line\s+(\d+)'
    )

    match3 = re.search(header_error_pattern2, user_input, re.IGNORECASE)

    if match3:
        warning, error_file, error_line = match3.groups()

        msg = "Se ha detectado un problema al enviar una cabecera HTTP después de que ya se ha iniciado el envío de contenido al navegador"
        if error_file and error_line:
            msg += f"El error se detectó en {error_file} en la línea {error_line}. "
        msg += ("ten en cuenta que los errores cannot modify header en WordPress, son problemas comunes que ocurre elatoriamente, por culpa de algun plugin o tema - Vamos a explorar las causas más comunes de este error: espacios en Blanco o Caracteres antes de <?php, Conflictos con Plugins o Temas."
                "Revisa y corrige los archivos mencionados. Si el problema persiste, reinstalar la integracion de wordpress con nuestra herramienta <a href='https://help.wnpower.com/hc/es/articles/360035361012-Tour-por-la-herramienta-WordPress-Doctor-de-WNPower' target='_blank'> Wordpress Doctor </a> o considera restaurar una copia de seguridad con nuestra herramienta <a href='https://help.wnpower.com/hc/es/search?utf8=%E2%9C%93&query=jetbackup+5' target='_blank'> Jetbackup 5 </a>")
        return msg
        
   
    # Diccionario que mapea frases clave (o palabras clave) que pueden estar presentes en la consulta del usuario
    # a los problemas conocidos de WordPress que están almacenados en la lista `wordpress_problems`.
    key_phrases = {
        "unable to create directory": "unable to create directory",
        "wc-ajax=get_refreshed_fragments": "wc ajax get refreshed fragments",
        "wc ajax get refreshed fragments": "wc ajax get refreshed fragments",
        "403": "error 403", 
        "404": "error 404", 
        "500": "error 500",
        "internal server error": "error 500",     
        "pantalla blanca": "pantalla blanca", "queda en blanco": "pantalla blanca", "pantalla en blanco": "pantalla blanca",  "no muestra nada": "pantalla blanca",        
        "error al establecer": "error base de datos", "con la base de datos": "error base de datos", "error establishing database connection": "error base de datos",
        "establishing database connection": "error base de datos",  
        "no puedo actualizar": "error actualizar", "no deja actualizar": "error actualizar", "valid json response": "error actualizar", "the response is not a valid JSON response": "error actualizar",   
        "updating failed": "error actualizar",   
        "connection timed out": "connection timed out", "the connection has timed out": "connection timed out",   "err_connection_timed_out": "connection timed out",
        "ERR_CONNECTION_TIMED_OUT": "connection timed out",  
        "ERR_TOO_MANY_REDIRECTS": "ERR_TOO_MANY_REDIRECTS", "ERR TOO MANY REDIRECTS": "ERR_TOO_MANY_REDIRECTS", "err too many redirects": "ERR_TOO_MANY_REDIRECTS",   
        "err_too_many_redirects": "ERR_TOO_MANY_REDIRECTS", "too many redirects": "ERR_TOO_MANY_REDIRECTS",
        "allowed memory size": "allowed memory size", "tamaño de memoria permitido": "allowed memory size", "tamano de memoria permitido": "allowed memory size",  "out of memory": "allowed memory size",
        "unexpected": "unexpected", "syntax error": "unexpected",  
        "object cache": "object cache", "cache de objetos persistente": "object cache", "cache de objetos": "object cache", "cache object": "object cache",
        "ocultar wp-admin": "hidewpadmin", "ocultar wp admin": "hidewpadmin", "cambiar wp-admin": "hidewpadmin", "cambiar wp admin": "hidewpadmin", "modificar wp-admin": "hidewpadmin", "ocultar login": "hidewpadmin",
        "correos no salen": "smtp", "los mails no llegan": "smtp", "emails no salen": "smtp", "correos no llegan": "smtp",
        "los correos no se reciben": "smtp", "los mails no se estan recibiendo": "smtp", "no se esta recibiendo correos": "smtp", "no salen los mails": "smtp",
        "mis mails no se reciben": "smtp", "fomulario no envia": "smtp", "fomulario no funciona": "smtp", "formulario no salen": "smtp", "no se envian los correos": "smtp",
        "no se envia el correo": "smtp", "wp mail smtp": "smtp", "envio mail": "smtp", "mandar mail": "smtp","envio mails": "smtp", "mandar mails": "smtp", "envio correo": "smtp", "mandar correos": "smtp", "smtp": "smtp",
        "enviar mails": "smtp", "enviar mail": "smtp", "enviar correo": "smtp", "enviar correos": "smtp",
        "version php": "phpversion", "php version": "phpversion","cambiar php": "phpversion","cambiar el php": "phpversion","modificar el php": "phpversion","modificar php": "phpversion",
        "este sitio web contiene software malicioso": "alerta de google", "contiene software malicioso": "alerta de google", 
        "visitar este sitio puede dañar su computadora": "alerta de google", "visitar este sitio puede danar su computadora": "alerta de google", 
        "el sitio al que vas a acceder contiene programas dañinos": "alerta de google", "el sitio al que vas a acceder contiene programas daninos": "alerta de google",
        "instalar wordpress ": "instalar wordpress","instalo wordpress ": "instalar wordpress","instalar wordpres ": "instalar wordpress","instalo wordpres ": "instalar wordpress","instalacion wordpres ": "instalar wordpress",
        "instalar plugin": "instalar plugin", "instalar plugins": "instalar plugin", "instalo plugins": "instalar plugin", "instalo plugin": "instalar plugin", "instalacion de un plugin": "instalar plugin",
        "instalar tema": "instalar tema", "instalar tema": "instalar tema", "instalo tema": "instalar tema", "instalo tema": "instalar tema", "instalacion de un tema": "instalar tema",
        "no puedo entrar a wordpress": "clave wordpress", "recuperar clave": "clave wordpress", "recuperar contraseña": "clave wordpress", "recuperar contrasena": "clave wordpress", "cambiar clave": "clave wordpress", "modificar clave wordpress": "clave wordpress", "error : la contraseña": "clave wordpress", "error : la contrasena": "clave wordpress",
        "some error has occurred at our end while migrating your site": "error guru",  "error has occurred at our end while": "error guru",
        "cambiar dominio": "cambio de dominio", "cambiar dominios": "cambio de dominio", "modificar el dominio": "cambio de dominio", "modificar dominio": "cambio de dominio", "cambiar la url": "cambio de dominio",        
    }

    # Iteramos sobre el diccionario `key_phrases`
    for key, phrase in key_phrases.items():
        # Verificamos si alguna de las palabras clave está presente en el texto introducido por el usuario.
        if key in user_input:
            # Si encontramos una coincidencia, buscamos el índice de esa frase en la lista `wordpress_problems`
            # para luego obtener la solución correspondiente desde `wordpress_solutions`.
            idx = wordpress_problems.index(phrase)
            return wordpress_solutions[idx]
            
    # Si no se detecta ningún problema conocido, la función devuelve None.
    return None

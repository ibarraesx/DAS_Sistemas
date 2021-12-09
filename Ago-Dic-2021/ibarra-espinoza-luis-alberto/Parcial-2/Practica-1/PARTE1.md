### Parte 1

  * ¿Qué patrón es más fácil de desarrollar (Monolítica vs. Microservicios), y por qué?
        Yo pienso que la arquitectura monolítica a pesar de ser mas anticudada es más facil de desarrollar,
        pero no por mucho. Una de las principales ventajas de la arquitectura Monolítica es que al ser
        un solo codigo, los erroes saltán de inmediato, y se pueden corregir en ese mismo momento.
        Mientras que en la de microserivcios tendríamos que esperar a conectar todos nuestros trozos de codigo
        para identificar alguna falla entre los modulos.


  * ¿En qué consiste el patrón de arquitectura monolítica?
        La arquitectura monolitica nos propone que la capa de interfaz de usuario y la capa de acceso de datos
        esten conmbinadas en un mismo programa y sobre una misma plataforma. Una aplicación monolítica es autónoma, e independiente de otras aplicaciones. La filosofía de diseño es que la aplicación es responsable no sólo de una única tarea, si no que es capaz de realizar todos los pasos o tareas necesarias para completar una determinada función.


  * ¿Cuáles son las principales desventajas de una arquitectura monolítica?
        Que no permite la creacion de modulos, por lo que la hace mas rigida y entorpece la actualización o modernización de la misma.
        La aplicacion tiene que ser totalmente desarollada en un solo lenguaje de programacion.


  * ¿Qué problemas presenta un monolito al que queremos agregar nueva funcionalidad?
        Que al ser un solo bloque de codigo es más complicado modificar una parte en especifico. 


  * ¿Qué sucede si falla una aplicación monolítica?
        Al ser un solo codigo al fallar una parte del mismo, toda la aplicacion dejaria de funcionar.


  * ¿En qué consiste el patrón de arquitectura basada en microservicios?
        La aquitectura de microservicios se caracteriza porque las aplicaciones del lado del backend
        estan dividades en distintas partes, a esto se le llama un microservicio, cada uno de estos
        microservicios hacen una funcion en particular.


  * ¿Qué sucede si aumenta la carga en un servicio de la arquitectura basada en microservicios?
        Una de las ventajas de esta arquitectura es que si un servicio deja de funcionar, al ser independiente del resto de la aplicacion
        los demas servicios pueden continuar operando sin problemas a menos que dependan directamente de ese servicio.


  * ¿Qué es un ambiente basado en contenedores?
        Los contenedores automatiza la implementación, la gestión, la escalabilidad y la conexión en red de los contenedores.
        Se puede aplicar en cualquier entorno donde ejecute contenedores y le permite implementar la misma aplicación en diferentes entornos sin necesidad de volver a diseñarla. Además, con los microservicios organizados en contenedores, es más fácil coordinar los servicios, incluidos el almacenamiento, la conexión de red y la seguridad. 


  * Si utilizaramos una arquitectura basada en microservicios, ¿seríamos dependientes a algún lenguaje/tecnología en específico o no?, ¿y por qué?
        No, cada servicio puede ser desarrollado en un lenguaje de programacion distinto. Ya que los microservicios no se caracterizan
        por la tecnologia que utilizan sino por el servcio que brindan, es decir la entrada y salida de información.


  * ¿De qué diferentes maneras se pueden comunicar los servicios en una arquitectura basada en microservicios?
        De manera directa en la que un servicio depende de otro. O indirecta donde los servicios se comunican atraves de un bus de eventos.


  * ¿Los microservicios pueden ser distribuidos? ¿Por qué?
        Asi es, al ser independientes se pueden distrubuir entre distos


  * ¿Cuáles son los principales desafios de una arquitectura basada en microservicios?
        Que en esta arquitectura vamos a tener que desarrollar, testear y desplegar cada parte por separado,
        lo cual nos terminara consumiendo mucho mas tiempo. Ademas que la velocidad con la que se comunican estos servicios
        van a depender de la red, asi mismo la seguridad de la misma.


  * ¿Cómo garantizamos la disponibilidad de un servicio en la arquitectura basada en microservicios?
        A traves de la replica de muliples de sus servicios.

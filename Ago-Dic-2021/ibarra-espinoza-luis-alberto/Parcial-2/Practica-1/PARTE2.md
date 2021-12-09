### Parte 2

  * ¿Qué lenguaje de programación utiliza el equipo de Netflix?
        JavaWeb


  * ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
        Que esta estaba alojada en un hardware al que llamaban "store database" y 
        cuando este hardware fallaba, todo el servicio de netflix se caía.



  * ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
        Que cuando al ser una arquitectura monolitica, todo el equipo trabajaba sobre el mismo codigo,
        cuando se introducian cambios y estos cambios generaban un fallo, era muy complicado identificar donde se
        estaba produciendo este error.


  * ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
        Martin Fowler


  * ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
        -Separacion de concerns.
        -Escalabilidad.
        -Virtualizacion y elasticidad.


  * ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
        El cuerpo humano, y sus organos.


  * Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
        -ELB
        -Zuul
        -NCCP


  * ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
        -Dependencia
        -Escabilidad
        -Cambios


  * ¿Qué es el falló en cascada?
        Cuando un servicio falla y no tu aplicación no esta bien preparada para defenderse de ese servicio caido,
        por lo que empiezan a caer más servicios a patir de ese error inicial, lo cual puede tumbar por completo
        la aplicacion.


  * ¿Qué es Hystrix?
        Es una libreria implementada por netflix la cual ayuda a evitar los fallos en cascada.


  * ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
        Describio a un hookworm, y como te puede hacer sentir debil, más aun si son muchos de ellos.


  * ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
        Con Cassandra, que es un sistema de código abierto distribuido de gestión de base de datos diseñado para manejar grandes cantidades de datos a través de muchos servidores de conveniencia, proporcionando alta disponibilidad sin ningún punto único de fallo.


  * ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
        Netflix implemento una estraregia de multi-region con tres regiones AWS, asi si uno falla otro
        puede continuar las operaciones con normalidad.


  * ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
        -Stateles services
        -Stateful services
        -Hybrid services


  * ¿De qué manera se describe un "_stateless service_" en el video?
        -No es cache o una base de datos
        -Metadatos frecuentemente accesados
        -Sin afinidad de instancia
        -La perdida de un nodo no es un evento


  * ¿Qué es Chaos Monkey?
        Una herramienta de fallas de Netflix, la cual ayuda a que todo siga funcionando cuando un nodo muere.


  * ¿Qué es un microservicio híbrido?
        Esta no la entendi muy bien, solo entendi que es una combinacion entre las dos anteriores :(


  * ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
        -Carga de trabajo particionada
        -Solicitudes de nivel en el cache
        -Respaldo de token seguro
        -Caos bajo carga


  * ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
        -NodeJS
        -Python
        -Ruby
        -Docker


  * ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
        -Herramientas de productividad
        -Fragmentacion en base a imagenes
        -Gestion de nodos
        -Duplicacion de librerias/plataformas
        -Curva de aprendizaje


  * ¿Qué es Spinnaker?
        Una herramienta DevOps para desplegar a producción rápido, seguro y repetible


  * ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
        Con la ley de Conway


  * ¿Qué es "_chaos engineering_" o "_ingeniería del caos_"?
        La ingeniería del caos está basada en cuatro principios definidos por  Netflix. Dichos principios consisten en definir un estado estable, realizar una hipótesis del estado que le seguirá, introducir variables que reflejen eventos fieles a la realidad e intentar romper la hipótesis, por ese orden.


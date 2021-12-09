### Parte 3

## Monolitico vs Microservicios

# Monolitica
La arquitectura Monolitica es la manera más "común" de desarrollar una aplicación.
Es un mismo bloque de codigo donde todo trabaja como un conjunto, tanto como el lado del usuario, la interfaz, la base de datos, etc.

Las aplicaciones que utilizan esta estructura son unico bloque de codigo. 

Las ventajas de esta estructura es que son mas faciles de testear o debugear. Son sencillas de desarrolar y faciles de lanzar.

Entre las desventajas de incluye que son menos ordenadas, por lo que su comprensión es mas complicada. El hacer cambios en ella es mas complejo ya que al ser un unico bloque de codigo al realizar un cambio en alguna parte del mismo debes hacerlo en todo lo demás. No puede ser escalada al ser un unico conjunto. 

# Microservicios

Las aplicaciones basadas en esta arquitectura son una colección de pequeñas unidades independientes, cada una ellas llamadas "Servicios". Estas unidades se encargan de una funcion distinta, por lo que cada servicio tiene su propia logica.

Entre los beneficios de la arquitectura de Microservicios se destaca:
Que como consecuencia de que un servicio sea pequeño, pueden ser desarrollados por uno o más equipos pequeños. Así mismo es posible escalar estos servicios.

Una vez lanzados los servicios al ser independientes uno de otros, es mas facíl identificar cuales de estos son los que reciben más carga que otros y así poder enfocarse en escalarlos.

Al fallar uno de estos servicios, sí nuestra aplicación esta bien respaldada no necesariamente tiene que dejar de funcionar nuestra aplicación.

Una de las más grandes ventajas es que al ser independientes tenemos la libertad de elegir que tecnología utilizar en cada uno de los servicios, tales como su lenguaje de programacion, la base de datos, etc.

Las desventajas de esta arquitectura es que las aplicaciones tienden a ser mucho más grandes y complejas que las monoliticas. Por lo mismo su desarrollo se ve entorpecido, por lo que no son recomendadas si tenemos una fecha de lanzamiento más corta de lo habitual.

# Puntos claves a tener en cuenta al momento de decidir entre una arquitectura Monolitica o una de Microservicios

Primero que nada hay que saber las capacidades de nuestro equipo, no siempre tener el equipo más grande es lo más eficiente, hay que tener en cuenta las habilidades y limitantes de cada uno de nuestros integrantes.

Pensando en la ecalabiidad de la aplicación hay que pensar tambien como el equipo puede escalar tambien con respecto a sus capacidades y la contribución que pueden aportar.

Con respecto a su lanzamiento las aplicaciónes monoliticas te permiten ser lanzadas y simplemente ir haciendo ajustes sobre la marcha. El problema con estas es que si un solo punto falla con estos cambios, toda la aplicacion colapsa.
Mientras que las aplicaciones basadas en microservicios requieren un efuerzo aun mayor en su lanzamiento, te permite lanzar cada servicio de manera independente. Asímismo al depender de herramientas de conexion entre servicios se incrementa el tiempo requerido para lanzar cada uno de estos servicios. Por ulitmo, al ser servicios independientes, si perdemos uno de estos, no necesariamente perderemos el proyecto entero.

Hablando de su mantenimiento no todo desarrollador esta familiarizado con Docker o las herramientas de conexion entre servcios. Por lo que esto puede ser un punto critico a tener en cuentra a la hora de elegir una u otra arquitectura para nuestro proyecto.

Sobre la confiabilidad los microservicios son claros ganadores, esto debído a la independiencia de cada uno de los servicios, si uno de estos servicios cae, solo una parte de nuestra aplicacion se veria comprometida. Aquí ponemos el ejemplo de una aplicacion bancaría.
Dónde si falla el servicio de transferencias bancarias es menos perjudicial que el perder toda la aplicación por completo.

En escalabilidad tambien las aplicaciones basadas en microservicios son amplias ganadoras. Volviendo a lo mismo de que los servicios son independientes son sencillos de escalar con respecto a nuestras necesidades.

Con todo esto ya pdemos darnos una idea de que arquitectura es la indicada para nosotros.

Hablando desde el punto de vista del testing los microservicios son mucho más complicado de testear, esto debido a que en la mayoria de los casos un servicio es muy complicado testear un solo servicio, esto debido a que se requiere del funcionamiento de otros servicios para ejecutarse correctamente. Sin hablar de las pruebas de integracion las cuales nos quitarian mucho tiempo en implementar.

# Transicion a Microservicios

Para una correcta transición a los microservicios se debe tener un plan bien definido. Tomar en cosideracion cuales son nuestros procesos criticos y tomarlos como objetivos de alto nivel. Determinar cuales son los componentes claves. Tambein debemos tener identidicados cuales son las funcionalidades de bajo impacto, de cuales podemos presindir al inicio de nuestro desarrollo.

# En conclusión
Ya con esta idea más clara sobre que son y como funcionan las aplicaciones monoliticas y las de microservicios, he llegado a la conclusión de que como estudiantes debemos seguir adoptando la arquitectura monolitica para nuestras aplicaciones o proyectos personales. Sin embargo no debemos dejar de experimentar con el uso de un arquitectura de microservicios, implementandola poco a poco a nuestros proyectos una vez que tengamos más experiencía como programadores.

Las ventajas de las aplicaciones basadas en microservicios son claras ante las monoliticas pero requiere un mayor esfuerzo y el conocimiento de varias tecnologías, por lo que equipos pequeños que no esten familiarizados con este tipo de estructura tendrá muchos problemas para adoptarla, asímismo los recursos requeridos de hardware para ejectutar este tipo de aplicaciones son mucho mayores, esto tambien complica mucho el desarrollo de las mismas.
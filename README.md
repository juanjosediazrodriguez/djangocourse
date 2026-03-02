## Preguntas Tutorial 03-B

**¿Puedes entender las diferencias entre las dos propuestas?**
En la versión con DI (`ImageViewFactory`), la vista recibe el objeto de almacenamiento desde afuera como parámetro, sin saber cuál implementación concreta se usa. En la versión sin DI (`ImageViewNoDI`), la vista crea ella misma el objeto `ImageLocalStorage()` internamente, acoplándose directamente a esa clase.

**¿Ventajas/desventajas de cada una?**
La versión con DI es más flexible y testeable: se puede cambiar el tipo de almacenamiento (local, S3, etc.) sin modificar la vista, solo cambiando qué se inyecta. Su desventaja es que es más compleja de entender. La versión sin DI es más simple y directa, pero si se quiere cambiar el almacenamiento hay que entrar a modificar la lógica de la vista, lo que viola el principio de responsabilidad única.

**Comparación con programación estructurada vs POO:**
En programación estructurada, las dependencias del código siguen la misma dirección que el flujo de control: si A llama a B, A depende de B directamente. Con POO e inversión de dependencias, se introduce una interfaz (`ImageStorage`) que invierte esa relación: tanto la vista como `ImageLocalStorage` dependen de la abstracción, no entre sí. Esto permite que el flujo de control y las dependencias del código apunten en direcciones opuestas, dando mayor flexibilidad al sistema.

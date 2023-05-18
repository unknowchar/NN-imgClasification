#INTRODUCCIÓN


---


>## Dataset: MNIST
>El set de datos elegido para este proyecto fue el data set de MNIST. Este dataset surgió alrededor de 1999 siendo un ejemplo básico y bueno para aquellos que deseen experimentar con las redes Neuronales y la computación visual, siendo un dataSet relativamente sencillo y común de entrenar entre los miles de datasets que existen en la actualidad.
>### Características
> * Está compuesto por 70,000 imágenes, de las cuales 60,000 de ellas son regularmente usadas para entrenar a la red neuronal y las otras 10,000 son usadas para realizar las pruebas de entrenamiento. 
>*Estás imágenes tienen un alto y ancho de 28px, cada una de ellas contiene un número del 0 al 9, siendo claramente 10 categorías para la salida de datos de está red. 
>* Todas estás imágenes están en una escala de grises.


---


>## Arquitectura de red neuronal: Convolucional
>>## Conceptos básicos
>>### ¿Qué es la convolución?
La convolución consiste en realizar un barrido de la imagen para tomar grupos de píxeles cercanos entre sí de la imagen de entrada y realizar un producto punto contra un kernel y un respectivo pooling.

>>### Kernel
El kernel es un filtro, el cual, se le aplica a la imagen a procesar para así extraer características especiales de la imagen para después hacer uso de estos nuevos valores filtrados. Principalmete se detectan bordes, desenfoque, entre otras características. Estos filtros están estructurados por matrices con valores predeterminados los cuales se multiplican contra un grupo de píxeles. <br> 

>>### Pooling
El pooling tiene en común con el kernel el manejo de  agrupaciones de píxeles específicas, funciona también como un "filtro" tomando únicamente los valores más altos de esas agrupaciones especificadas hasta reducirlas notablemente para al final sear reagrupadas y mantener sus características, siendo posible combinarse junto con el  Kernel para obtener detalles más precisos.

>### Red Neuronal Convolucional
>### Estructura
Las redes neuronales convolucionales suelen ser una arquitectura muy convencional para el procesamiento y clasificación de imágenes. Existen muchos modelos de redes neuronales convolucionales, pero al trabajar en los datos de MNIST hablaremos del modelo de RNC llamado LeNet. Este modelo está compuesto de dos partes, uno en donde hace recepción de los datos (su capa de entrada) mediante 2 capas convolucionales que incluyen su respectivo sistema de pooling.
Las capas convolucionales se dedican a extraer características de las imágenes y de obetener una representación compacta y con base a esta seguir compactandola aun más y de realizar la calsificación de cada imagen.



---



>## Modelo Lenet
El modelo Lenet utiliza la arquitectura de una red neuronal convolucional, disminuyendo su alto y su ancho pero al mismo tiempo de que este ocurre su profundidad aumenta progresivamente. 
<img src="https://www.codificandobits.com/img/posts/2019-04-26/red-lenet.png">


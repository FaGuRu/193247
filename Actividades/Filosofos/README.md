Matricula: 193247              Alumno: Gumeta Ruíz Fabricio Tadeo           Matria: Programación concurrente            Corte: 2

Problematica:
Cada filósofo puede tomar los tenedores que están a su izquierda o derecha, para poder comer el filósofo de tener los dos tenedores. Si cualquier filósofo toma los dos tenedores entonces los que están al lado queda en espera. Hay un tenedor y los dos filósofos compiten por tomarlo y uno queda sin tenedores. Si todos los filósofos toman el tenedor que está a su derecha entonces todos se quedaran esperando infinitamente. Nadie va a ceder su tenedor porque todos están en la misma situación.¿Cómo podemos hacer para que los filósofos no sufran para comer? , el problema en sí tiene muchas soluciones pero solo vamos a enunciar una: Un filósofo toma los dos tenedores y los demás hacen una cola alrededor de la mesa para saber cual es el siguiente hasta que todos acaban.

Explicación del código:

Se utilizo el metodo __int__ porque es el constructor de la clase filosofo, en el este metodo creamos la instancia de la clase, donde le damos ciertos atributos como lo es el id.

Se utilizo super().__init__() es para que las clases o metodos secundarios que pueden estar usando herencia múltiple cooperativa llamen a la siguiente función de clase primaria.

Se utilizo self para pasar la instancia de la clase a los métodos de instancia.
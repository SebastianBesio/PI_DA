<h1 align='center'>
 <b>Cryptocurrency Market Data Analytics</b>
</h1>

# <h1 align="center">**`Informe de introducción al mercado de las criptomonedas.`**</h1>

<p align='center'>
<img src ="https://brightnode.io/wp-content/uploads/2022/10/Are-Cryptocurrencies-Securities-or-Commodities-Brightnode-consultancy-930x620.jpeg" width="300">
<p>

# **Objetivo**

 Este informe está dirigido a aquellas personas que no tengan tanto conocimiento de las criptomonedas y quieran comprender mejor este mercado para empezar a dar sus primeros acercamientos en este mundo.

# **Introduccion Criptomonedas**

El mundo de las criptomonedas a tenido un crecimiento y adopción importante a nivel mundial.

### *¿Qué es una criptomoneda?*

Una criptomoneda es un activo digital que emplea un cifrado criptográfico para garantizar su titularidad y asegurar la integridad de las transacciones, y controlar la creación de unidades adicionales, es decir, evitar que alguien pueda hacer copias como haríamos, por ejemplo, con una foto. Estas monedas no existen de forma física: se almacenan en una cartera digital.

### *¿Cómo funcionan las criptomonedas?*

Las criptomonedas cuentan con diversas características diferenciadoras respecto a los sistemas tradicionales: no están reguladas ni controladas por ninguna institución y no requieren de intermediaros en las transacciones. Se usa una base de datos descentralizada, blockchain o registro contable compartido, para el control de estas transacciones.

Al hilo de la regulación, las criptomonedas no tienen la consideración de medio de pago, no cuentan con el respaldo de un banco central u otras autoridades públicas y no están cubiertas por mecanismos de protección al cliente.

En cuanto a la operativa de estas monedas digitales, es muy importante recordar que una vez que se realiza la transacción con criptomonedas, es decir, cuando se compra o vende el activo digital, no es posible cancelar la operación porque el blockchain es un registro que no permite borrar datos. Para "revertir" una transacción es necesario ejecutar la contraria.

# **Alcance**

Debido a que hay un sin fin de monedas para poder estudiar, se opto por reducir este análisis introductorio a solo 10 monedas.

Teniendo en cuenta el publico objetivo del informe, pareció oportuno tomar las 10 monedas con mayor `capitalización de mercado` (valor total de una criptomoneda) ya que son las mas conocidas y establecidas en el mercado en este momento.

Con esas monedas se estudiaron distintos casos que ocurren con ellas para ejemplificar varias situaciones que pueden suceder con criptomonedas.

### **Las 10 criptomonedas elegidas**

A la fecha de la extracción de datos (10/08/2023) el ranking y valores de las 10 monedas elegidas es el siguiente:

| Moneda | Capitalización de Mercado | Fecha creación |
| - |- | - |
| Bitcoin | $573,275,353,641 | Ene 2009 |
| Ethereum | $222,779,937,243 | Jul 2015 |
| Tether | $83,523,033,624 	 | Oct 2014 |
| BNB | $37,278,781,259 | Dic 2016 |
| XRP | $33,264,038,194 | Jun 2012 |
| USD Coin | $26,194,591,871 | Set 2018 |
| Lido Staked Ether | $14,883,170,103 | Dic 2020 |
| Dogecoin | $10,704,527,382 | Dic 2013 |
| Cardano | $10,439,618,161 | Set 2017 |
| Solana | $9,968,918,311 | Mar 2020 |

Es importante recordar que este ranking es para un momento puntual, este era distinto en el pasado y va a ser distinto en el futuro con la aparición de nuevas monedas y cambio en la preferencia de criptomonedas de los usuarios. Igual a pesar de eso es un buen punto de partida para el análisis que queremos realizar.

Entre ellas hay varias monedas que tienen unos 10 años desde su creación y algunas otras mas nuevas.

# **Datos**

Se utilizó [CoinGecko](https://www.coingecko.com/) para conocer las criptomonedas y se extrajeron los datos a travez de la [API CoinGecko](https://www.coingecko.com/en/api/documentation).

Las tres variables principales que se pueden obtener de una criptomoneda son,
- `precio` (price): Precio de la criptomoneda.
- `capitalización de mercado` (market capitalization): es el valor total de una criptomoneda, precio de la criptomomneda por la cantidad total que existen.
- `volumen` (24hr volume): Volumen de transacciones de la criptomomneda en las ultimas 24 horas.

Esas se podian extrar mas facilmente con un endpoint (**/coins/{id}/market_chart/range**) que le pasabas el rango de tiempo y la moneda y te devolvia esas tres variables.

**Extracción variables adicionales**

Pero como se queria ver si otros factores incidian como el de las redes sociales se opto por usar otro endpoint (**/coins/{id}/history**) que también traia algunas variables adicionales.

La gran desventaja que tenia usar este endpoint era que no tenia rango de fecha y habia que hacerlo por cada dia e iba a llevar mas tiempo extraer los datos.

Se tomo un rango de 2 años y medio, para 10 monedas `2,5 años * 365 dias * 10 monedas = 9125 consultas` . Teniendo en cuenta que la API Acepta 10-30 consultas por minuto se optó por esperar 5 segundos entre cada consulta (aprox 12 por minuto). Llevando el tiempo total a un valor aproximado de `9125/12 = 760 minutos = 12.6 horas`.

Se dejó toda la noche levantando datos corriendo el [get_data](get_data.py) que se encargaba de consultar e ir guardando en un JSON [raw_coins_data](datasets/raw_coins_data.json).


 **Análisis Exploratorio de los Datos (EDA)**

Luego de tener los datos se realizó un EDA en donde,

- Se limpiaron los datos, chequeraon duplicados, datos faltantes y tipos de dato.
- Se conocieron los datos, graficaron distintas variables y se realizaron correlaciónes.
- Se exportaron las datos limpios con las columans a estudiar en [cleaned_coins_data](datasets/cleaned_coins_data.csv).

Para información mas detallada se puede ver el análsiis completo en [1_EDA](1_EDA.ipynb).

## **Estudio de monedas**

### **Dominio de la Bitcoin**

El dominio de una moneda esta marcado por el porcentaje de la capitalización de mercado que acapara. Como la `bitcoin` fue la primer moneda y la mas reconocida es la que ha tenido mas aceptación y uso.

Por ese dominio el precio de la `bitcoin` influencia al resto del las monedas del mercado, principalmente a las monedas de menor capitalización de mercado. 

Si miramos la correlacion entre los precios de las monedas se puede ver que la mayoria estan bastante correlacionados.

Esté estudio se realizó entre el 01/01/2021 y el 31/07/2022 y se puede ver como el porcentaje de capitalización de mercado de la `bitcoin` baja de 80% a 55% aproximadamente.

Esto se explica por el crecimiento de capitalización de mercado de otras monedas. Las que mas resaltan son `ethereum` y `tether`.

### **Criptomonedas estables (stablecoins)**

Una criptomoneda estable es una criptomoneda diseñada para minimizar la volatilidad del precio de estas, en relación a un activo "estable" o conjunto de activos. Una moneda estable puede estar vinculada a una criptomoneda, a dinero Fiat, o al comercio de commodities (tales como metales preciosos o metales industriales).

Las ventajas de las criptomonedas respaldadas por activos es que están estabilizadas por activos que operan fuera del espacio de dichas criptomonedas. O sea, que el activo subyacente no es correlativo, reduciéndose así el riesgo financiero. 

Al ofrecer estabilidad en su valor, las stablecoins pueden ser utilizadas para realizar pagos, préstamos y otros usos similares al dinero tradicional. De esta manera te podes evitar que tu dinero cambie de valor y evitar por ejemplo hacer cambios de divisas.

En nuestras monedas de estudio hay dos criptomonedas estables, la `Tether` y la `USD Coin`. Ambas tienen un valor practicamente de 1 USD ya que estan relacionadas y respaldadas para que ese precio se mantenga de esa manera.

Las monedas estables respaldadas están sujetas a la misma volatilidad y riesgos asociados que el activo de respaldo. Si la moneda estable es respaldada de manera descentralizada, entonces es relativamente segura frente a los depredadores. Pero si hay una bóveda central, puede ser robada, o sufrir pérdida de confianza.

Por mas que se afirma que hay un respaldo 1 a 1 del valor en USD de ambas monedas estables, han sido acusadas de ser incapaces de demostrarlo, generando algunas dudas sobre la confianza de estas monedas.


### **Ethereum y Staked Ether**

El `ethereum` es una moneda que ha tenido gran aceptación creciendo en el porcentaje de capitalización de mercado. Un detalle adicional es que existe una moneda llamada `Staked Ether` que se puede observar que tiene practicamente el mismo precio que el `ethereum`. Esto es porque el `Staked Ether` en realidad es una moneda "auxiliar" al `ethereum` que se utiliza para poder ser  validadores de una red (Los validadores verifican las transacciones de la red y reciben recompensas por esta actividad).

## **Promedio Movil Simple (SMA)**

Para poder ver las tendencias de precios de una moneda se puede analizar el promedio movil de una moneda.

Se puede hacer un promedio movil de por ejemplo 200 días para ver la tendencia a largo plazo de una moneda.

Si se utiliza menor cantidad de dias para el promedio movil se pueden ver comportamientos mas a corto plazo (por ejemplo 50 días).

Hay que tener cuidado si se utilizan lapsos de tiempo muy corto ya que pueden empezar a mostrar demasiadas fluctiaciones como para poder analizarlo correctametne la evolución del precio.

## **Precio Máximo Absoluto (ATH)**

El valor del ATH por si solo no dice tanta información, pero se pueden hacer algunas métricas para sacar información relevante.


- **% ATH**: Porcentaje Precio Actual con respecto al ATH.
- **Días ATH**: Días desde que sucedió el utimo Precio Máximo Absoluto.

Si estudiamos el caso de `dogecoin` por ejemplo vemos que en este momento el precio es alrededor del 10% con respecto a su ATH. Y tambien podemos ver que paso hace mas de 800 días. Esta convinacion de bajo **% ATH** y gran cantidad de **Días ATH** marca una alerta en esa moneda ya que tuvo su maximo hace muchisimo tiempo y desde entonces ha tenido una baja muy significativa del precio.


## **Redes Sociales****

Los valores de las redes sociales pueden ser importantes, principalmente para monedas con bajo nivel de capitalización de mercado. 

Volviendo al caso de `dogecoin` podemos ver que cuando tuvo su gran pico de precios en mayo del 2021 se vio acompañado por gran cantidad de comentarios de reddit y aumento de seguidores en twitter.

En esas fechas personas notoriamente conocidas hablaron de la moneda en las redes generando una bola de nieve y aumentando el precio de forma exponencial.

Igual hay que tener mucho cuidado porque que haya relacion entre el precio y las redes sociales no necesariamente implica que una es consecuencia de la otra.

## **KPIs**

### **Cambio porcentual**

El cambio porcentual de una moneda se puede utilizar para saber cuanto ha variado el precio de una moneda en cierto rango de tiempo. Al ser porcentual nos permite evaluar rapidamente cuan significativo fue ese cambio.

### **Retorno de Inversión (ROI)**

Este valor está definido por las ganancias (o pérdidas) generadas por una inversion.

En nuestro caso dejamos previsto que se coloque una cantidad hipotética de una monedas compradas y podemos ver cuanto hubiera sido nuestro retorno de inversión al final de un periodo.

En este caso que estamos trabajando con datos estaticos sirve para simular inversiones, pero en el caso de que tuvieramos datos vivos podriamos utilizarlo para saber realmente el ROI que tendríamos.

### **Coeficiente de Variación**

Una manera de ver cuanta fluctuación tiene una moneda seria utilizando el coeficiente de variación.

La formula está dada por la desviación estandar dividido la media.

Mientras mas cercano a 0 menos fluctuaciones tiene la moneda. Por ejemplo las stable coins tienen valores de practicamente 0.


# **Conclusiones**

Las criptomonedas tienen una gran variedad de tipos y usos.

En el caso que se quiera utilizar criptomonedas para poder hacer transacciones rápidas de dinero pero sin el riesgo de las fluctuaciones de precios conviene utilzar `stable coins`.

Si se quiere hacer inversiones a largo plazo se puede estudiar el promedio móvil de una moneda para un lapso grande de dias e ir viendo como viene la tendencia general de la moneda. Dos monedas que aparentan estar en subida los ultimos meses son `ethereum` y la `bitcoin`, mas alla de las fluctuaciones que puedan tener en los distintos dias.

Hay que tener cuidado con las monedas que hayan tendio el valor de precio máximo hace mucho tiempo y que hoy en día tengan una pequeña fracción de su valor ya que no serian una buena inversion segun los datos porque probablemente sigan en un pequeño declive a medida que pase el tiempo.
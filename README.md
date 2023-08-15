<h1 align='center'>
 <b>Cryptocurrency Market Data Analytics</b>
</h1>

# <h1 align="center">**`Informe de introducción al mercado de las criptomonedas.`**</h1>

<p align='center'>
<img src ="https://brightnode.io/wp-content/uploads/2022/10/Are-Cryptocurrencies-Securities-or-Commodities-Brightnode-consultancy-930x620.jpeg" width="300">
<p>

# **Objetivo**

El mundo de las criptomonedas a tenido un crecimiento y adopción importante a nivel mundial. Este informe está dirigido a aquellas personas que no tengan tanto conocimiento de las criptomonedas y quieran comprender mejor este mercado para empezar a dar sus primeros acercamientos en este mundo.

# **Introduccion Criptomonedas**

### *¿Qué es una criptomoneda?*
Una criptomoneda es un activo digital que emplea un cifrado criptográfico para garantizar su titularidad y asegurar la integridad de las transacciones, y controlar la creación de unidades adicionales, es decir, evitar que alguien pueda hacer copias como haríamos, por ejemplo, con una foto. Estas monedas no existen de forma física: se almacenan en una cartera digital.

### *¿Cómo funcionan las criptomonedas?*

Las criptomonedas cuentan con diversas características diferenciadoras respecto a los sistemas tradicionales: no están reguladas ni controladas por ninguna institución y no requieren de intermediaros en las transacciones. Se usa una base de datos descentralizada, blockchain o registro contable compartido, para el control de estas transacciones.

Al hilo de la regulación, las criptomonedas no tienen la consideración de medio de pago, no cuentan con el respaldo de un banco central u otras autoridades públicas y no están cubiertas por mecanismos de protección al cliente.

En cuanto a la operativa de estas monedas digitales, es muy importante recordar que una vez que se realiza la transacción con criptomonedas, es decir, cuando se compra o vende el activo digital, no es posible cancelar la operación porque el blockchain es un registro que no permite borrar datos. Para "revertir" una transacción es necesario ejecutar la contraria.

Como éstas monedas no están disponibles de forma física, hay que recurrir a un servicio de monedero digital de criptomonedas, que no está regulados para almacenarlas.

# **Alcance**

Debido a que hay un sin fin de monedas para poder elegir y analizar, se opto por reducir el analisis a solo 10 monedas.

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

Es importante recordar que este ranking es para un momento puntual, este era distinto en el pasado y va a ser distinto en el futuro. Igual a pesar de eso es un buen punto de partida para el análisis que queremos realizar.

Entre ellas se encuentran algunas que en el entorno de los 10 años y algunas otras mas nuevas.

# **Datos**

Se utilizó [CoinGecko](https://www.coingecko.com/) para conocer las criptomonedas y se extrajeron los datos a travez de la [API CoinGecko](https://www.coingecko.com/en/api/documentation).

Las tres variables principales que se pueden obtener de una criptomoneda son,
- `precio` (price): Precio de la criptomoneda
- `capitalización de mercado` (market capitalization): es el valor total de una criptomoneda, precio de la criptomomneda por la cantidad total que existen.
- `volumen` (24hr volume): Volumen de la criptomomneda en las ultimas 24 horas.

Esas se podian extrar mas facilmente con un endpoint (*/coins/{id}/market_chart/range*) que le pasabas el rango de tiempo y la moneda y te devolvia esas tres variables.

### **Endpoint Hisotry**

Pero como se queria ver si otros factores incidian como el de las redes sociales se opto por usar otro endpoint (*/coins/{id}/history*) que ademas de esos valores tambien traia algunas variables sobre redes sociales. La gran desventaja que traia era que no tenia rango de fecha y habia que hacerlo por cada dia.

Se tomo un rango de 2 años y medio, para 10 monedas `2,5 años * 365 dias * 10 monedas = 9125` consultas.

Teniendo en cuenta que la API Acepta 10-30 request por minuto se optó por esperar 5 segundos entre cada consulta (aprox 12 por minuto).   entre `9125/12 = 760 minutos = 12.6 hs`.

Se dejó toda la noche levantando datos corriendo el [get_data.py](get_data.py) que se encargaba de consultar e ir guardando en un JSON [raw_coins_data.json](datasets/raw_coins_data.json).

---
## **Estudio de monedas**

### **Dominio de la Bitcoin**


The ratio of the market capitalization of Bitcoin to the total market capitalization of Bitcoin is known as Bitcoin dominance. A cryptocurrency's market capitalization is a measurement of its market value

Bitcoin dominance influences the whole market as most of the smaller cap coins follow Bitcoin price movements. It measures Bitcoin’s market cap in relation to the rest of the market. If the total market cap of the whole market is growing and Bitcoin dominance is going down, an “alt season” (the bull market for altcoins) is likely approaching.

Un primer factor importante a tener en cuenta es que la Bitcoin tiene un dominio importante sobre el mercado.

Esto significa que si la Bitcoin tiene cambios de precio, eso va a afectar a casi todas las monedas.



### **Criptomonedas estables (stablecoins)**

Una criptomoneda estable es una criptomoneda diseñada para minimizar la volatilidad del precio de estas, en relación a un activo "estable" o conjunto de activos. Una moneda estable puede estar vinculada a una criptomoneda, a dinero Fiat, o al comercio de commodities (tales como metales preciosos o metales industriales).

Se dice que las monedas estables canjeables por divisas, mercancías, o dinero fiat están respaldadas; mientras que aquellas ligadas a un algoritmo se denominan de tipo señoreaje (no respaldadas).


Las ventajas de las criptomonedas respaldadas por activos es que están estabilizadas por activos que operan fuera del espacio de dichas criptomonedas. O sea, que el activo subyacente no es correlativo, reduciéndose así el riesgo financiero. 



En nuestras monedas de estudio de mayor capitalización de mercado hay dos criptomonedas estables, la `Tether` y la `USD Coin`. Ambas tienen un valor practicamente de 1 USD ya que estan relacionadas y respaldadas para que ese precio se mantenga de esa manera.

Las monedas estables respaldadas están sujetas a la misma volatilidad y riesgos asociados que el activo de respaldo. Si la moneda estable es respaldada de manera descentralizada, entonces es relativamente segura frente a los depredadores. Pero si hay una bóveda central, puede ser robada, o sufrir pérdida de confianza.2​ 



Por mas que se afirma que hay un respaldo 1 a 1 del valor en USD de ambas monedas estables, han sido acusadas de ser incapaces de demostrarlo.

# **Conclusiones**


# **Herramientas**
Se mencionan las tecnologías y herramientas utilizadas en el proyecto, así como la metodología aplicada de manera exhaustiva.

Además, se presentan análisis detallados y conclusiones fundamentadas que demuestran un profundo entendimiento de los datos analizados.


---

### **Staked Ether**

give financial or other support to.
"he staked him to an education at the École des Beaux-Arts"
 Understanding Staked Ether (stETH)

To understand stETH, it's important first to understand the concept of "staking" cryptocurrency tokens. Proof-of-stake is the consensus mechanism used by Ethereum, implemented in September 2022.3 Ether (ETH) is the native blockchain token for the Ethereum blockchain.4

Users that wish to participate in the network by becoming a validator must offer ether as a "stake"—an interest in remaining an honest network participant. The staked cryptocurrency is used as an incentive; it can be taken away if a validator doesn't act in the best interest of the blockchain and other participants.5

Owners that stake their cryptocurrency are allowed to participate in transaction validation; they open new blocks and receive rewards in the form of a percentage of the transaction value they work to validate. Because staking effectively removes cryptocurrency from a user's liquid assets, there is a risk that they could lose capital because they cannot unstake their crypto until the Ethereum Shanghai upgrade is rolled out.5


## **Distintos casos de estudio ??????**
MACD

The moving average convergence divergence indicator (or oscillator) is a good buying or selling simple momentum indicator and one of the most popular tools used by crypto traders.

The MACD divergence refers to the two underlying moving averages moving apart, while the convergence relates to the two underlying moving averages coming towards each other.

 What Is an Exponential Moving Average (EMA)?

An exponential moving average (EMA) is a type of moving average (MA) that places a greater weight and significance on the most recent data points. The exponential moving average is also referred to as the exponentially weighted moving average. An exponentially weighted moving average reacts more significantly to recent price changes than a simple moving average simple moving average (SMA), which applies an equal weight to all observations in the period. 


The MACD indicator is the difference between a short period and a longer period of exponential moving averages. Typically, the 12 and the 26-period EMAs are considered in crypto. The result of those calculations is the MACD line, which can offer interesting buy or sell signals.

If the MACD is above 0, it is positive and indicates an upside (bullish) momentum, meaning that it is a good time to buy. If it is below 0, it is negative and shows a downside (bearish) momentum, meaning that it is a good time to sell.

Use the same rules that apply to SMA when interpreting EMA. Keep in mind that EMA is generally more sensitive to price movement. This can be a double-edged sword. On one side, it can help you identify trends earlier than an SMA would. On the flip side, the EMA will probably experience more short-term changes than a corresponding SMA.

## **Distintos casos de estudio ??????**



- **Bitcoin Dominance**
- **SMA predicciones?**
- **Dogecoin - Red Flag ATH, ATH % current value and ATH time**
- **USD-coin**

- **Ethereum vs staked ethereum**
- **Evolucion de las dos mas nuevas Staked Ether y Solana?**
- **# cantidad cripto por años?**

# **Conclusiones**

Al principio conviene ser mas conservador y no especular con nuevas monedas que pueden tener mucha volatilidad. Tener cuidado con monedas que tuvieron su valor máximo hace mucho tiempo y hoy valen solo una pequeña fraccion de lo que valieron.


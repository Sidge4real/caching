# Caching Implementation Testing

This repository contains a set of Python and Express.js applications that demonstrate and test various caching techniques. It includes Python scripts that test different cache strategies and an example use case, as well as two Express.js applications—one using Redis caching and the other without it. The repository also includes benchmark results to compare the performance of the two Express.js applications.

## Project Overview

1. **Python Scripts for Testing Caching Techniques**
   - The Python scripts explore different caching mechanisms, including Redis, disk-based caches, and in-memory caches, to evaluate their performance for an example application.
   - These scripts demonstrate how to use the `redis` library, Python's built-in `pickle` module, and other caching solutions.
   - **Installation**:
     - To install the necessary Python dependencies, run:
       ```bash
       pip install -r requirements.txt
       ```
     - After installing the dependencies, you can run the Python scripts to test caching strategies. The scripts include implementations for Redis-based caching and a variety of other caching techniques.

2. **Express.js Applications for Benchmarking Caching**
   - Two separate Express.js applications are included:
     1. **With Redis Caching**: This app uses Redis for caching data.
     2. **Without Caching**: This app does not use Redis and directly fetches the data from the external API every time.
   - Both applications serve the same API, which returns news data from an external API, but one uses Redis to cache the data for faster retrieval.
   - **Benchmarking**:
     - Benchmark results are included in the `/benchmarks` folder.
     - Results and performance analysis are documented in the `/performance` folder.
   - **Running the Express.js Apps**:
     - Make sure you have Node.js installed on your machine.
     - To install the dependencies, run:
       ```bash
       npm install
       ```
     - To run the apps:
       - For the Redis application: `node app-with-redis.js`
       - For the non-Redis application: `node app-without-redis.js`
     - Then, run the following curl commands to test the APIs and record the benchmarks:
       ```bash
       curl -w "Time to first byte: %{time_starttransfer}\nTotal time: %{time_total}\n" -o /dev/null -s http://localhost:8000/news
       curl -w "Time to first byte: %{time_starttransfer}\nTotal time: %{time_total}\n" -o /dev/null -s http://localhost:8001/news
       ```

## Performance Results

- The benchmark results are saved in the `/performance` folder. In these results, you'll find:
  - **Comparison of response times**: The two applications (with and without Redis) are compared in terms of response times for the same API request.
  - **Observations**: Key takeaways from the benchmarking, such as how Redis caching improved performance and reduced latency.
  
## Conclusion

- **Purpose of This Project**: This project demonstrates the impact of caching on API response times, comparing scenarios with and without Redis caching.
- The purpose is to test and understand how caching (particularly Redis) can optimize performance, reduce server load, and improve user experience in real-world applications.
  
---

### In Dutch

## Caching Implementatie Testen

Deze repository bevat een reeks Python- en Express.js-toepassingen die verschillende cachingtechnieken demonstreren en testen. Het bevat Python-scripts die verschillende cache-strategieën testen en een voorbeeldtoepassing, evenals twee Express.js-toepassingen—één met Redis-caching en de andere zonder Redis. De repository bevat ook benchmarkresultaten om de prestaties van de twee Express.js-toepassingen te vergelijken.

## Project Overzicht

1. **Python-scripts voor het testen van cachingtechnieken**
   - De Python-scripts verkennen verschillende cachingmechanismen, waaronder Redis, schijfgebaseerde caches en in-memory caches, om hun prestaties te evalueren voor een voorbeeldtoepassing.
   - Deze scripts demonstreren hoe de `redis`-bibliotheek, de ingebouwde `pickle`-module van Python en andere cachingoplossingen te gebruiken.
   - **Installatie**:
     - Om de benodigde Python-afhankelijkheden te installeren, voer je het volgende uit:
       ```bash
       pip install -r requirements.txt
       ```
     - Na installatie van de afhankelijkheden kun je de Python-scripts uitvoeren om de cachingstrategieën te testen. De scripts bevatten implementaties voor Redis-gebaseerde caching en andere cachingtechnieken.

2. **Express.js-toepassingen voor benchmarking van caching**
   - Er zijn twee aparte Express.js-toepassingen inbegrepen:
     1. **Met Redis-caching**: Deze app gebruikt Redis voor het cachen van data.
     2. **Zonder Caching**: Deze app gebruikt geen Redis en haalt de data elke keer opnieuw op van de externe API.
   - Beide toepassingen bieden dezelfde API, die nieuwsdata van een externe API retourneert, maar de ene gebruikt Redis om de data te cachen voor snellere toegang.
   - **Benchmarking**:
     - Benchmarkresultaten zijn opgeslagen in de map `/benchmarks`.
     - Resultaten en prestatieanalyse zijn gedocumenteerd in de map `/performance`.
   - **De Express.js-toepassingen uitvoeren**:
     - Zorg ervoor dat Node.js is geïnstalleerd op je machine.
     - Om de afhankelijkheden te installeren, voer je het volgende uit:
       ```bash
       npm install
       ```
     - Om de toepassingen uit te voeren:
       - Voor de Redis-toepassing: `node app-with-redis.js`
       - Voor de non-Redis-toepassing: `node app-without-redis.js`
     - Voer daarna de volgende curl-opdrachten uit om de API's te testen en de benchmarks op te nemen:
       ```bash
       curl -w "Time to first byte: %{time_starttransfer}\nTotal time: %{time_total}\n" -o /dev/null -s http://localhost:8000/news
       curl -w "Time to first byte: %{time_starttransfer}\nTotal time: %{time_total}\n" -o /dev/null -s http://localhost:8001/news
       ```

## Prestatie Resultaten

- De benchmarkresultaten zijn opgeslagen in de map `/performance`. In deze resultaten vind je:
  - **Vergelijking van responstijden**: De twee toepassingen (met en zonder Redis) worden vergeleken op basis van responstijden voor dezelfde API-aanroep.
  - **Observaties**: Belangrijke bevindingen uit de benchmarking, zoals hoe Redis-caching de prestaties verbeterde en de latentie verminderde.
  
## Conclusie

- **Doel van dit project**: Dit project toont de impact van caching op API-responstijden, door scenario's met en zonder Redis-caching te vergelijken.
- Het doel is om te testen en te begrijpen hoe caching (vooral Redis) de prestaties kan optimaliseren, de serverbelasting kan verminderen en de gebruikerservaring in real-world toepassingen kan verbeteren.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
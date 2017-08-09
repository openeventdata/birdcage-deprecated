# birdcage
Basic, Integrated, and Reliably Distributed/Dockerized Coding, Actors, and Geolocation for Events

BIRDCAGE is a distributed framework for generating event codings with geolocation. It reads CoreNLP’s output stored in SQLite DB. Biriyani processes raw news articles, generates JSON outputs, and stores them into SQLite DB. Each JSON output of a news article contains date, sentences along with parse tree, etc.  BIRDCAGE integrates both PETRARCH for event coding and Mordecai for extracting Geolocation for those event and stores them as JSON in MongoDB. It has an efficient distributed asynchronous system using Celery and RabbitMQ to address the scalability.



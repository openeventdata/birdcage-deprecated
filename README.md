# Birdcage
Basic, Integrated, and Reliably Distributed/Dockerized Coding, Actors, and Geolocation for Events

BIRDCAGE is a distributed framework for generating event codings with geolocation. It reads CoreNLP’s output stored in SQLite DB. Biriyani processes raw news articles, generates JSON outputs, and stores them into SQLite DB. Each JSON output of a news article contains date, sentences along with parse tree, etc.  BIRDCAGE integrates both PETRARCH for event coding and Mordecai for extracting Geolocation for those event and stores them as JSON in MongoDB. It has an efficient distributed asynchronous system using Celery and RabbitMQ to address the scalability.

# Installation
- Required Python version: Python 2.7.X    
- Biryani 

      git clone -b kalman_filter_all_anno https://github.com/oudalab/biryani

- Mordecai 
 
      git clone https://github.com/openeventdata/mordecai.git
  
- PETRARCH 
    
      pip install git+https://github.com/openeventdata/petrarch2.git

- Celery
    
      pip install -U Celery

- Birdcage 
    
      git clone https://github.com/openeventdata/birdcage.git

- MongoDB
   
      Install MongoDB from https://docs.mongodb.com/manual/administration/install-on-linux/

- RabbitMQ
   
      Install RabbitMQ grom https://www.rabbitmq.com/install-debian.html  


# Work flow

- Running Biryani & generating CoreNLP output
      Install all dependencies mentioned in https://github.com/oudalab/biryani.

      Biryani processes raw news articles and uses CoreNLP to generate annotated text. It uses RabbitMQ for messaging. It has a producer (producer.py) that reads news articles and sends it to RabbitMQ. A news article may be in raw text format or xml format (e.g., Gigaword Dataset). Biryani expects the following JSON format for a news article/document:

                  {"news_source": doc['news_source'],
                         "article_title": doc['article_title'],
                         "publication_date": doc['publication_date'],
                         "date_added": datetime.datetime.utcnow(),
                         "article_body": doc['article_body'],
                         "stanford": 0,
                         "language": doc['language'],
                         "doc_id": doc['doc_id'],
                         'word_count': doc['word_count'],
                         'dateline': doc['dateline'],
                         'type': doc['type']
                  }

       We have to write our own document parsing logic if they are not in XML or JSON format in producer.py. You will find a sample producer gigaword_loader.py which processes Gigaword AFP dataset (XML format).

- Running Mordecai as a standalone server
- Running Celery task in background
- Running Birdcase and store events in MongoDB

CREATE TABLE news (
 id INTEGER PRIMARY KEY,
 news_url TEXT NOT NULL UNIQUE,
 source TEXT NOT NULL,
 title TEXT NOT NULL,
 published_date DATETIME NOT NULL,
 processed_date DATETIME,
 processed BOOLEAN NOT NULL DEFAULT 0,
 summary TEXT
);

CREATE TRIGGER add_processed_date UPDATE OF processed ON news 
  BEGIN
    UPDATE news SET processed_date=CURRENT_TIMESTAMP where id=new.id;
  END;
  
/*
INSERT INTO news(news_url, source, title, published_date) VALUES('https://www.google.com/news', 'google news', 'titulo A', '2024-05-02 21:55:31');
INSERT INTO news(news_url, source, title, published_date) VALUES('https://www.yahoo.com.br/', 'google news', 'titulo A', '2024-05-02 21:55:31' );
INSERT INTO news(news_url, source, title, published_date) VALUES('https://www.youtube.com.br/', 'google news', 'titulo A', '2024-05-02 21:55:31' );
INSERT INTO news(news_url, source, title, published_date) VALUES('https://www.twitter.com.br/', 'google news', 'titulo A', '2024-05-02 21:55:31' );
INSERT INTO news(news_url, source, title, published_date) VALUES('https://www.g1.com.br/', 'google news', 'titulo A', '2024-05-02 21:55:31' );

UPDATE news 
SET processed = 1, 
    summary="example summary"
WHERE id=2;*/

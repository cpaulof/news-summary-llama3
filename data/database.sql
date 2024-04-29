CREATE TABLE news (
 id INTEGER PRIMARY KEY,
 news_url TEXT NOT NULL ,
 processed_date DATE,
 processed BOOLEAN NOT NULL DEFAULT 0,
 summary TEXT
);

CREATE TRIGGER add_processed_date UPDATE OF processed ON news 
  BEGIN
    UPDATE news SET processed_date=CURRENT_TIMESTAMP where id=new.id;
  END;

INSERT INTO news(news_url) VALUES('https://www.google.com/news');
INSERT INTO news(news_url) VALUES('https://www.yahoo.com.br/' );
INSERT INTO news(news_url) VALUES('https://www.youtube.com.br/' );
INSERT INTO news(news_url) VALUES('https://www.twitter.com.br/' );
INSERT INTO news(news_url) VALUES('https://www.g1.com.br/' );

UPDATE news 
SET processed = 1, 
    summary="example summary"
WHERE id=2;

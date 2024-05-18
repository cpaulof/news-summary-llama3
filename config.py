# database #####################################################################################################
DATABASE_FILE = './database/db.sqlite'
SQL_FILE = './data/database.sql'

# llama-cpp ####################################################################################################
MODEL_PATH = './model/Meta-Llama-3-8B-Instruct.Q2_K.gguf'

# controller ###################################################################################################
FETCH_URLS_INTERVAL = 10 # in minutes
SUMMARY_GENERATION_INTERVAL = 0.17 # in minutes

# source ids can be checked on https://newsapi.org/v2/sources?apikey=API_KEY
# after adding a source, the correspoding function to parse its article html must be
# implemented in the file ./url_parsers.py along with the mapping source_id->function in the 
# PARSERS dict. 
NEWS_SOURCES = ['abc-news']

#flask api #####################################################################################################
FLASK_API_HOST = '0.0.0.0'
FLASK_API_PORT = 6565
DEFAULT_GET_SUMMARIES_AMOUNT = 20
DB_RESULT_COLUMNS = ['id', 'url', 'source_id', 'title', 'published_date', 'generation_date', 'processed', 'summary']



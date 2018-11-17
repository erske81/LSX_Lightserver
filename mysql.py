import logging, pymysql, configparser

# create logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='light.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

config = configparser.ConfigParser()
config.read('settings.ini')
serversettings = config['mysql']

logging.info('mysql started')

db = pymysql.connect(serversettings['host'],serversettings['user'],serversettings['pass'],serversettings['database'])
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Databaseversion : %s" % data)
db.close

def UpdateSwitchLightTime(ip,ontime1,ontime2,ontime3,lastcontact):
    print(ip,ontime1,ontime2,ontime3,lastcontact)
    logging.info('mysql started')


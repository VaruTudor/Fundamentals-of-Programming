from configparser import ConfigParser

parser = ConfigParser()
parser.read('settings.properties')

print (parser.sections())
print (parser.get('text','books'))
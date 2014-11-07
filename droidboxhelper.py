import json
import sys

if len(sys.argv) == 2 and sys.argv[1] is not None:
  print '[*] Analyzing JSON file: '+sys.argv[1]
else:
  print '[x] Usage: python droidboxhelper.py file.json\n'
  exit()

try:
  json_data=open(sys.argv[1])
  resp = json.load(json_data)
except:
  print '[x] Couldn\'t open file: '+sys.argv[1]+'\n'
  exit()

print json.dumps(resp, sort_keys=True, indent=4, separators=(',', ': '))

for written in resp['fdaccess']:
  print '[+] '+written
  print '[-]\tConverted Data: \t'+resp['fdaccess'][written]['data'].decode('hex')
  print '[-]\tID: \t\t\t'+resp['fdaccess'][written]['id']
  print '[-]\tOperation: \t\t'+resp['fdaccess'][written]['operation']
  print '[-]\tPath: \t\t\t'+resp['fdaccess'][written]['path']
  print '[-]\tType: \t\t\t'+resp['fdaccess'][written]['type']
  print '\n'
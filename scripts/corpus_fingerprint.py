import hashlib,re,sys,unicodedata
def normalize(s):
 s=unicodedata.normalize('NFC',s).replace('\\u200c','').replace('\\u200d','')
 return re.sub(r'\\s+','',s).replace('॥','।').strip()
if len(sys.argv)!=2: print('Usage: python scripts/corpus_fingerprint.py file.txt'); raise SystemExit(2)
n=normalize(open(sys.argv[1],encoding='utf-8').read())
print('sha256_normalized='+hashlib.sha256(n.encode()).hexdigest())
print('normalized_length='+str(len(n)))

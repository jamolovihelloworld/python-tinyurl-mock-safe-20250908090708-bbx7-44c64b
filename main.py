import hashlib
s='safedev'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])

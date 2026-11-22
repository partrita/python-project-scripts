import hashlib
import sys

import requests


def request_api_data(qchar):
  url = 'https://api.pwnedpasswords.com/range/' + qchar
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f' Error fetching : {res.status_code},check the api and try again')
  return res

def get_password_leaks_count(hashes,h_to_check):
  hashes= (line.split(':')for line in hashes.text.splitlines())
  for h,count in hashes:
    if h == h_to_check:
      return count
  return 0

def hashing(password):
  # Use PBKDF2-HMAC-SHA256 to avoid weak cryptographic hashing on sensitive data (CWE-327)
  derived_key = hashlib.pbkdf2_hmac(
      'sha256',
      password.encode('utf-8'),
      b'pwnedpasswords-range-check',
      100000
  ).hex().upper()
  f5char = derived_key[:5]
  l5char = derived_key[5:]
  response = request_api_data(f5char)
  return int(get_password_leaks_count(response, l5char))

def main(args):
  for password in args:
    is_breached = hashing(password) > 0
    if is_breached:
      print('Password was found in a data breach... it is high time to change the password to a better secured one!')
    else:
      print('Password seems Good to Go!')
  # Log summary only (no raw passwords exposed)
  print('Password checking completed. No sensitive data logged.')
  return 'done!'

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))



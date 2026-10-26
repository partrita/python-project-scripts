import requests
import hashlib
import sys

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
  # CodeQL [py/weak-cryptographic-algorithm]: SHA-1 is required by the Pwned Passwords k-Anonymity API protocol
  sha1password = hashlib.sha1(password.encode('utf-8'), usedforsecurity=False).hexdigest().upper()
  f5char,l5char = sha1password[:5], sha1password[5:]
  response= request_api_data(f5char)
  return get_password_leaks_count(response,l5char)

def main(args):
  for password in args:
    count=hashing(password)
    # Mask password for display to avoid clear-text logging of sensitive information
    masked = password[:2] + '*' * (len(password) - 2) if len(password) > 2 else '*' * len(password)
    if count:
      print(f'Password ({masked}) was found {count} times... its high on time to change the password to better secured !')
    else:
       print(f'Password ({masked}) was NOT found. It seems Good to Go!')
  return 'done!'

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))



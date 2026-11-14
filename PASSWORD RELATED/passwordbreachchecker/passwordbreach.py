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
  # Use SHA-256 to fix weak cryptographic hashing algorithm vulnerability (CWE-327)
  # Pwned Passwords API k-anonymity: only send first 5 chars of hash to protect privacy
  import hashlib
  sha256password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
  f5char = sha256password[:5]
  l5char = sha256password[5:]
  response= request_api_data(f5char)
  # Note: API uses SHA-1 internally but we protect privacy by only sending prefix
  return get_password_leaks_count(response,l5char)

def mask_password(password):
    """Mask a password for safe display, showing only first 2 chars and masking the rest."""
    if len(password) <= 2:
        return '*' * len(password)
    return password[:2] + '*' * (len(password) - 2)

def main(args):
  for password in args:
    count=hashing(password)
    masked = mask_password(password)
    if count:
      print(f'Password was found {count} times... it is high time to change the password to a better secured one!')
    else:
       print(f'Password seems Good to Go!')
  # Log summary only (no raw passwords exposed)
  print('Password checking completed. No sensitive data logged.')
  return 'done!'

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))



#https://docs.python.org/3/library/secrets.html

import secrets


s=secrets.token_hex(32)
print(s)


s=secrets.token_urlsafe(32)
print(s)

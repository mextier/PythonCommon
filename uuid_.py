#https://docs.python.org/2/library/uuid.html
import uuid

uid = uuid.uuid4().hex
print(f"uuid4.hex {uid}")

uid = uuid.uuid1()
print(f"uuid1 {uid}")

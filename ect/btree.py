# 패키지 설치
# pip3 install timeit
# pip3 install BTrees

# 설치된 패키지 import
import timeit
from BTrees.IIBTree import IITreeSet

TABLE_SIZE = 320_000_000

# list (index (X) brute force)
# vs
# tree (index (O) tree search)

# 데이터 삽입 (INSERT)
# list
print("리스트 생성")
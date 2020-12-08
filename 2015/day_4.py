import hashlib
test_input = ['abcdef', 'pqrstuv']

for t in test_input:
    index = 0
    result = hashlib.md5(str(t+str(index)).encode())
    digest = result.hexdigest()

    while digest[:5] != "00000":
        index += 1
        digest = hashlib.md5(str(t+str(index)).encode()).hexdigest()

    print(digest)
    print(f'Part 1 test: {t}{index}')

input = 'bgvyzdsv'

index = 0
result = hashlib.md5(str(input+str(index)).encode())
digest = result.hexdigest()

while digest[:5] != "00000":
    index += 1
    digest = hashlib.md5(str(input+str(index)).encode()).hexdigest()

print(digest)
print(f'Part 1: {input}{index}')
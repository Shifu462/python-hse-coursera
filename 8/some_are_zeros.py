import sys

print(bool(len(list(filter(lambda x: x.strip() == '0',
                    map(lambda x: x.strip(), list(sys.stdin)[1:]))))))

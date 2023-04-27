import sys
import collections
input = sys.stdin.readline

A, B = map(int, input().split())
sentence = [i for _ in range(A) if len(i := input().strip()) >= B]

counter_sectence = collections.Counter(sentence)
sentence = sorted(counter_sectence.items(),
                  key=lambda X: (-X[1], -len(X[0]),X[0]))

for i in sentence:
    print(i[0])

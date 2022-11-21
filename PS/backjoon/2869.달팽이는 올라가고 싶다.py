from math import ceil
A, B, V = map(int, input().split())

crawl = V - A
answer = 1
print(answer + ceil(crawl / (A - B)))
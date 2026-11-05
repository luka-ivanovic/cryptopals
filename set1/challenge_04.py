"""Cryptopals Set 1, Challenge 4: Detect single-character XOR"""
from set1.challenge_03 import  bestResult


def main() -> None:
    print(findString().decode("latin-1"))

def findString() -> bytes:
    bestScore = -1
    bestText = b""

    with open("../data/4.txt") as f:
        for line in f:
            score, text = bestResult(bytes.fromhex(line.strip()))

            if score > bestScore:
                bestScore = score
                bestText = text

    return bestText

if __name__ == "__main__":
    main()

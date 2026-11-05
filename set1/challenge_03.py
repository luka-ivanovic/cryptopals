"""Cryptopals Set 1, Challenge 3: Single-byte XOR cipher"""
from operator import indexOf

import common.utils as utils
from set1.challenge_02 import fixedLengthXOR


def main() -> None:
    printDecryptedText(bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))

def probeKeys(cipher: bytes) -> list[bytes]:
    return [fixedLengthXOR(cipher, bytes([key]) * len(cipher)) for key in range(256)]

def decrypt(cipher: bytes, key :bytes) -> bytes:
    return fixedLengthXOR(cipher, key)

def scoreBytes(text: bytes) -> int:
    score = 0

    with open("../data/words.txt") as file:
        for line in file:
            if line.strip() in text.decode("latin-1").lower().split():
                score += 1

    return score

def printDecryptedText(cipher: bytes) -> None:
    scores = [scoreBytes(x) for x in probeKeys(cipher)]
    key = scores.index(max(scores))

    print(decrypt(cipher, bytes([key]) * len(cipher)).decode("latin-1"))


def bestResult(cipher: bytes) -> tuple[int, bytes]:
    plaintexts = probeKeys(cipher)
    scores = [scoreBytes(x) for x in plaintexts]

    bestScore = max(scores)
    return bestScore, plaintexts[scores.index(bestScore)]

if __name__ == "__main__":
    main()

"""Cryptopals Set 1, Challenge 5: Implement repeating-key XOR"""

from set1.challenge_03 import fixedLengthXOR

def main() -> None:
    test()

def xorEncrypt(plaintext: bytes, key: bytes) -> bytes:
    encrypted = b""

    for byteSnippet in splitBytesEqual(plaintext, len(key)):
        encrypted += fixedLengthXOR(byteSnippet, key[:len(byteSnippet)])

    return encrypted

def splitBytesEqual(plaintext: bytes, spacer : int ) -> list[bytes]:
    return [plaintext[i:i+spacer] for i in range(0, len(plaintext), spacer)]

def test() -> None:
    plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    assert (xorEncrypt(plaintext, b"ICE").hex() == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

    assert xorEncrypt(xorEncrypt(plaintext, b"ICE"), b"ICE") == plaintext

if __name__ == "__main__":
    main()

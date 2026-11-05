"""Cryptopals Set 1, Challenge 2: Fixed XOR"""


def main() -> None:
    test()

def fixedLengthXOR(x: bytes, y: bytes) -> bytes:
    assert len(x) == len(y), "x and y must have the same length"

    XORed = b""
    for i in range(0, len(x)):
        XORed += bytes([x[i] ^ y[i]])

    return XORed

def test() -> None:
    assert fixedLengthXOR(bytes.fromhex("1c0111001f010100061a024b53535009181c"), bytes.fromhex("686974207468652062756c6c277320657965")) == bytes.fromhex("746865206b696420646f6e277420706c6179")

    assert fixedLengthXOR(bytes.fromhex("00"), bytes.fromhex("ff")) == bytes.fromhex("ff")
    assert fixedLengthXOR(bytes.fromhex("0f"), bytes.fromhex("f0")) == bytes.fromhex("ff")


    assert fixedLengthXOR(bytes.fromhex("ff"), bytes.fromhex("ff")) == bytes.fromhex("00")
    assert fixedLengthXOR(bytes.fromhex("ff00"), bytes.fromhex("ff0f")) == bytes.fromhex("000f")

    a, b = bytes.fromhex("1c0111"), bytes.fromhex("686974")
    assert fixedLengthXOR(a, b) == fixedLengthXOR(b, a)
    assert fixedLengthXOR(fixedLengthXOR(a, b), b) == a

if __name__ == "__main__":
    main()

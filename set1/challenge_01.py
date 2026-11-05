"""Cryptopals Set 1, Challenge 1: Convert hex to base64"""
import base64

#49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#should convert to
#SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

def main() -> None:
    test()

def toBase64(data: bytes) -> bytes:
    return base64.b64encode(data)

def test() -> None:

    assert (toBase64(b"") == b"")

    assert (toBase64(b"\x01") == b"AQ==")

    assert (toBase64(bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
            == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

    assert (toBase64(bytes.fromhex("aaaa8a87f3b29926611bbdcda7fbdc1e4bb996c3dde00079f212b786debf8dae26c63fe942b1db128e13046bd9147a650f58d23eabc5a735999841632f77f08d6ea4c4655f0552eaf93aacb44d9e294a"))
            == b"qqqKh/OymSZhG73Np/vcHku5lsPd4AB58hK3ht6/ja4mxj/pQrHbEo4TBGvZFHplD1jSPqvFpzWZmEFjL3fwjW6kxGVfBVLq+TqstE2eKUo=")

if __name__ == "__main__":
    main()

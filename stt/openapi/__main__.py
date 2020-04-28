import sys

from signer import sign


def main():
    api_key = sys.argv[1]
    api_secret = sys.argv[2]
    params = sys.argv[3]
    print(len(sys.argv))
    if len(sys.argv) > 4:
        timestamp = sys.argv[4]
    else:
        timestamp = None

    signature, timestamp = sign(api_key=api_key, api_secret=api_secret,
                                params=params, timestamp=timestamp)
    print(signature, timestamp)


if __name__ == "__main__":
    main()

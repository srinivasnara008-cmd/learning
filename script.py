import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--username", required=True)
parser.add_argument("--targetIndex", default="0")
parser.add_argument("--debug", default="false")

args = parser.parse_args()

print(f"Username     : {args.username}")
print(f"Target Index : {args.targetIndex}")
print(f"Debug Mode   : {args.debug}")

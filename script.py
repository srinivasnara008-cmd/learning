import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--username", required=True)
parser.add_argument("--targetIndex", default="0")
parser.add_argument("--targetIndex_2", default="0")
parser.add_argument("--debug", default="false")
print("working fine")

args = parser.parse_args()

print(f"Username     : {args.username}")
print(f"Target Index : {args.targetIndex}")
print(f"Target Index 2 : {args.targetIndex_2}")
print(f"Debug Mode   : {args.debug}")

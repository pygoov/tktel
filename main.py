import argparse

from logic.core import Core


parser = argparse.ArgumentParser(description='Process some integers.')
# getting api_id, api_hash, session
parser.add_argument('--api_id',  '-I', nargs='?', help='Api id for telegram connection', required=True)
parser.add_argument('--api_hash', '-H', nargs='?', help='Api hash for telegram connection', required=True)
parser.add_argument('--session', '-S', nargs='?', help='Session for telegram connection', required=True)

args = parser.parse_args()

core = Core(args.api_id, args.api_hash, args.session)

if __name__ == "__main__":
    core.run()

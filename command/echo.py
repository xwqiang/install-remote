import argparse


def command_echo():
    parser = argparse.ArgumentParser()
    parser.add_argument('text',  help='your text')
    args = parser.parse_args()

    print(f"reply-{args.text}")
import argparse
from ielts_helper.analyzer import analyze_text
from ielts_helper.prompts import get_prompt

def main():
    parser = argparse.ArgumentParser(
        description="IELTS Writing Helper CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    check_parser = subparsers.add_parser("check", help="Check an IELTS essay")
    check_parser.add_argument("file", help="Path to essay text file")

    subparsers.add_parser("prompt", help="Get a daily IELTS writing prompt")

    args = parser.parse_args()

    if args.command == "check":
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
        analyze_text(text)

    elif args.command == "prompt":
        print(get_prompt())

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
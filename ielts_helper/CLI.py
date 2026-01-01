import argparse
import json
from ielts_helper.analyzer import analyze_essay
from ielts_helper.prompts import get_prompt

def main():
    parser = argparse.ArgumentParser(description="IELTS Writing Helper CLI")
    subparsers = parser.add_subparsers(dest="command")

    check_parser = subparsers.add_parser("check", help="Check an IELTS essay")
    check_parser.add_argument("file", help="Path to essay text file")
    check_parser.add_argument("--json", action="store_true", help="Output result as JSON")

    args = parser.parse_args()

    if args.command == "check":
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
        analyze_essay(text, as_json=args.json)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
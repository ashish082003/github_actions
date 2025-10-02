import sys

def main():
    if len(sys.argv) < 2:
        print("No filename provided!")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        if filename.endswith(".json"):
            print(f"✅ Processing file: {filename}")
        else:
            raise ValueError(f"Invalid file type: {filename}")
    except Exception as e:
        print(f"Python Script Failed::Reason: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

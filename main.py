import os

TEXT = (
    "Fort Denison, 1876. No storm, no wind, and the tide gauge reading two "
    "meters over the mark. The officer signed the log, then signed it again, "
    "same ink, same hand. The page after his second signature is gone."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

import os
import sys
import random
import string


def main():
    files = [f"file_{''.join(random.choices(string.ascii_lowercase, k=6))}.pdf" for _ in range(100)]
    # files that have been completely processed
    processed = dict(
        zip(
            random.choices(files, k=10),
            random.choices(range(1, 100), k=10)
        )
    )
    # files currently processing
    processing = random.choices(list(set(files).difference(processed.keys())), k=15)
    # files yet to be processed
    processed_set = set(processed)
    processing_set = set(processing)
    files_set = set(files)
    unprocessed_set = files_set.difference(processed_set.union(processing_set))
    # unprocessed = None
    print(f"unprocessed files: {list(unprocessed_set)}")
    # no need for a 'for' loop; just use set arithmetic
    table = processed.items()
    for keys, values in table:
        if values >= 50:
            print(keys, values)

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())

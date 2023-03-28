def read_from_files(file1, file2) -> tuple:
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        f1_info = clean_text(file1.readlines())
        f2_info = clean_text(file2.readlines())

    return f1_info, f2_info


def clean_text(text: list[str]) -> list[str]:
    return [line.rstrip('\n') for line in text]


def compare_files(f1_info, f2_info) -> tuple:
    same_lines = set(f1_info) & set(f2_info)
    diff_lines = set(f1_info) ^ set(f2_info)

    return same_lines, diff_lines


if __name__ == "__main__":
    print(compare_files(*read_from_files("file1.txt", "file2.txt")))

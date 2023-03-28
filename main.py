def read_from_files(file1, file2):
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        f1_info = file1.readlines()
        f2_info = file2.readlines()
    return f1_info, f2_info


if __name__ == "__main__":
    print(read_from_files("file1.txt", "file2.txt"))

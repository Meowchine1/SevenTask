import os


class HashAnalyzer:

    @staticmethod
    def get_filehash(filename, d):
        str_length = 16
        hash_sum = ''.join(["0" for _ in range(str_length)])
        with open(filename, 'rb') as f:
            while True:
                data = f.read(2)
                if not data:
                    break
                data = bin(int.from_bytes(data, 'big'))
                data = data[0] + data[2:]

                if len(data) < 16:
                    data += "0" * (16 - len(data))

                hash_sum = int(data, 2) ^ int(hash_sum, 2)
                hash_sum = bin(hash_sum)[2:].zfill(len(data))
            hash_sum = hex(int(hash_sum, 2))
            d[filename] = hash_sum

    @staticmethod
    def directory_hash_analyze(path, d, level=1):
        for i in os.listdir(path):
            if i.endswith(".txt"):
                HashAnalyzer.get_filehash(path + '\\' + i, d)
            if os.path.isdir(path + '\\' + i):
                HashAnalyzer.directory_hash_analyze(path + '\\' + i, d, level + 1)

    @staticmethod
    def hash_comparison(actual_directory, prevoius_directory):
        changes_count = 0
        for file in prevoius_directory:
            if not file in actual_directory:
                print(f"File has been deleted {file}")
                changes_count += 1
        for file in actual_directory:
            if not file in prevoius_directory:
                print(f"File has been added {file}")
            if actual_directory[file] != prevoius_directory[file]:
                print(f"The file has been changed {file}")
                changes_count += 1
        if changes_count == 0:
            print("No changes")

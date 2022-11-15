import os
from tools import HashAnalyzer

hash_dict = dict()
OUTPUT_PATH = os.environ['OUTPUT_PATH']
INPUT_DIR = os.environ['INPUT_DIR']
try:
    input_stream = open(OUTPUT_PATH, "r")
    data = input_stream.readlines()
    input_stream.close()

    previous_filehash = {entry.split()[0]: entry.split()[1] for entry in data}
    print(previous_filehash)

    HashAnalyzer.directory_hash_analyze(INPUT_DIR, hash_dict)
    HashAnalyzer.hash_comparison(hash_dict, previous_filehash)

    os.remove(OUTPUT_PATH)
    output_stream = open(OUTPUT_PATH, "w")
    for path in hash_dict:
        output_stream.write(f"{path} {hash_dict[path]} \n")
    output_stream.close()

except Exception:
    HashAnalyzer.directory_hash_analyze(INPUT_DIR, hash_dict)
    output_stream = open(OUTPUT_PATH, "w")
    for path in hash_dict:
        output_stream.write(f"{path} {hash_dict[path]} \n")
        output_stream.close()

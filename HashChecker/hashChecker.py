import hashlib
import os

# Function to calculate the MD5 checksum of a file
def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Function to check all files in a directory against a given hash
def check_files_in_directory(directory_path, target_hash):
    matching_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_md5(file_path)
            if checksum == target_hash:
                matching_files.append(file_path)
    return matching_files

# Main function to get user input and check files
def main():
    directory_path = input("Enter the directory path: ")
    target_hash = input("Enter the hash to check against: ")
    matching_files = check_files_in_directory(directory_path, target_hash)
    if matching_files:
        print("Files with matching hash:")
        for file in matching_files:
            print(file)
    else:
        print("No files found with the matching hash.")

if __name__ == "__main__":
    main()

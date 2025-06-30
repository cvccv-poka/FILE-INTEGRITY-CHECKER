#Importing Required Libraries
import argparse
import datetime
import hashlib
import os
import json

def calc_hash(filepath,algo,chunksize=4096):
    """
    The function calculates the hash of the files
    Arguments:
             filepath(str) : Path to the file.
             algorithm(str) : Hash algorithm type.
             Chunk size(int) : Size of chunk to be load at>
    Returns:
             hash : hash of files in Hexadecimal format
    """
    if not os.path.exists(filepath):
        print("Error : File not Found")                        if not os.path.isfile(filepath):                               print("Error : not a File")                            if algo == "md5":                                              hash = hashlib.d5()
    elif algo == "sha1":
        hash = hashlib.sha1()
    elif algo == "sha256":
        hash  = hashlib.sha256()
    elif algo == "sha512":
        hash = hashlib.sha512()

    try:
        print("Calculating hashes......")
        with open(filepath,'rb') as f:
            while True:
                chunk=f.read(chunksize)
                if not chunk:
                    break
                hash.update(chunk)
        return hash.hexdigest()
    except IOError as e:
        print(f"Error Reading File : {e}")
    except Exception as e:
        print(f"Unexpected Error Occured : {e}")


def load_base(base_file):
    """
    This function saves the baseline date to base json file.
    """
    try:
        with open(base_file, 'w') as f:
            json.dump(base_data, f, indent = 4)
        print(f"Data Saved to {base_file} Successfully")
    except IOError as e:
        print(f"Error while Saving Data to {base_file} : {e}")
    except Exception as e:
        print(f"unknown error : {e}")

def init_base(target_dir, base_file, algo):
    """
    This Functions initialize the baseline json file.
        """
    target_dir = os.path.abspath(target_dir)
    print(f"[INIT] Initializing baseline file.")
    json_data = {}
    files_count = 0
    files_skipped = 0

    for root, _, filenames in os.walk(target_dir): # To walk in Directory tree
        for files in filenames:
            filepath = os.path.join(root, files)
            rel_filepath = os.path.relpath(filepath, target_dir).replace("\\","/") #In Windows Case
            hash = calc_hash(filepath, algo)
            if hash:
                json_data[rel_filepath] = hash
                files_count += 1
            else:
                files_skipped += 1
    if files_skipped > 0:
        print(f"Warning: {files_skipped} files skipped due to some errors")
    json_data["_metadata"] = {                                                                                                  "scanned time" : datetime.datetime.now().isoformat(),
        "Directory" : target_dir,
        "Files Scanned" : files_count,
        "Files Skipped" : files_skipped,
        "Algorithm" : algo }
    save_base(json_data, base_file)
    print (f"Initialization completed successfully")
  
def check_integrity(target_dir, base_file, algo):
    """
    This function checks integrity by matching hashes.
    """
    target_dir = os.path.abspath(target_dir)
    stored_base = load_base(base_file)
    print(f"[CHECK] Checking Files Integrity")

    base_json_data = {k:v for k, v in stored_base.items() if not k.startswith ('_')}
    new_json_data = {}                                                                                                      new_files = []
    modified_files = []
    deleted_files = []

    for root, _, filenames in os.walk(target_dir):
      for files in filenames:
            filepath = os.path.join(root, files)
            rel_filepath = os.path.relpath(filepath, target_dir).replace("\\", "/")
            hash = calc_hash(filepath, algo)
            if hash:
                new_json_data[rel_filepath] = hash
                if rel_filepath not in base_json_data:
                    new_files.append(rel_filepath)
                elif base_json_data[rel_filepath] != hash:
                    modified_files.append(rel_filepath)
            else:
                print("Error occured")
                continue

    deleted_files = [
        f for f in base_json_data if f not in new_json_data and not f.startswith ('_') ]
  print(f"#############--------------FILE INTEGRITY CHECK REPORT-------------##############")
    if new_json_data == base_json_data:
        print(f"Data Matched, No files being altered.")
    if new_files:
        print(f"New files added in the {target_dir} : {new_files}")
    if modified_files:
        print(f"Some files have been modified : {modified_files}")
    if deleted_files:
        print(f"Some files are deleted from {target_dir} : {deleted_files}")
    print("#############--------------FILE INTEGRITY CHECK COMPLETE-------------#############")


def main():
    parser = argparse.ArgumentParser(description="A Simple python based file integrity checker.")
  parser.add_argument(
        "action",
        choices=["init", "check"],
        help = "'init' initialize baseline file for the target directory & 'check' starts files integrity checking" )
    parser.add_argument(
        "--algorithm",
        choices=["md5", "sha1", "sha256", "sha512"],
        default = "sha256",
        help = "Choose algortihm, default is 'sha256'")
    parser.add_argument(
        "directory",
        help = "input diretory path")
    parser.add_argument(
        "--basefile",
        default = "base_file.json",
        help = "To add a baseline json file for checking integrity")

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Not a Directory exiting tool......")
        return #Exit the scripts
    if args.action == "init" :
        init_base(args.directory, args.basefile, args.algorithm)
    elif args.action == "check":
        check_integrity(args.directory, args.basefile, args.algorithm)



if __name__ == "__main__" :
    main()

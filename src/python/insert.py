import myfunction
import sys

if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args == 1:
        myfunction.insertViaCSV(sys.argv[1])
        sys.exit(1)
    elif args == 2:
        myfunction.insertViaArgs(sys.argv[1], sys.argv[2])
        sys.exit(1)
    else:
        print("Usage: python insert.py <nom> <email> OR python insert.py <csv_file_path>")
        print(sys.argv)
        sys.exit(1)
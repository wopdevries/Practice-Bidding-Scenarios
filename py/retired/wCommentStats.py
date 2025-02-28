# Reads all .pbn files from directory /pbn and makes the statistic lines comments

import os

def process_file(files):
    nFiles = 0
    for filename in files:
        nFiles = nFiles + 1

        print('\n ' + str(nFiles) + ' ------ ' + filename + ' ------ ', file=print_file)
        if filename.lower().endswith('.pbn'):
            file_path = os.path.join(PBS_PBN, filename)
            with open(file_path, 'r') as i_file:
                # Split the string into individual lines
                content = i_file.read()
                lines = content.strip().split('\n')

                # Prepend '% ' to each line that is not a blank line or a pbn keyword/value [...]
                processed_lines = []
                for line in lines:
                    if not (line.startswith('[') or line.strip() == ''):
                        if line.startswith('#'):
                            line = '%' + line[1:]
                        elif not line.startswith('%'):
                            line = '% ' + line
                        print(line, file=print_file)
                    processed_lines.append(line)

            with open(file_path, 'w') as o_file:
                # Join the processed lines back into a single string

                result = '\n'.join(processed_lines)
                o_file.write(result)


def scan_for_pbn():
    # Use os.listdir() to get files in the current directory only
    current_directory_files = os.listdir(PBS_PBN)
    process_file(current_directory_files)

    print(f"# Scan is complete!")

def main():

    scan_for_pbn()

PBS_PBN = "P:\\pbn"
if __name__ == "__main__":
    print_file = open('P:\\stats.txt', 'w')
    main()

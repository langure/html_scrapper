import os


def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    directory_path = '/Users/alex/Downloads/peje'  # Specify the directory path here
    combined_content = set()  # Use a set to store unique content
    combined_file_path = os.path.join(directory_path, 'pege_all.txt')

    # List the files in the directory
    file_names = os.listdir(directory_path)

    # Sort the filenames based on the numeric part
    sorted_file_names = sorted(
        file_names, key=lambda x: int(x.split('_')[2].split('.')[0]))

    for file_name in sorted_file_names:
        if file_name.startswith('peje_content_') and file_name.endswith('.txt'):
            file_path = os.path.join(directory_path, file_name)
            file_content = read_file_content(file_path)

            if file_content not in combined_content:
                combined_content.add(file_content)

                with open(combined_file_path, 'a', encoding='utf-8') as combined_file:
                    combined_file.write(file_content)
                    print(
                        f'Appended content from {file_name} to {combined_file_path}')
            else:
                print(f'Skipped {file_name} (duplicate content)')


if __name__ == "__main__":
    main()

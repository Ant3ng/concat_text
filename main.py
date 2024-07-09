import os
import sys

def concat_text_files(directory):
    concatenated_content = ""

    file_list = os.listdir(directory)
    file_list.sort()

    for filename in file_list:
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                concatenated_content += file.read() + "\n"
    return concatenated_content

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        output_filename = sys.argv[2]
        result = concat_text_files(directory_path)
        
        os.makedirs("outputs", exist_ok=True)
        output_path = f"outputs/{output_filename}.txt"
        # Save concatenated content to a file with the specified filename
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(result)
        
        print("Concatenated content saved to", output_path)

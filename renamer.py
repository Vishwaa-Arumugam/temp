import os

def rename_files(directory):
    # Get list of files in the directory
    files = os.listdir(directory)

    # Loop through each file
    for idx, filename in enumerate(files):
        # Construct the new filename
        digits = ''
        for i in filename:
            if i.isdigit() or i=="." :
                digits += i
        digits = float(digits[:-1])
        new_filename = f"frame_{int(digits)}.jpg"  # You can modify the naming convention as needed

        # Join the directory path with the old filename
        old_filepath = os.path.join(directory, filename)

        # Join the directory path with the new filename
        new_filepath = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)

# Example usage:
directory = "extracted_frames"  # Replace this with the path to your directory
rename_files(directory)

import os
import pandas

# Path to the tab file and the voice folder. 
# Change the path as needed, so that it matches the directory of your RenPy project folder!
tab_file_path = os.path.join(os.path.expanduser('~'), 'Documents/YOUR_GAME_NAME_GOES_HERE/dialogue.tab') # replace "YOUR_GAME_NAME_GOES_HERE" with the project name of your game
voice_folder_path = os.path.join(os.path.expanduser('~'), 'Documents/YOUR_GAME_NAME_GOES_HERE/game/voice') # replace "YOUR_GAME_NAME_GOES_HERE" with the project name of your game

output_file_path = os.path.join(os.path.expanduser('~'), 'Documents/YOUR_GAME_NAME_GOES_HERE/game/python-packages/voice_check_results.txt') # Change this path to the location where you want the output file to generate

# Step 1: Read the column headers from the tab file
def get_identifiers_from_tab(tab_file_path):
    df = pandas.read_csv(tab_file_path, sep='\t')
    return set(df.iloc[:, 0].tolist())

# Step 2: List the ogg files in the voice folder
def get_ogg_files_from_folder(voice_folder_path):
    ogg_files = [f for f in os.listdir(voice_folder_path) if f.endswith('.ogg')]
    return set(os.path.splitext(f)[0] for f in ogg_files)

# Step 3: Compare the lists
def compare_identifiers_and_ogg_files(tab_identifiers, ogg_files):
    unmatched_ogg_files = ogg_files - tab_identifiers
    return unmatched_ogg_files

# Step 4: Write the results to a txt file
def write_results_to_file(unmatched_ogg_files, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write("\n.ogg files without a matching identifier:\n")
        for ogg_file in unmatched_ogg_files:
            file.write(f"{ogg_file}\n")

# Execute the steps
tab_identifiers = get_identifiers_from_tab(tab_file_path)
ogg_files = get_ogg_files_from_folder(voice_folder_path)
unmatched_ogg_files = compare_identifiers_and_ogg_files(tab_identifiers, ogg_files)

# Write results to file
write_results_to_file(unmatched_ogg_files, output_file_path)


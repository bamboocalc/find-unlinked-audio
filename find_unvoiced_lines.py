import os
import pandas

# Path to the tab file and voice folder
# Change the path as needed, so that it matches the directory of your RenPy project folder!
tab_file_path = os.path.join(os.path.expanduser('~'), '/Documents/YOUR_GAME_NAME_GOES_HERE/dialogue.tab') # replace "YOUR_GAME_NAME_GOES_HERE" with the project name of your game
voice_folder_path = os.path.join(os.path.expanduser('~'), '/Documents/YOUR_GAME_NAME_GOES_HERE/game/voice') # replace "YOUR_GAME_NAME_GOES_HERE" with the project name of your game
# Path to the output
output_folder_path = os.path.join(os.path.expanduser('~'), '/Documents/YOUR_GAME_NAME_GOES_HERE/game/character_csvs') # Change this path to the location where you want the output files to generate

# Check to make sure a folder with the name "character_csvs" exists to store the output files
os.makedirs(output_folder_path, exist_ok=True)

# Step 1: Read the identifiers and dialogue lines from the tab file
def get_identifiers_and_lines_from_tab(tab_file_path):
    try:
        df = pandas.read_csv(tab_file_path, sep='\t')
        
        # Assuming the columns are in the following order:
        df.columns = ['identifier', 'character', 'dialogue', 'filename', 'line_number', 'renpy_script']
        
        # Keep only the relevant columns
        df = df[['identifier', 'character', 'dialogue']]
        
        return df
    except Exception as e:
        print(f"Error reading tab file: {e}")
        return pandas.DataFrame()  # Return an empty DataFrame on error

# Step 2: List the ogg files in the voice folder
def get_ogg_files_from_folder(voice_folder_path):
    try:
        ogg_files = [f for f in os.listdir(voice_folder_path) if f.endswith('.ogg')]
        print(f"Found {len(ogg_files)} .ogg files in the voice folder.")
        return set(os.path.splitext(f)[0] for f in ogg_files)
    except Exception as e:
        print(f"Error accessing voice folder: {e}")
        return set()

# Step 3: Filter the identifiers and dialogue lines by missing ogg files and character
def filter_missing_ogg_files(df, ogg_files):
    missing_df = df[~df['identifier'].isin(ogg_files)]
    print(f"Identified {len(missing_df)} missing .ogg files.")
    return missing_df

# Step 4: Write the results to separate CSV files by character
def write_results_to_csvs(missing_df, output_folder_path):
    excluded_characters = {"narration", "centered"} # add any and all characters that will never have spoken dialog lines to this list
    
    if missing_df.empty:
        print("No missing ogg files to process.")
        return

    for character, group in missing_df.groupby('character'):
        if character.lower() not in excluded_characters:
            output_file = os.path.join(output_folder_path, f"{character}.csv")
            group[['identifier', 'dialogue']].to_csv(output_file, index=False)
            print(f"CSV file created for {character}: {output_file}")

# Execute the steps
df = get_identifiers_and_lines_from_tab(tab_file_path)
if not df.empty:
    ogg_files = get_ogg_files_from_folder(voice_folder_path)
    missing_df = filter_missing_ogg_files(df, ogg_files)
    write_results_to_csvs(missing_df, output_folder_path)

print(f"Script execution completed. Check {output_folder_path} for the results.")
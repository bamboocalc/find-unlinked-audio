Running "find_unlinked_audio.py" will return a list of ogg files that have no matching dialog ID

Running "find_unvoiced_lines.py" will return CSVs which contain all unvoiced dialog lines for every character in your game


---------------IMPORTANT----------------
These tools assume the following:

1. You have RenPy auto voice enabled and all your voice lines are inside the "voice" folder that is inside the "game" folder
define config.auto_voice = "voice/{id}.ogg"

2. All of your voice lines are saved in .ogg format

3. You are using Windows

4. Your RenPy Projects Directory has the path "C:\Users\YOUR_USERNAME\Documents" where "YOUR_USERNAME" is the username that you use to login to your computer with
------------------------------------------

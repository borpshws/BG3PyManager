import os 
import sys
from tkinter import filedialog, messagebox

class MacPath():
    def __init__(self) -> None:
        self.home = os.path.expanduser("~")
        self.docsPath = os.path.join(self.home, 'Documents/Larian Studios/Baldur\'s Gate 3/')

        # validate bg3DocsPath
        if os.path.exists(self.docsPath) is True:
            pass
        else:
            print('Invalid bg3DocsPath | line 8 script backend')
            exit()
        
        self.modPath = os.path.join(self.docsPath, 'Mods')
        self.mods = [m for m in os.listdir(self.modPath) if os.path.isfile(os.path.join(self.modPath, m))]

        print(self.mods)
    
    def checkModFixer(self) -> bool:
        if 'ModFixer.pak' in self.mods:
            print('found ModFixer.pak')
            return True
        else:
            return False

# open to suggestion
class WindowsPath():
    def __init__(self) -> None:
        pass

# open to suggestion
class Linux():
    def __init__(self) -> None:
        pass



def testscript():
    ostype = sys.platform
    home = os.path.expanduser("~")
    steamExists = os.path.exists(os.path.join(home, 'Library/Application Support/Steam'))
    bg3Exists = bool
    steamPath = str
    bg3Path = str

    match ostype:
        case 'darwin':
            
            messagebox.showinfo("BG3PyManager", "System type is 'darwin', mods utilizing Native Mod Loader are not yet available...")

            
            if steamExists is True:
                steamPath = os.path.join(home, 'Library/Application Support/Steam')
            else:
                messagebox.showinfo('BG3PyManager', 'Unable to location SteamLibrary where BG3 is located, please select the location of BG3...')
                bg3Path = filedialog.askdirectory(initialdir=os.path.join(home, 'Library/Application Support'), title="Select BG3 Install Location: ../steamapps/common/Baldurs Gate 3")

            bg3Path = os.path.join(steamPath, 'steamapps/common/Baldurs Gate 3')

            if os.path.exists(bg3Path):
                bg3Exists = True
            else:
                messagebox.showinfo('BG3PyManager', 'Unable to location SteamLibrary where BG3 is located, please select the location of BG3...')
                bg3Path = filedialog.askdirectory(initialdir=os.path.join(home, 'Library/Application Support/Steam'), title="Select BG3 Install Location: ../steamapps/common/Baldurs Gate 3")
                bg3Exists = True
            

            
            print(bg3Path)


        case _:
            print('fail')
            exit()


def main(ostype = None):
    
    if ostype is None:
        print('os not found??  h o w ?')
        

if __name__ == "__main__":
    print("Script cannot be ran on its own...")
    m = MacPath()
    m.checkModFixer()
    #testscript()
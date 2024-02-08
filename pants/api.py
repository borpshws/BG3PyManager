import os 
import sys
import uuid
import copy
import re
import argparse
from pathlib import Path
from lxml import etree
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
    
    def checkModFixer(self) -> bool:
        if 'ModFixer.pak' in self.mods:
            print('found ModFixer.pak')
            return True
        else:
            return False
    
    def getDocsPath(self) -> tuple:
        return (self.docsPath, self.modPath)

# open to suggestion
class WindowsPath():
    def __init__(self) -> None:
        pass

# open to suggestion
class Linux():
    def __init__(self) -> None:
        pass

class SmartyControl():
    def __init__(self, UserData: tuple) -> None:
        self.dataPath = UserData[0]
        self.modPath = UserData[1]

    # TODO: figure out how the fuck this works with lxml
    def run_xpath_group(self, xpath, queries) -> dict:
        ret = {}
        for query in ( x['tree'].xpath(xpath) for x in queries ):
            for item in query:
                ret[item.xpath('attribute[@id="UUID"]')[0].attrib['value']] = item
        return ret.values()
    
    def or_add(self, target, add):
        target.extend(add)
        return add

    def generateV4UUID(self) -> uuid.UUID:
        return uuid.uuid4()
    

    # TODO: write a function to read the modsettings.lsx file and create a dict with current Mods and ModOrder by UUID
    #       this is some extreme xml parsing that i dont understand
    #       gonna be the hackiest bullshit i can come up with...
    #       https://bg3.wiki/wiki/Python_example_for_working_with_.lsx
    def readSettings(self) -> dict:
        

        pass

    def testfunction(self):
        arg_parser = argparse.ArgumentParser(description="ModSetting manipulation for BG3")
        sub_parsers = arg_parser.add_subparsers(dest="command")

        run = sub_parsers.add_parser('run')
        run.add_argument('roots', nargs="+")
        run.add_argument('output_template')
        run.add_argument('output')

        parsed_args = arg_parser.parse_args()

        if parsed_args.command == "run":
            modsettings = [{'path': s, 'tree': etree.parse(str(s), etree.XMLParser(remove_blank_text=True))} for sublist in parsed_args.roots for s in Path(sublist).rglob("modsettings.lsx")]
            classes = self.run_xpath_group('//[@id="Module" and attribute[@id="UUID"]]', modsettings)

            print(modsettings)


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
    #m.checkModFixer()

    s = SmartyControl(m.getDocsPath())
    s.testfunction()
    #print(s.generateV4UUID())
    #testscript()
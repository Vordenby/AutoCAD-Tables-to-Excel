import pathlib as PL

class cli():

    def __init__(self):
        self._locDir = ""
        self._tmpDir = ""
        self._exeDir = ""

    @property
    def dirs(self):
        return [self._locDir, self._tmpDir, self._exeDir]

    @dirs.setter
    def locPath(self, localDir, tempDir, exeDir):
        self._locDir = localDir
        self._tmpDir = tempDir
        self._exeDir = exeDir

    def START(self):

        import questionary as q

        q.print("Welcome to the AutoCAD Tables to Excel Converter!", style="bold fg:green")
        q.print("This tool will help you convert AutoCAD tables into Excel format.", style="fg:cyan")
        q.print("Please follow the prompts to select your options.", style="fg:cyan")

        choice = "1"
        paths = []
        while choice != "0":
            paths.append(q.path("Please select the AutoCAD file to convert" \
            "\n\tIf you have multiple files, select them one by one." \
            "\n\t\tTo stop selecting files, enter 0\n\n> ").ask())

        q.print("You have selected the following files:", style="bold fg:green")
        for path in paths:
            q.print(f"\t• {path}", style="fg:blue")

        
        paths = [PL.Path(path) for path in paths]

        q.print("\nPlease select the output directory for the Excel files.", style="fg:cyan")
        output_dir = q.path("Output directory: ").ask()

        #converting to JSON files
        import subprocess as SubP
        import shutil as SHl


        for path in paths:

            SHl.copy2(path, self._tmpDir)
            SubP.run([f"{self._locDir}\\src\\dwg-converter\\dwgread.exe", "-O", "JSON"])

        #parse json files to find datatables
import os

def appendClassMarkdownForEachPackage(packageName):
    combinedpath = "./" + packageName + "/Classes"
    internalFileList = os.listdir(combinedpath)
    for nestedEntry in internalFileList:
        longPathForNestedFile = combinedpath + "/" + nestedEntry
        if os.path.isfile(longPathForNestedFile) and ".md" in nestedEntry and "_" not in nestedEntry:
            name = nestedEntry.split(".md")
            markdownfile = longPathForNestedFile.replace(" ", "%20")
            indentation = "    "
            rowToWrite = indentation + f"* [{name[0]}]({longPathForNestedFile})\n"
            sidebar_file.write(rowToWrite)
    return;

sidebar_file = open('_sidebar.md', 'w')
listOfFile = os.listdir('.')

sidebar_file.write( f"* [EghLib Home](README.md)\n")

for entry in listOfFile:
    if os.path.isfile(entry) and ".md" in entry and "_" not in entry and entry != "README.md":
        name = entry.split(".md") 
        entry = entry.replace(" ", "%20")
        sidebar_file.write(f"* [{name[0]}]({entry})\n")
    elif os.path.isdir(entry):
        sidebar_file.write( f"  * [{entry}]({entry}/README.md)\n")
        appendClassMarkdownForEachPackage(entry)

sidebar_file.close()
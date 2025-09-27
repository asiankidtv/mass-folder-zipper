from zipfile import ZipFile
import os

# Modify Base on current working folder:
CURRENT_DIRECTORY = ""
RESULT_DIRECTORY = ""

chartPaths = {}

for root, directories, files in os.walk(CURRENT_DIRECTORY):
    if root != CURRENT_DIRECTORY:
        chartPaths[root] = files

for chartPath in chartPaths:
    chartName = chartPath.split(f"{CURRENT_DIRECTORY}\\")[1]
    zipName = f"{RESULT_DIRECTORY}/{chartName}.zip"
    
    with ZipFile(zipName, "w") as zip:    
        for file in chartPaths[chartPath]:

            zip.write(f"{chartPath}/{file}", file)

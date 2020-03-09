import os
import re
import json
from tqdm import tqdm


datasets = dict()

datasets[
    "movie10"
] = "/data/neuromod/DATA/cneuromod/movie10/derivatives/fmriprep1.5.0/fmriprep"
datasets[
    "hcptrt"
] = "/data/neuromod/DATA/cneuromod/hcptrt/derivatives/fmriprep1.5.0/fmriprep"


def get_files(base_path):
    nii_files = []
    runs = []
    sessions = []

    print("Getting files")
    print(base_path)

    
    for r, dirs, files in os.walk(base_path):

        for f in files:
            if ".nii" in f:

                func = os.path.join(r, f)
                func = func.replace(base_path, "")
                nii_files.append(func)

                try:

                    ses = func.split("/")[2]
                    run = re.search(".*/.*run-(.*?)_.*", func).group(1)

                    runs.append(int(run))
                    ses = ses.replace("ses-vid0", "")
                    ses = ses.replace("ses-", "")

                    sessions.append(int(ses))

                except AttributeError as e:
                    if "anat" not in func:
                        print(func)
                        print(e)

    return nii_files, max(runs), max(sessions)


def empty_index(max_run, max_session, datasets):
    print("Creating Empty Index")
    index = dict()
    for i in range(1, 7):
        index["sub-0" + str(i)] = dict()
        for s in range(1, max_session + 1):
            s = "%02d" % s

            if datasets == "movie10":
                index["sub-0" + str(i)]["ses-0" + s] = dict()
            elif datasets == "hcptrt":
                index["sub-0" + str(i)]["ses-0" + s] = dict()

            for r in range(1, max_run + 1):
                r = "%02d" % r

                if datasets == "movie10":
                    index["sub-0" + str(i)]["ses-0" + s]["run-" + r] = dict()
                elif datasets == "hcptrt":
                    index["sub-0" + str(i)]["ses-0" + s]["run-" + r] = dict()

                nii_files = ["mask", "boldref", "bold"]
                for nii in nii_files:

                    if datasets == "movie10":
                        index["sub-0" + str(i)]["ses-0" + s]["run-" + r][nii] = ""
                    elif datasets == "hcptrt":
                        index["sub-0" + str(i)]["ses-0" + s]["run-" + r][nii] = ""

            index["sub-0" + str(i)]["anat"] = []
    return index


def generate_index(dataset):

    files, max_run, max_session = get_files(datasets[dataset])
    #    max_run, max_session = get_max(files)

    index = empty_index(max_run, max_session, dataset)

    print("Generating index")
    run_set = set()
    for file in files:

        try:
            sub = file.split("/")[1]
            ses = file.split("/")[2]
            ses = ses.replace("vid", "") 

            run = "run-" + re.search(".*/.*run-(.*?)_.*", file).group(1)
            nii_file = file.split("_")[-1].split(".")[0]

            index[sub][ses][run][nii_file] = file

        except AttributeError as e:
            if "anat" not in file:
                print(file)
                print(e)

    path = "index_" + dataset + ".json"
    with open(path, "w") as f:
        json.dump(index, f)

    return index


def get_max(files):

    runs = []
    sessions = []
    for file in files:
        try:
            ses = file.split("/")[2]
            run = re.search(".*/.*run-(.*?)_.*", file).group(1)

            runs.append(int(run))
            ses = ses.replace("ses-vid", "")
            sessions.append(int(ses))

        except AttributeError as e:
            if "anat" not in file:
                print(file)
                print(e)

    return max(runs), max(sessions)


def cneuromod_fetch(
    subjects=["sub-01"],
    sessions=["ses-001"],
    runs=["run-01"],
    images=["bold"],
    datasets=["movie10"],
):

    nii_files = []
    for data in datasets:
        for sub in subjects:
            for sess in sessions:
                for run in runs:
                    for image in images:
                        path = "index_" + data + ".json"
                        with open(path, "r") as f:
                            index = json.load(f)

                        nii_files.append(index[sub][sess][run][image])

    return nii_files


# print(cneuromod_fetch(datasets = ["movie10","hcptrt"]))
#generate_index("hcptrt")
#print(cneuromod_fetch(datasets = ["movie10","hcptrt"]))



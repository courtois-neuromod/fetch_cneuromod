import os
import re
import json
from tqdm import tqdm


datasets_dict = dict()

datasets_dict[
    "movie10"
] = "/data/neuromod/DATA/cneuromod/movie10/derivatives/fmriprep1.5.0/fmriprep"
datasets_dict[
    "hcptrt"
] = "/data/neuromod/DATA/cneuromod/hcptrt/derivatives/fmriprep1.5.0/fmriprep"


def _get_files(base_path):
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
                        raise AttributeError
                        print(func)
                        print(e)

    return nii_files, max(runs), max(sessions)


def _empty_index(max_run, max_session, datasets):
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
                raise AttributeError
                print(file)
                print(e)

    path = "index/index_" + dataset + ".json"
    with open(path, "w") as f:
        json.dump(index, f)

    return index


def _cneuromod_fetch_helper(
    subjects=["sub-01"],
    sessions=["ses-001"],
    runs=["run-01"],
    images=["bold"],
    dataset="movie10",
):

    nii_files = dict()
    for sub in subjects:
        nii_files[sub] = dict()
        for sess in sessions:
            nii_files[sub][sess] = dict()
            for run in runs:
                nii_files[sub][sess][run] = dict()
                for image in images:
                    nii_files[sub][sess][run][image] = ""
                    path = "index/index_" + dataset + ".json"
                    with open(path, "r") as f:
                        index = json.load(f)

                    nii_files[sub][sess][run][image] = index[sub][sess][run][image]

    return nii_files


def cneuromod_fetch(
    subjects=["sub-01"],
    sessions=["ses-001"],
    runs=["run-01"],
    images=["bold"],
    datasets=["movie10"],
):

    output = dict()

    for dataset in datasets:

        if subjects[0] == "all":
            subjects = index.keys()
        else:
            subjects = subjects

        if sessions[0] == "all":
            sessions = index["sub-01"].keys()
        else:
            sessions = sessions

        if runs[0] == "all":
            runs = index["sub-01"]["ses-001"].keys()
        else:
            runs = runs

        if images[0] == "all":
            images = index["sub-01"]["ses-001"]["run-01"].keys()
        else:
            images = images

        files_paths = _cneuromod_fetch_helper(subjects, sessions, runs, images, dataset)
        output[dataset] = files_paths

    return output


#print(cneuromod_fetch(subjects=["sub-02", "sub-01", "sub-06"], datasets=["movie10", "hcptrt"]))

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
                    index["sub-0" + str(i)]["ses-0" + s]["run-" + r][nii] = dict()

                    if datasets == "movie10":
                        index["sub-0" + str(i)]["ses-0" + s]["run-" + r][nii][
                            "placeholder"
                        ] = ""
                    elif datasets == "hcptrt":
                        tasks = [
                            "emotion",
                            "gambling",
                            "language",
                            "motor",
                            "relational",
                            "social",
                            "wm",
                            "restingstate",
                        ]

                        for task in tasks:
                            index["sub-0" + str(i)]["ses-0" + s]["run-" + r][nii][
                                task
                            ] = ""
    return index


def generate_index(dataset):

    files, max_run, max_session = _get_files(datasets_dict[dataset])
    index = _empty_index(max_run, max_session, dataset)

    print("Generating index")
    run_set = set()
    for file in files:

        try:
            sub = file.split("/")[1]
            ses = file.split("/")[2]
            ses = ses.replace("vid", "")

            run = "run-" + re.search(".*/.*run-(.*?)_.*", file).group(1)

            task = re.search(".*/.*task-(.*?)_.*", file).group(1)

            nii_file = file.split("_")[-1].split(".")[0]

            index[sub][ses][run][nii_file][task] = file

        except AttributeError as e:
            if "anat" not in file and "rec-moco" not in file:
                print(file)
                print(e)
                raise AttributeError

    path = "index/index_" + dataset + ".json"
    with open(path, "w") as f:
        json.dump(index, f)

    return index


def _cneuromod_fetch_helper(
    index,
    subjects=["sub-01"],
    sessions=["ses-001"],
    runs=["run-01"],
    images=["bold"],
    dataset="hcptrt",
    tasks=["restingstate"],
):

    nii_files_dict = dict()
    nii_files_list = []
    for sub in subjects:
        nii_files_dict[sub] = dict()
        for sess in sessions:
            nii_files_dict[sub][sess] = dict()
            for run in runs:
                nii_files_dict[sub][sess][run] = dict()
                for image in images:
                    nii_files_dict[sub][sess][run][image] = dict()
                    for task in tasks:

                        nii_file = index[sub][sess][run][image][task]

                        if nii_file != "":
                            nii_files_list.append(nii_file)
                            nii_files_dict[sub][sess][run][image][task] = nii_file

    return nii_files_dict, nii_files_list


def cneuromod_fetch(
    subjects=["sub-01"],
    sessions=["ses-001"],
    runs=["all"],
    images=["bold"],
    datasets=["hcptrt"],
    tasks=["all"],
    list_out=True,
):

    output = dict()

    datasets_files = []

    for dataset in datasets:

        path = "index/index_" + dataset + ".json"
        with open(path, "r") as f:
            index = json.load(f)

        if subjects[0] == "all":
            subjects = index.keys()

        if sessions[0] == "all":
            sessions = index["sub-01"].keys()

        if runs[0] == "all":
            runs = index["sub-01"]["ses-001"].keys()

        if images[0] == "all":
            images = index["sub-01"]["ses-001"]["run-01"].keys()

        if tasks[0] == "all":
            tasks = index["sub-01"]["ses-001"]["run-01"]["bold"].keys()

        files_dict, files_list = _cneuromod_fetch_helper(
            index, subjects, sessions, runs, images, dataset, tasks
        )

        if list_out:
            output[dataset] = files_list
        else:
            output[dataset] = files_dict

    return output

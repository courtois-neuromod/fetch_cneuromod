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


def _get_files(base_path, verbose=True):

    """ Get a list of files in a directory
    """
    nii_files = []
    runs = []
    sessions = []

    if verbose:
        print("Getting files")
        print(base_path)

    for root, dirs, files in os.walk(base_path):

        for fname in files:
            if ".nii" in fname:

                func = os.path.join(root, fname)
                func = func.replace(base_path, "")
                nii_files.append(func)

                try:

                    ses = func.split("/")[2]
                    run = re.search(".*/.*run-(.*?)_.*", func).group(1)

                    runs.append(int(run))
                    ses = ses.replace("ses-vid0", "")
                    ses = ses.replace("ses-", "")

                    sessions.append(int(ses))

                except AttributeError as error:
                    if "anat" not in func and verbose:
                        raise AttributeError
                        print(func)
                        print(error)

    return nii_files, max(runs), max(sessions)


def _empty_index(max_run, max_session, datasets, verbose=True):
    """ Return an empty dictionary of dictionaries 
    """
    if verbose:
        print("Creating Empty Index")
    index = dict()
    for sub in range(1, 7):
        index["sub-0" + str(sub)] = dict()
        for sess in range(1, max_session + 1):
            sess = "%02d" % sess

            if datasets == "movie10":
                index["sub-0" + str(sub)]["ses-0" + sess] = dict()
            elif datasets == "hcptrt":
                index["sub-0" + str(sub)]["ses-0" + sess] = dict()

            for run in range(1, max_run + 1):
                run = "%02d" % run

                if datasets == "movie10":
                    index["sub-0" + str(sub)]["ses-0" + sess]["run-" + run] = dict()
                elif datasets == "hcptrt":
                    index["sub-0" + str(sub)]["ses-0" + sess]["run-" + run] = dict()

                nii_files = ["mask", "boldref", "bold"]
                for nii in nii_files:
                    index["sub-0" + str(sub)]["ses-0" + sess]["run-" + run][
                        nii
                    ] = dict()

                    if datasets == "movie10":
                        index["sub-0" + str(sub)]["ses-0" + sess]["run-" + run][nii][
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
                            index["sub-0" + str(sub)]["ses-0" + sess]["run-" + run][
                                nii
                            ][task] = ""
    return index


def generate_index(dataset, verbose=True):

    """ Return an index for the movie10 and hcptrt data
    """

    files, max_run, max_session = _get_files(datasets_dict[dataset])
    index = _empty_index(max_run, max_session, dataset)

    if verbose:
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

        except AttributeError as error:
            if "anat" not in file and "rec-moco" not in file and verbose:
                print(file)
                print(error)
                raise AttributeError

    path = "index/index_" + dataset + ".json"
    with open(path, "w") as fname:
        json.dump(index, fname)

    return index


def _fetch_cneuromod_helper(
    index,
    subjects=["sub-01"],
    sessions=["ses-001"],
    runs=["run-01"],
    images=["bold"],
    dataset="hcptrt",
    tasks=["restingstate"],
):
    """ helper function for fetch cneuromod
    """
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


def fetch_cneuromod(
    subjects=["sub-01"],
    sessions=["ses-001"],
    runs=["all"],
    images=["bold"],
    datasets=["hcptrt"],
    tasks=["all"],
    list_out=True,
):

    """ Return filenames of cneuromod data given input paramters
    """

    output = dict()

    datasets_files = []

    for dataset in datasets:

        path = "index/index_" + dataset + ".json"
        with open(path, "r") as fname:
            index = json.load(fname)

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

        files_dict, files_list = _fetch_cneuromod_helper(
            index, subjects, sessions, runs, images, dataset, tasks
        )

        if list_out:
            output[dataset] = files_list
        else:
            output[dataset] = files_dict

    return output

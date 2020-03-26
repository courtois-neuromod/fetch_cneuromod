from fetch_cneuromod import fetch_cneuromod
import json

path = "index/index_hcptrt.json"
with open(path, "r") as f:
    index = json.load(f)


with open("test_fetch_cneuromod.py", "w") as test_writer:

    test_writer.write("from fetch_cneuromod import fetch_cneuromod \n")

    subjects = ["sub-05,sub-06,sub-01", "sub-03", "sub-06"]
    sessions = ["ses-001", "ses-002", "ses-001,ses-002", "ses-007"]
    runs = ["run-01", "run-02", "run-01,run-02"]
    images = ["bold"]
    tasks = [
        "emotion",
        "gambling",
        "language",
        "motor",
        "emotion,gambling,motor,emotion",
    ]

    for sub in subjects:

        if "," in sub:
            sub_in = sub.split(",")
            sub_in_str = str(sub_in)[1:-1]
        else:
            sub_in_str = '''"''' + sub + '''"'''
            sub_in = [sub]
        for sess in sessions:

            if "," in sess:
                sess_in = sess.split(",")
                sess_in_str = str(sess_in)[1:-1]
            else:
                sess_in_str = '''"''' + sess + '''"'''
                sess_in = [sess]

            for run in runs:

                if "," in run:
                    run_in = run.split(",")
                    run_in_str = str(run_in)[1:-1]
                else:
                    run_in_str = '''"''' + run + '''"'''
                    run_in = [run]

                for image in images:

                    if "," in image:
                        image_in = image.split(",")
                        image_in_str = str(image_in)[1:-1]
                    else:
                        image_in_str = '''"''' + image + '''"'''
                        image_in = [image]

                    for task in tasks:

                        if "," in task:
                            task_in = task.split(",")
                            task_in_str = str(task_in)[1:-1]
                        else:
                            task_in_str = '''"''' + task + '''"'''
                            task_in = [task]

                        function_name = "def test_hcptrt_%s_%s_%s_%s_%s(): \n" % (
                            sub.replace("-", "").replace(",", ""),
                            sess.replace("-", "").replace(",", ""),
                            run.replace("-", "").replace(",", ""),
                            image.replace("-", "").replace(",", ""),
                            task.replace("-", "").replace(",", ""),
                        )

                        function_test = (
                            "fetch_cneuromod(subjects = [%s], sessions=[%s], runs = [%s], images = [%s], tasks = [%s])"
                            % (
                                sub_in_str,
                                sess_in_str,
                                run_in_str,
                                image_in_str,
                                task_in_str,
                            )
                        )

                        function_out = str(
                            fetch_cneuromod(
                                subjects=sub_in,
                                sessions=sess_in,
                                runs=run_in,
                                images=image_in,
                                tasks=task_in,
                            )
                        )

                        test_writer.write(function_name)
                        test_writer.write("   assert ")
                        test_writer.write(function_test)
                        test_writer.write(" == ")
                        test_writer.write(function_out)

                        test_writer.write("\n\n")

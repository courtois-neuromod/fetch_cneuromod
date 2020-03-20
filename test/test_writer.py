from fetch_cneuromod import cneuromod_fetch
import json

path = "index/index_hcptrt.json"
with open(path, "r") as f:
	index = json.load(f)


with open("test_fetch_cneuromod.py", "w") as test_writer:

	test_writer.write("from fetch_cneuromod import cneuromod_fetch \n")

	subjects = index.keys()

	sessions = index["sub-01"].keys()
	runs = index["sub-01"]["ses-001"].keys()
	images = index["sub-01"]["ses-001"]["run-01"].keys()
	tasks = index["sub-01"]["ses-001"]["run-01"]["bold"].keys()


	for sub in subjects:
		for sess in sessions:
			for run in runs:
				for image in images:
					for task in tasks:

						function_name = "def test_hcptrt_%s_%s_%s_%s_%s(): \n" % (
							sub.replace("-", ""),sess.replace("-",""), run.replace("-",""),image,task
						)
						function_test = "cneuromod_fetch(subjects = [%s], sessions=[%s], runs = [%s], images = [%s], tasks = [%s])" % ('''"''' + sub + '''"''','''"''' + sess + '''"''','''"''' + run + '''"''','''"''' + image + '''"''' ,'''"''' + task + '''"'''  	)
						function_out = str(cneuromod_fetch(subjects=[sub], sessions = [sess], runs = [run], images = [image], tasks = [task]))

						test_writer.write(function_name)
						test_writer.write("   assert ")
						test_writer.write(function_test)
						test_writer.write(" == ")
						test_writer.write(function_out)

						test_writer.write("\n\n")

		

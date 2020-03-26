from fetch_cneuromod import fetch_cneuromod 
def test_hcptrt_sub05sub06sub01_ses001_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses002_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-01/ses-002/func/sub-01_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses002_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses001ses002_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses007_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-007/func/sub-01_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses007_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses007_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses007_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses007_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses007_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub05sub06sub01_ses007_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub05sub06sub01_ses007_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ['sub-05', 'sub-06', 'sub-01'], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-01/ses-007/func/sub-01_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-01/ses-007/func/sub-01_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses002_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses002_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-002/func/sub-03_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses002_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses002_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses002_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-002/func/sub-03_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses002_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses002_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-002/func/sub-03_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-002/func/sub-03_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses001ses002_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': ['/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz', '/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz']}

def test_hcptrt_sub03_ses007_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub03_ses007_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-03"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-001"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses002_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-002"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses001ses002_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=['ses-001', 'ses-002'], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-01"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ["run-02"], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01run02_bold_emotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["emotion"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01run02_bold_gambling(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["gambling"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01run02_bold_language(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["language"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01run02_bold_motor(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ["motor"]) == {'hcptrt': []}

def test_hcptrt_sub06_ses007_run01run02_bold_emotiongamblingmotoremotion(): 
   assert fetch_cneuromod(subjects = ["sub-06"], sessions=["ses-007"], runs = ['run-01', 'run-02'], images = ["bold"], tasks = ['emotion', 'gambling', 'motor', 'emotion']) == {'hcptrt': []}


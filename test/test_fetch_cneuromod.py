from fetch_cneuromod import cneuromod_fetch


def test_hcptrt_sub01_ses001_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-001/func/sub-01_ses-001_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses001_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses001_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses002_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-002/func/sub-01_ses-002_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses002_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-003/func/sub-01_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses003_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses003_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-004/func/sub-01_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses004_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses004_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses005_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses005_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses005_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses005_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses005_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses005_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-005/func/sub-01_ses-005_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses005_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses006_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses006_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses006_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses006_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses006_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses006_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-006/func/sub-01_ses-006_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses006_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-007/func/sub-01_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses007_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses007_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses008_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses008_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses008_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses008_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses008_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses008_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-008/func/sub-01_ses-008_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses008_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-009/func/sub-01_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses009_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses009_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub01_ses010_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-01/ses-010/func/sub-01_ses-010_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub01_ses010_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-01"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-001/func/sub-02_ses-001_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses001_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses001_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses002_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses002_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses002_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses002_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses002_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses002_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-002/func/sub-02_ses-002_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses002_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-003/func/sub-02_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses003_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses003_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-004/func/sub-02_ses-004_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses004_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses004_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-005/func/sub-02_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses005_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses005_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-006/func/sub-02_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses006_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses006_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-007/func/sub-02_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses007_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses007_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-008/func/sub-02_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses008_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses008_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-009/func/sub-02_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses009_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses009_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-02/ses-010/func/sub-02_ses-010_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub02_ses010_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub02_ses010_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-02"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses001_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses001_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses001_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses001_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses001_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses001_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-001/func/sub-03_ses-001_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses001_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-002/func/sub-03_ses-002_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses002_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses002_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-003/func/sub-03_ses-003_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses003_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses003_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-004/func/sub-03_ses-004_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses004_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses004_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-005/func/sub-03_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses005_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses005_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses006_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-006/func/sub-03_ses-006_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses006_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-007/func/sub-03_ses-007_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses007_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses007_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses008_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-008/func/sub-03_ses-008_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses008_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses009_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-009/func/sub-03_ses-009_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses009_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-03/ses-010/func/sub-03_ses-010_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub03_ses010_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub03_ses010_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-03"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses001_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses002_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses003_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses004_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses005_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses006_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses007_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses008_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses009_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub04_ses010_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-04"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-001/func/sub-05_ses-001_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses001_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses001_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-002/func/sub-05_ses-002_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses002_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses002_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-003/func/sub-05_ses-003_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses003_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses003_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses004_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-004/func/sub-05_ses-004_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses004_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses005_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-005/func/sub-05_ses-005_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses005_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-006/func/sub-05_ses-006_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses006_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses006_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses007_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-008/func/sub-05_ses-008_task-relational_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses008_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses008_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-emotion_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-gambling_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-language_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-009/func/sub-05_ses-009_task-restingstate_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses009_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses009_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-motor_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-motor_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-motor_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-relational_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-social_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-wm_run-01_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-motor_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-social_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-wm_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-gambling_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-motor_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-social_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-wm_run-02_space-MNI152NLin2009cAsym_boldref.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-emotion_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-gambling_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-language_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-motor_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub05_ses010_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-social_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {
        "hcptrt": [
            "/sub-05/ses-010/func/sub-05_ses-010_task-wm_run-02_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
        ]
    }


def test_hcptrt_sub05_ses010_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-05"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses001_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-001"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses002_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-002"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses003_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-003"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses004_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-004"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses005_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-005"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses006_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-006"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses007_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-007"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses008_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-008"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses009_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-009"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run01_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-01"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_mask_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["mask"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_boldref_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["boldref"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_emotion():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["emotion"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_gambling():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["gambling"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_language():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["language"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_motor():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["motor"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_relational():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["relational"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_social():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["social"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_wm():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["wm"],
    ) == {"hcptrt": []}


def test_hcptrt_sub06_ses010_run02_bold_restingstate():
    assert cneuromod_fetch(
        subjects=["sub-06"],
        sessions=["ses-010"],
        runs=["run-02"],
        images=["bold"],
        tasks=["restingstate"],
    ) == {"hcptrt": []}

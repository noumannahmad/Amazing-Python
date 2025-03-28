# Imiomics Visualization and Analysis Toolkit

This repository provides tools to **analyze, visualize, and generate collages and videos** from *Imiomics statistical maps*, enabling voxel-wise anatomical insights from MRI data. It supports regression analysis, multiple comparison correction, reference alignment, and publication-ready outputs in both image and video formats.

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `collage_Imiomics.py` | Generate PNG collages from Imiomics statistical maps |
| `imiomicsVideos.py` | Create axial and coronal videos (.avi) of Imiomics maps |
| `regression.py` | Voxel-wise linear/logistic regression to produce statistical NRRD maps |
| `writeShell.py` | Generate shell scripts to run batch regression jobs |
| `helper_collage.py` | Helper to retrieve and organize map files for collage generation |
| `videoHelper.py` | Generate title images with metadata for collages/videos |
| `getParameterFiles.py` | Align and merge subject IDs and variable arrays |
| `README.md` | Project documentation |

---

## 🚀 Getting Started

Install required Python packages:

```bash
pip install numpy matplotlib nibabel scipy
```

---

## 🖼 Generate Collages – `collage_Imiomics.py`

Create comparison collages of Imiomics maps (Jacobian, fat fraction, correlation, regression) across groups.

### Command

```bash
python collage_Imiomics.py \
  -i /path/to/imiomics/maps \
  -f /path/to/mri_and_masks \
  -s small \
  -v BMI,Age \
  -m holm
```

### Arguments

| Flag | Description |
|------|-------------|
| `-i` | Folder with Imiomics maps (`male/`, `female/`) |
| `-f` | Folder with MRI and bodymask data (`small/`, `orig/`, etc.) |
| `-s` | Size of reference couple: `small`, `original`, `large`, `T2D`, `median_new`, etc. |
| `-v` | Variable name(s) used in regression (comma-separated) |
| `-m` | *(Optional)* MCC method: `holm`, `hochberg`, `rft` |

### Output

- Saves `<variable>_collage.png` in the Imiomics folder

---

## 🎥 Generate Videos – `imiomicsVideos.py`

Visualize Imiomics regression results as axial and coronal videos.

### Command

```bash
python imiomicsVideos.py \
  -m "MAPS_DIR/male/beta1_Multiple_Jac__M_map.nrrd,MAPS_DIR/female/beta1_Multiple_Jac__F_map.nrrd,MAPS_DIR/male/beta1_Multiple_Fat__M_map.nrrd,MAPS_DIR/female/beta1_Multiple_Fat__F_map.nrrd" \
  -b "BODYMASK_DIR/male_mask.vtk,BODYMASK_DIR/female_mask.vtk" \
  -r "REFERENCE_DIR/male_water.nrrd,REFERENCE_DIR/male_fat.nrrd,REFERENCE_DIR/female_water.nrrd,REFERENCE_DIR/female_fat.nrrd" \
  -v BMI \
  -f 1 \
  -o output/videos
```

### Arguments

| Flag | Description |
|------|-------------|
| `-m` | Regression map files: Jac_M, Jac_F, Fat_M, Fat_F |
| `-b` | VTK bodymask files for male and female |
| `-r` | Reference MRI files (water & fat) for both genders |
| `-v` | Variable name used in maps |
| `-f` | Flag to include R² map (1 = yes, 0 = no) |
| `-c` | *(Optional)* MCC method |
| `-o` | Output directory for videos |

### Output

- Saves `BMI_axial.mp4`, `BMI_coronal.mp4` in output directory

---

## 📊 Voxel-wise Regression – `regression.py`

Run linear/logistic regression on Imiomics maps for each voxel using subject metadata.

### Command

```bash
python regression.py \
  -fn Jac_M.nrrd \
  -grp_n male \
  -var_f age.txt \
  -ids_f ids.txt \
  -out results/beta_age_male.vtk \
  -mask bodymask.vtk \
  -compute run
```

### Output

- NRRD maps for:
  - Regression coefficients (intercept, main variable, covariates)
  - P-values
  - R² fit map

---

## 🗒️ Generate Shell Scripts – `writeShell.py`

Automate shell script creation for regression jobs on clusters like Bianca.

- Reads subject IDs, variable files
- Generates `.sh` files with `regression.py` commands

---

## 🔧 Helper Scripts

### `helper_collage.py`
- Locates and returns map files in male/female folders
- Organizes files as `[Jac_M, Jac_F, Fat_M, Fat_F]`

### `videoHelper.py`
- Generates title image with metadata
- Includes map type, subject counts, and R² indicator

### `getParameterFiles.py`
- Combines and sorts multiple ID and value arrays
- Returns aligned, sorted inputs for regression

---

## 🔄 Full Example Workflow

```bash
# Generate collage
python collage_Imiomics.py -i maps/ -f mri_masks/ -s small -v BMI

# Generate videos
python imiomicsVideos.py \
  -m "maps/male/beta1_BMI_Jac_M.nrrd,maps/female/beta1_BMI_Jac_F.nrrd,maps/male/beta1_BMI_Fat_M.nrrd,maps/female/beta1_BMI_Fat_F.nrrd" \
  -b "masks/male.vtk,masks/female.vtk" \
  -r "ref/male_water.nrrd,ref/male_fat.nrrd,ref/female_water.nrrd,ref/female_fat.nrrd" \
  -v BMI -f 1 -o output/
```


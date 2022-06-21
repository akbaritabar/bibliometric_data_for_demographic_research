# 1. Required installation and set-up for Python

The following software have installation files for Windows/Linux/Mac. Please choose the one suitable for your operating system and install them. None of them require administrator privileges to be installed, hence you can use your personal laptop or work PC to install them.

- Clone (download) this repository from GitHub: [https://github.com/akbaritabar/bibliometric_data_for_demographic_research](https://github.com/akbaritabar/bibliometric_data_for_demographic_research)
- Please install Anaconda Python from: https://www.anaconda.com/products/individual (**NOTE**: if you use other distributions of Python or environment management systems, it is OK, but make sure to install all libraries in yaml file and run the codes to see if they work?)
    - Use the "yml" file in this directory named "00_setup_required_environment.yml" and conda to create an environment with needed python libraries following points below
    - After successful installation of python, open "Anaconda prompt" (doesn't need to be administrator) by going to windows start menu and searching it
    - Uncomment the line suitable for your operating system in the "yml" file (line 8 for Unix users and line 6 for Windows users. Uncomment means, "delete the starting "#" sign in the line. If needed, change the directory in "yml" file based on where Anaconda Python is installed on your PC)).
    - NOTE: Please rename the environment from bibliodemography to something else (e.g., add a 1 or 2 digit number(s) to the end of the name in line 1 that reads name: bibliodemography to become name: bibliodemography23) if you think someone else might use the same computer to create this environment on the same computer (e.g., if you share a computing platform with colleagues).
    - Change directory to where you have downloaded the "yml" file (e.g., run `cd Users\YOUR-USERNAME\Downloads\` on Windows)
    - Run `conda env create -f 00_setup_required_environment.yml` (it will take a while to download and install the libraries, circa 5-15 minutes is normal depending on the system and internet speed)
    - Check if the installation has been successful and environment is usable (run `conda env list` which should show you "base" and the new environment "bibliodemography". Then run `conda activate bibliodemography` and it should add this name into parenthesis before your prompt e.g., "(bibliodemography) ..."
    - Now you can cd to the directory of this project, type "Jupyter lab" in the `Anaconda prompt` and use it for open scripts in the code folder to replicate the results.

These steps are enough if you wish to replicate text analysis examples, but if you wished to follow the advanced section on parallelization, make sure to follow the extra steps outlined in `03_parallelization_with_dask_duckdb_dbeaver.md`.

# If environment was messed up, what to do?
- First, calm down, it is OK, the goal of using environments was not to cause harm to other projects and isolate them (and also to ensure replicability of projects!)
- Activate `base` environment (with `conda activate base`), because we want to delete `bibliodemography` and recreate it.
- Remove conda environment `bibliodemography` with `conda remove --name bibliodemography --all`
- Then again install everything with: `conda env create -f 00_setup_required_environment.yml`
- Activate bibliodemography ("conda activate bibliodemography" and see with "conda info" if everything if fine?)

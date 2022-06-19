### 1. Required installation and set-up for Python

The following software have installation files for Windows/Linux/Mac. Please choose the one suitable for your operating system and install them. None of them require administrator privileges to be installed, hence you can use your personal laptop or work PC to install them.

- Clone (download) this repository from GitHub: [https://github.com/akbaritabar/bibliometric_data_for_demographic_research](https://github.com/akbaritabar/bibliometric_data_for_demographic_research)
- Please install Anaconda Python from: https://www.anaconda.com/products/individual
    - Use the "yml" file in this directory named "00_setup_required_environment.yml" and conda to create an environment with needed python libraries following points below
    - After successful installation of python, open "Anaconda prompt" (doesn't need to be administrator) by going to windows start menu and searching it
    - Uncomment the line suitable for your operating system in the "yml" file (line 8 for Unix users and line 6 for Windows users. Uncomment means, "delete the starting "#" sign in the line. If needed, change the directory in "yml" file based on where Anaconda Python is installed on your PC)).
    - Change directory to where you have downloaded the "yml" file (e.g., run `cd Users\YOUR-USERNAME\Downloads\` on Windows)
    - Run `conda env create -f 00_setup_required_environment.yml` (it will take a while to download and install the libraries, circa 5-15 minutes is normal depending on the system and internet speed)
    - Check if the installation has been successful and environment is usable (run `conda env list` which should show you "base" and the new environment "bibliodemography". Then run `conda activate bibliodemography` and it should add this name into parenthesis before your prompt e.g., "(bibliodemography) ..."

These steps are enough if you wish to replicate text analysis examples, but if you wished to follow the advanced section on parallelization, make sure to follow the extra steps outlined in `03_parallelization_with_dask_duckdb_dbeaver.md`.
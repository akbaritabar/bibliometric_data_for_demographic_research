# Code

R, Python, and SQL scripts to replicate workshop examples

# Scripts and their usage

## 00_setup_required_environment.yml

This is a Yaml (`.yml`) file that allows you to create a `conda` environment to isolate your Python codes in this workshop from any other project you are creating. You will read more about it in `01_Required_installation_setup_python.md` and `03_parallelization_with_dask_duckdb_dbeaver.md` scripts which are to setup Python libraries.

**NOTE**: Please rename the environment from `bibliodemography` to something else (e.g., add a 1 or 2 digit number(s) to the end of the name in line 1 that reads `name: bibliodemography` to become `name: bibliodemography23`) if you think someone else might use the same computer to create this environment on the same computer (e.g., if you share a computing platform with colleagues).

## 01_Required_installation_setup_python.md

Those who wish to use Python and replicate our examples and results, need to follow instructions in this file to setup their conda environment.

## 02_Required_installation_setup_R.md

Those who wish to use R and replicate our examples and results, need to follow instructions in this file to install needed libraries in R (you need to have R and perhaps R studio as an IDE installed on your machine, see: [https://rstudio-education.github.io/hopr/starting.html](https://rstudio-education.github.io/hopr/starting.html)).

## 03_parallelization_with_dask_duckdb_dbeaver.md

Those who wish to use Python and follow this more advanced tutorial, need to follow instructions in this file to setup their conda environment and also to install two further software that were not installed in instructions of `01_Required_installation_setup_python.md`.


## 04_simple_duckdb_dbeaver_query.sql

If you follow `03_parallelization_with_dask_duckdb_dbeaver.md`, then you will see that `04_simple_duckdb_dbeaver_query.sql` is a simple SQL example that runs with DuckDB and DBeaver.

## 05_HU_seminar_network_analysis.Rmd

This is the Rmarkdown script that generated slides on *introduction to network analysis*. In order to run them, you need to setup R and install libraries (see 02 above). (see here for a description on what is Rmarkdown: [https://akbaritabar.github.io/CV_MD/git_github_for_academic_writing.html](https://akbaritabar.github.io/CV_MD/git_github_for_academic_writing.html))

## 06_example_network_igraph_python.py

For Python users (who have already followed 01 above) who wish to see example of creating a network and some basic functionalities in the Python version of igraph (similar to what was shown in 05 script and slides for R), need to follow this script.

## 07_igraph_from_pandas.py

This is a Python function that is being imported and used in script 06 (you do not need to modify it).

## 08_text_analysis_exact_and_anchor_words.py

If you wish to replicate examples presented in text analysis, `exact and anchor words` identification section, you should use this script.

## 09_functions_to_import_for_text_analysis.py

These are some Python functions that are being imported and used in script 08 (you do not need to modify them).

## 10_text_analysis_noun_phrase_clauses.py

If you wish to replicate examples presented in text analysis, `noun phrase clauses` identification section, you should use this script.

## 99_other_preamble.tex

This is a `preamble` file that is being used in slides of script 05, you do not need to modify it.
--
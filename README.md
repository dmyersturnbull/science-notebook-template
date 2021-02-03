# Science notebook template

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dmyersturnbull/science-notebook-template/HEAD)
[![DOI](https://zenodo.org/badge/335203974.svg)](https://zenodo.org/badge/latestdoi/335203974)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![template science_notebook](https://img.shields.io/badge/template-science_notebook-990099.svg)](https://github.com/dmyersturnbull/science-notebook-template)

🧪 A simple, elegant template for repositories supporting publications.
Companion to the more sophisticated [🦖 Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus), which is for code projects.
No cookiecutter. Just click _Use this Template_ above.

### Citing

**Just tell people how to cite your work.**

Please reference the manuscript with this BibTeX:

```
@misc{sciencenotebooktemplate,
  doi = {10.5281/zenodo.4495745},
  url = {https://zenodo.org/record/4485186},
  author = {Myers-Turnbull, Douglas},
  title = {dmyersturnbull/science-notebook-template: v0.1.0},
  publisher = {Zenodo},
  year = {2021},
  copyright = {Open Access}
}
```

Or APA format:

> Myers-Turnbull, D. (2021). dmyersturnbull/science-notebook-template (v0.1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.4495745

### About this repository

**What’s in this repo?**

- Automatic linting of Python, Markdown, config files, etc. using [pre-commit](https://pre-commit.com/)
- Nice default GitHub settings (just install the [Probot settings app](https://github.com/apps/settings) to your repo
- IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
- [CodeMeta](https://codemeta.github.io/user-guide/) and [CITATION.cff](https://citation-file-format.github.io/)
- Nice gitignore, dockerignore, changelog, and other misc files
- Example/stub Conda environment file, Vagrantfile, and shields

### Steps to reproduce

**How to download needed data, run the code, etc.**

1. Clone this repository as a template and run `pre-commit install`. (`pip install pre-commit`).
2. Install the [Probot settings app](https://github.com/apps/settings).
3. Add to [Binder](https://mybinder.org/) and [Get a DOI](https://guides.github.com/activities/citable-code/) for your repo.
4. Make a local clone of your repo. Modify the readme, changelog, etc. Add your code/notebooks.
5. Commit and push to *main*. (If a linter fails on commit, just re-run. It just meant the linter modified a file.)

### Branch protection rules

This template includes
[branch protection](https://docs.github.com/en/github-ae@latest/github/administering-a-repository/managing-a-branch-protection-rule)
rules for the _main_ branch that disable force-commits, forbid direct pushes,
require status checks to pass, and require a linear history.
You can configure these rules under *Settings → Branches → main*.
The typical workflow is: push changes to a new branch, make a pull request against *main*, and squash–merge or rebase into *main* after the status checks pass.
An *admin*-role user *can* push directly to *main*, but non-*admin* users (with write access) must make pull requests.

### Contributing

**Tell people how to report problems and ask questions.**

The source code in this repository is licensed under the terms of the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).
Contributions and questions are welcome via issues.
For reference, refer to the [contributing guide](https://github.com/dmyersturnbull/science-notebook-template/blob/main/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/science-notebook-template/blob/main/SECURITY.md).

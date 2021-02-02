# Science notebook template

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4485186.svg)](https://doi.org/10.5281/zenodo.4485186)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![template science_notebook](https://img.shields.io/badge/template-science_notebook-990099.svg)](https://github.com/dmyersturnbull/science-notebook-template)

🧪 A simple, elegant template for repositories supporting publications.
Companion to the more sophisticated [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus), which is for code projects.
No cookiecutter. Just click _Use this Template_ above.

### Citing

**Just tell people how to cite your work.**

Please reference the manuscript with this BibTeX:

```
@misc{https://doi.org/10.5281/zenodo.4485186,
  doi = {10.5281/ZENODO.4485186},
  url = {https://zenodo.org/record/4485186},
  author = {Myers-Turnbull, Douglas},
  title = {dmyersturnbull/tyrannosaurus: v0.9.1},
  publisher = {Zenodo},
  year = {2021},
  copyright = {Open Access}
}
```

Or APA format:

> Myers-Turnbull, D. (2021). dmyersturnbull/tyrannosaurus: v0.9.1 (v0.9.1) [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.4485186

### About this repository

**What’s in this repo?**

- Automatic linting of Python, Markdown, config files, etc. using [pre-commit](https://pre-commit.com/)
- Nice default GitHub settings (just install the [Probot settings app](https://github.com/apps/settings) to your repo
- IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
- [CodeMeta](https://codemeta.github.io/user-guide/) and [CITATION.cff](https://citation-file-format.github.io/)
- Nice gitignore, dockerignore, changelog, and other misc files
- Example Conda environment file and Vagrantfile

### Steps to reproduce

**How to download needed data, run the code, etc.**

This template includes GitHub
[branch protection](https://docs.github.com/en/github-ae@latest/github/administering-a-repository/managing-a-branch-protection-rule)
rules against the _main_ branch that: disable force-commits, forbid direct pushes,
require status checks to pass, and require a linear history.
This means that, after your initial import, you will not be able to commit directly to the _main_ branch.
Instead, commit to a new branch and make a pull request.

1. Clone this repository as a template and run `pre-commit install`. (`pip install pre-commit`).
2. Install the [Probot settings app](https://github.com/apps/settings).
3. Make a local clone of your repo, modify the files, commit, and push to _main_.
4. Add your code, commit it, and push it to a _new_ branch.
5. Make a pull request against _main_, wait for the checks to pass, and rebase the changes into _main_.
6. [Get a DOI](https://guides.github.com/activities/citable-code/) for your repo.

### Contributing

**Tell people how to report problems and ask questions.**

The source code in this repository is licensed under the terms of the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).
Contributions and questions are welcome via issues.
For reference, refer to the [contributing guide](https://github.com/dmyersturnbull/science-notebook-template/blob/main/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/science-notebook-template/blob/main/SECURITY.md).

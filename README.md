# Science notebook template

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dmyersturnbull/science-notebook-template/HEAD)
[![DOI](https://zenodo.org/badge/335203974.svg)](https://zenodo.org/badge/latestdoi/335203974)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![template science_notebook](https://img.shields.io/badge/template-science_notebook-990099.svg)](https://github.com/dmyersturnbull/science-notebook-template)

🧪 A simple, elegant template for repositories supporting publications.
Scientific companion to the much more sophisticated code template [Tyrannosaurus 🦖](https://github.com/dmyersturnbull/tyrannosaurus)
No cookiecutter. Just click **Use this Template** above.

## 👋 Citing

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

> Myers-Turnbull, D. (2021). dmyersturnbull/science-notebook-template (v0.1.0) [Computer software].
> Zenodo. https://doi.org/10.5281/zenodo.4495745

## 🎁 About this repository

**What’s in this repo?**

- Automatic linting of Python, Markdown, config files, etc. using
  [pre-commit](https://pre-commit.com/), [Ruff](https://github.com/astral-sh/ruff), and [Prettier](https://prettier.io/).
- IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
- Recommended readme organization, [CITATION.cff](https://citation-file-format.github.io/), etc.
- Nice gitignore, dockerignore, pull request and issue templates, etc.

## 📜 Steps to reproduce

**How to download needed data, run the code, etc.**

1. Click **Use this Template** and create your repo.
2. Clone your repo, and run `pip install pre-commit` and `pre-commit install`.
3. Add your scripts or notebooks, write your readme, and modify anything as you see fit.
   _Note: When you run `git commit`, pre-commit will error if it made changes._
   _That’s normal. Just re-run to finish the commit._
4. In your repo settings, disable _Discussions_ and _Wiki_.
   Also disable _Projects_, if not needed.
5. Enable _Vulnerability reporting_ under _Code security_.
6. Add a _Branch protection rule_ for _main_.
   Check these boxes:
   - _Require a pull request before merging_
   - _Require status checks to pass before merging_
   - _Require branches to be up to date before merging_
   - _Require linear history_
7. Set up [Binder](https://mybinder.org/), and [Get a DOI](https://guides.github.com/activities/citable-code/).

### Development workflow

Use pull requests (PRs) instead of committing directly into _main_.
Give PRs useful titles and descriptions.
Use GitHub Releases to mark stable versions, and include release notes that document the changes.
Follow a consistent versioning scheme, such as [semantic versioning](https://semver.org/).


## 🌳 Layout

**Describe the layout of this repo.**

```
├── src/                     ⟵ project source code
├── data
│   ├── temp-output/         ⟵ files generated per-run
│   │   ├── figures/         ⟵ raw charts and graphs
│   │   ├── ...files
│   │   ├── csv/             ⟵ raw tables
│   │   └── ...files
│   ├── living/              ⟵ files we are actively curating
│   │   ├── figures/
│   │   ├── tables/
│   │   ├── manuscript/
│   │   └── ...files
│   └── frozen/              ⟵ non-modifiable files
│       ├── raw/             ⟵ experimental or downloaded data
│       └── ref/             ⟵ frozen analyses and outputs
└── README.md
```

Some of or all your data might live somewhere external (as documented below) rather than `data/frozen/`.
See [research projects guide](https://dmyersturnbull.github.io/guide/research-projects/) for more info.

## 🔌 External resources

**Describe any external resources needed (e.g., API keys).**

## 🍁 Contributing

**Tell people how to report problems and ask questions.**

The source code in this repository is licensed under the terms of the
[Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).
Contributions and questions are welcome via issues.
For reference, refer to the
[contributing guide](https://github.com/dmyersturnbull/science-notebook-template/blob/main/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/science-notebook-template/blob/main/SECURITY.md).

Note: The source code headers (i.e., SPDX) are to protect you, the user.
I don’t expect you to retain them.
Remove them or replace them with your own when you modify them.

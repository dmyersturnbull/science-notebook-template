# Science notebook template

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dmyersturnbull/science-notebook-template/HEAD)
[![DOI](https://zenodo.org/badge/335203974.svg)](https://zenodo.org/badge/latestdoi/335203974)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![template science_notebook](https://img.shields.io/badge/template-science_notebook-990099.svg)](https://github.com/dmyersturnbull/science-notebook-template)

🧪 A simple, elegant template for repositories supporting publications.
Scientific companion to the much more sophisticated code template [Tyrannosaurus 🦖](https://github.com/dmyersturnbull/tyrannosaurus)
No cookiecutter. Just click _Use this Template_ above.

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

- Automatic linting of Python, Markdown, config files, etc. using [pre-commit](https://pre-commit.com/)
- Nice default GitHub settings (just install the [Probot settings app](https://github.com/apps/settings) to your repo
- IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
  [CITATION.cff](https://citation-file-format.github.io/)
- Nice gitignore, dockerignore, changelog, and other misc files
- Example/stub Conda environment file, Vagrantfile, and shields

## 📜 Steps to reproduce

**How to download needed data, run the code, etc.**

1. Fork this repository as a template.
2. Clone and run `pip install pre-commit` and `pre-commit install`.
3. Install the [Probot settings app](https://github.com/apps/settings).
4. Fix `.github/CODEOWNERS`. Replace with your username or org name.
5. Fix `.github/settings.yml`. (**NOTE:** Make sure to change `private` and `name`.)
6. If you want to use [Commitizen](https://commitizen-tools.github.io/), uncomment the lines in `.pre-commit.yaml`.
   Otherwise, delete `.cz.toml`.
7. Add to [Binder](https://mybinder.org/) and [Get a DOI](https://guides.github.com/activities/citable-code/) for your repo.
8. Make a local clone of your repo. Modify the readme, changelog, etc. Add your code/notebooks.
   Feel free to remove or replace SPDX headers.
9. Commit and push to _main_. (If a linter fails on commit, just re-run. It just meant the linter modified a file.)
10. Configure branch rules _Settings_.

## 🌳 Layout

**Describe the layout of this repo.**

```bash
├── src/                     ⟵ project source code
├── data
│   ├── temp-output/         ⟵ files generated per-run
│   │   ├── figures/         ⟵ raw charts and graphs
│   │   └── ...misc. files
│   ├── living/              ⟵ files we are actively curating
│   │   ├── figures/
│   │   ├── manuscript/
│   │   └── ...misc. files
│   └── frozen/              ⟵ non-modifiable files
│       ├── raw/             ⟵ experimental or downloaded data
│       └── ref/             ⟵ frozen analyses and figures
└── README.md
```

See [research projects guide](https://dmyersturnbull.github.io/guide/research-projects/) for more info.

## 🔌 External resources

**Describe any external resources needed (e.g., API keys).**

## 🍁 Contributing

**Tell people how to report problems and ask questions.**

The source code in this repository is licensed under the terms of the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).
Contributions and questions are welcome via issues.
For reference, refer to the [contributing guide](https://github.com/dmyersturnbull/science-notebook-template/blob/main/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/science-notebook-template/blob/main/SECURITY.md).

Note: The source code headers (i.e., SPDX) are to protect you, the user.
I don’t expect you to retain them.
Remove them or replace them with your own when you modify them.

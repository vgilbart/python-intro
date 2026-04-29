- [Python introduction](#python-introduction)
  - [Description](#description)
  - [Material](#material)
  - [Old Material](#old-material)


# Python introduction 

## Description

- Public: Biology PhD students
- Modalities: 3 x 3 hours of class

## Material 

| Lecture | Link  |
|--------|--------|
| Lesson 1 - Introduction, representing, manipulating and visualising data | [lecture/lesson-1.html](https://vgilbart.github.io/python-intro/lecture/lesson-1.html) |
| Lesson 2 - Lesson 2 - Conditional, Functions, User-input and Errors | [lecture/lesson-2.html](https://vgilbart.github.io/python-intro/lecture/lesson-2.html) |

## Old Material 

The lesson for each year is tagged. To get access to old material, find the tag for the corresponding year. 
You can either browse the files online via github (e.g. for [2024](https://github.com/vgilbart/python-intro/tree/2024))
Or you can clone the repository locally, and switch branch to the corresponding tag.

```
git clone git@github.com:vgilbart/python-intro.git
git checkout -b 2024_branch 2024
```

The lesson are quarto files, which can be rendered in RStudio or in command line (see [quarto documentation](https://quarto.org/docs/projects/quarto-projects.html#rendering-projects) for more information). 

You might need to run the following:
```
QUARTO_PYTHON=~/miniconda3/quarto/bin/python
quarto preview python-intro/lecture/lesson-1.qmd --no-browser --no-watch-inputs
```
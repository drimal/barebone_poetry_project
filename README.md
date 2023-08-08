# A barebone python project using poetry
Python dependency issues can sometimes turn into a nightmare for data scientists and
python developers. I learned this lesson the hard way late 2022, when I had to swich to a new mac with M1 chip. It was a pain to set things up on a new mac with M1 chip. It was around that time, I came across Poetry, but I did not have much bandwidth at the time to try and experiment with it. Inspired by Laszlo Sragner's recent [post](https://laszlo.substack.com/p/cq4ds-python-project-from-scratch?r=366ls&utm_medium=ios&utm_campaign=post), I wanted to
give it a try along with some of the automation from his posts.

```
    poetry new -n --src <project>
    cd <project>
    poetry config virtualenvs.in-project true
    poetry env use python3.10
    source .venv/bin/activate
    poetry add black ruff pytest pre-commit
```

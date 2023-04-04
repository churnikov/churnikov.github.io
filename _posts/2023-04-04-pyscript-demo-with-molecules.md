---
title: "PyKetch: PyScript demo with Ketcher"
categories:
  - Blog
tags:
  - development
  - pyscript
  - ketcher
  - python
---

# Introduction

During PyCon Sweden 2022 I heard a talk on PyScript from its product owner. This talk inspired me to try out combination of PyScript and Ketcher.

👉[Link to the demo](https://churnikov.github.io/demo/pyketch/index.html)👈

## What is PyScript?
[https://pyscript.net/](https://pyscript.net/)

You can [read anacondas announcement](https://engineering.anaconda.com/2022/04/welcome-pyscript.html) on what is PyScript. Essentially it's python that runs in the browser. Important that it's not python translated to javascript, but it's actual python compiled for browser.

PyScript was created in such a way that you can easily use python functions in JavaScript and parts of JavaScript in python.

## What is Ketcher?
[https://lifescience.opensource.epam.com/ketcher/index.html](https://lifescience.opensource.epam.com/ketcher/index.html)
[Ketcher JS docs](https://lifescience.opensource.epam.com/ketcher/developers-manual.html)

Ketcher is a free and open source small molecule visualisation and drawing software developed by EPAM. From my experience it's really nice free web alternative to MarvinJS, which is proprietary software.

# Demo

Idea has actually history that goes back to me working at Biocad. There we tried to use [DashMarvinJS module](https://github.com/stsouko/marvin_dash) for Dash. The problem was that we [had to press ⬆ button which passed state of marvin-js to Dash](https://github.com/stsouko/marvin_dash/issues/3). That was okay for an internal application, but it was not intuitive from the user perspective.

In my opinion, PyScript+Ketcher combo is much better for a Python developer as you don't really have to know JS, but can use its objects directly from Python.

Bellow are the instructions for how to setup minimal local application:

<script src="https://gist.github.com/churnikov/b38940f190efea1f6f13e3f29204ff88.js"></script>

## Problems

While trying out this setup, I encountered a couple of problems:

**I could not use rdkit from pypi.**

But that's understandable limitation of this environment. PyScript team provides custom built libraries like numpy with limited functions (around 80% of functions are available). May be in the future there will be rdkit from pypi available. For now 

**Solution:** Use [rdkit.js](https://www.rdkitjs.com)

**For some reason, the first call of ketcher window for a molecule returns an empty string**

I could not find a solution to that and I guess you have to use ♿ for now.


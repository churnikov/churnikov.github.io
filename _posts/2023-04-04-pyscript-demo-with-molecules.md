---
title: "PyKetch: PyScript demo with Ketcher"
categories:
  - Blog
tags:
  - development
  - pyscript
  - ketcher
  - python
layout: splash
---

# PyKetch: PyScript demo with Ketcher and RDKit

<iframe width="60%" height="500px" src="/demo/pyketch/presentation/"></iframe><br>

Click on the presentation and press `f` to enter fullscreen mode.
{: .notice--info}

This presentation is the end result of this work. I gave this presentation at [EuroScipy 2023](https://pretalx.com/euroscipy-2023/talk/98ZVJH/).

I really hope these efforts will help someone in their work.

# Introduction

During PyCon Sweden 2022 I heard a talk on PyScript from its product owner. This talk inspired me to try out combination of PyScript and Ketcher.

👉[Link to the demo](https://churnikov.github.io/demo/pyketch/index.html)👈

[Link to slides]()

## What is PyScript?
[https://pyscript.net/](https://pyscript.net/)

You can [read anacondas announcement](https://engineering.anaconda.com/2022/04/welcome-pyscript.html) on what is PyScript. Essentially it's python that runs in the browser. Important that it's not python translated to JavaScript, but it's actual python compiled for browser.

PyScript was created in such a way that you can easily use python functions in JavaScript and parts of JavaScript in python.

## What is Ketcher?

Ketcher is a free and open source small molecule visualisation and drawing software developed by EPAM. From my experience it's really nice free web alternative to MarvinJS, which is proprietary software.

- [https://lifescience.opensource.epam.com/ketcher/index.html](https://lifescience.opensource.epam.com/ketcher/index.html)
- [Ketcher JS docs](https://lifescience.opensource.epam.com/ketcher/developers-manual.html)
- There are actually some undocumented functions you can use. [Check out source code on this](https://github.com/epam/ketcher)

# Demo

Idea has actually history that goes back to me working at BIOCAD. There we tried to use [DashMarvinJS module](https://github.com/stsouko/marvin_dash) for Dash. The problem was that we [had to press ⬆ button which passed state of marvin-js to Dash](https://github.com/stsouko/marvin_dash/issues/3). That was okay for an internal application, but it was not intuitive from the user perspective.

In my opinion, PyScript+Ketcher combo is much better for a Python developer as you don't really have to know JS, but can use its objects directly from Python.

Bellow are the instructions for how to setup minimal local application:

<script src="https://gist.github.com/churnikov/b38940f190efea1f6f13e3f29204ff88.js"></script>

## Problems

### Python libraries problems

While trying out this setup, I encountered a couple of problems:

**I could not use rdkit from pypi.**

But that's understandable limitation of this environment. Pyodide team provides [custom built libraries](https://pyodide.org/en/stable/usage/packages-in-pyodide.html) like numpy with limited functions (around 80% of functions are available). May be in the future there will be rdkit from pypi available. For now 

**Solution:** Use [rdkit.js](https://www.rdkitjs.com)

### PyScript problems

**For some reason, the first call of Ketcher window for a molecule returns an empty string**

As far as I understand, the problem is with using py-repl and async functions. In this setup you (and god forbid you do
that through code) have to wait for async code to finish executing. If you would try to run `while not task.done()` loop you
will make an infinite loop that will block your browser window and the whole application. Don't do that. If you want to
actually make working app with async calls, use external python scripts and buttons for now.

Otherwise, wait, Human.

### Integration with other frontend tools

As of 2023, VUE devs explicitly forbid use of `<script>` tag in your DOM. That means that you cannot load PyScript to
your page.

[Link to github issue](https://github.com/vuejs/core/issues/5851#issuecomment-1116026295)



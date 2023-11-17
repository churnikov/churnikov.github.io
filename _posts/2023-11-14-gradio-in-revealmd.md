---
title: "Gradio in Reveal.md"
categories:
  - Blog
tags:
  - development
  - reveal-md
  - gradio
  - presentation-engagement
  - presentation
---

I just found out about [gradio-lite](https://www.gradio.app/guides/gradio-lite). It seems pretty cool and I like to put
these pyodide based projects in reveal-md as it can make for a nice presentation.

In this post I'm trying to put [gradio-lite](https://www.gradio.app/guides/gradio-lite) in a reveal-md presentation.

UPD 14.11.2023: I've tried to put it in a reveal-md presentation, it works but there are a couple of issues:

- In firefox it isn't loading with this error: `Security Error: Content at http://localhost:2500/raw.html may not load data from https://cdn.jsdelivr.net/npm/@gradio/lite/dist/assets/webworker-9ce86444.js.`
- This is a general issue for this type of thing, but the best results of working with this is put gradio app in a
  separate html file and load it as an iframe.


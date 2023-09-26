---
title: "Mentimeter in Reveal.md"
categories:
  - Blog
tags:
  - development
  - reveal-md
  - mentimeter
  - presentation-engagement
  - presentation
---

For EuroScipy 2023 I decided to add add a little engagement element to my presentation. I wanted audience to do
something for me. And in Sweden on many occasions I have seen people use [Mentimeter](https://www.mentimeter.com/) for
presentations, quizzes and other interactivity.

So I decided to check it out myself.

# Mentimeter

Mentimeter is a web-based tool for creating interactive presentations. It has a free tier that allows you to create 
unlimited amount of presentations but only 2 questions per presentation. To me it seems like 2 questions is enough for
what I wanted to do.

And you can export presentations as iframes. Which is great for embedding into reaveal.md presentations.

# Reveal.md

Reveal.md is a tool for creating presentations using markdown. It's simple to use and has some nice docs.

Also, being a markdown based tool it's easy to embed iframes into it, because raw html in markdown files is left untouched
by frameworks that turn markdown into html.

# Embedding Mentimeter into Reveal.md

So I took url for embedding from Mentimeter and put it into my reveal.md presentation. And it worked.

Here is the markup for that:

```markdown
## Slides with Mentimeter

<img src="assets/images/ment_qr.png" width="400" align="center">

Or go to [menti.com](www.menti.com) and Enter `7450 0995`


`---` <!-- remove ` quotes to make it work -->

<section data-background-iframe="https://www.mentimeter.com/app/presentation/alhphvtfbcj74f5kdbdonqpymvzopfku/embed" data-background-interactive>

</section>
```

# Result

These are the slides that I used for my Lightning talk at EuroScipy 2023.

<iframe src="/demo/menitmeter-in-reveal-md/slides/slides.html" width="100%" height="500px"></iframe>

As you can see, you can use reveal.js presentation and on the second slide you can see the mentimeter questions.

There are two slides and you can switch between them using arrows on the bottom left side of the slide.

To allow users check presentation out at their own pace and go through questions at their own speed, you select
`audience pace` in the settings of the presentation.

![mentimeter settings](/assets/images/mentimeter-settings-for-sharing.png)

# Lightning talk

I had only 20 minutes to prepare this. It was enough time, but still, I was a bit scared to do that. I'm happy that I
did as it showed me that my idea actually works and I can now use it my future presentations.

But despite being nervous and not being too good at the presentation I'm content with myself for doing it. While not
conquering my fear of public speaking, I'm at least getting used to it.

It's especially hard that this is happening in English, which is not my native language. And it's stupid when I have to
take a second to generate a sentence in my head before saying it out loud. I hope that by doing this I will get on the
same level of presenting as it was in Russian.


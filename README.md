# Churnikov's blog

This is my personal blog. I write about my projects, my thoughts and my life.

## How to run locally

1. Install [Ruby](https://www.ruby-lang.org/en/downloads/) and [Bundler](https://bundler.io/).
    1. [How to install ruby on MacOS](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/#start-here-if-you-choose-the-long-and-manual-route)
2. Clone this repository.
3. Run `bundle install` in the repository directory.
4. Run `bundle exec jekyll serve --livereload` to start the local server.
5. Open [http://localhost:4000](http://localhost:4000) in your browser.

## Scripts on MacOS to work with images:

Set AWS credentials in `~/.aws/credentials`:

```bash
[default]
aws_access_key_id = <your_access_key_id>
aws_secret_access_key = <your_secret_access_key>
```

How to upload images to DigitalOcean Spaces:
```bash
for file in *.jpg; do
    aws s3 cp --acl public-read --endpoint=https://fra1.digitaloceanspaces.com $file s3://path/on/s3/$file
done
```

How to resize images on MacOS:
```bash
for file in *.jpg; do
    sips -Z 800 "$file" --out "${file%.jpg}_resized.jpg"
done
```

How to convert HEIC to JPG on MacOS:
```bash
for file in *.HEIC; do
    sips -s format jpeg "$file" --out "${file%.heic}.jpg"
done
```

## From the author of template

Click [**Use this template**](https://github.com/mmistakes/mm-github-pages-starter/generate) button above for the quickest method of getting started with the [Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes).

Contains basic configuration to get you a site with:

- Sample posts.
- Sample top navigation.
- Sample author sidebar with social links.
- Sample footer links.
- Paginated home page.
- Archive pages for posts grouped by year, category, and tag.
- Sample about page.
- Sample 404 page.
- Site wide search.

Replace sample content with your own and [configure as necessary](https://mmistakes.github.io/minimal-mistakes/docs/configuration/).

---

## Troubleshooting

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.

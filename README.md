# Note_Algebraic_Dynamics
Notes on algebraic dynamics.

## Managing and building the notes

Run `./accessories/manage-notes` to list and manage chapters and sections.
`notes.json` records their order, titles, status, TeX paths, and PDF URLs.
All documents use the root `refs.bib`. Unfinished titles receive `(draft)`
in LaTeX; the JSON title and folder name retain their original values.

Run `./accessories/manage-notes validate` before committing. For a local
build, install the class from `accessories/templates-of-latex/noteformyself`
and the bundled LXGW WenKai font, then run XeLaTeX/latexmk from the directory
containing the selected wrapper. The book root is `aaa-dynamics.tex`.

After pushing, select **Settings → Pages → Source → GitHub Actions** once.
Use **Actions → Build and deploy notes → Run workflow** to publish PDFs.
The first run builds every document. Later runs rebuild changed documents
and their parent chapter/book, reusing previously published PDFs.
Select **full_build** to rebuild everything, including after an accessories
update (accessories changes are intentionally excluded from detection).
All entries are built and listed regardless of their published/finished flags.

The site serves `notes.json` alongside the PDFs. Its `url` fields are relative
to the Pages site, so a personal website can resolve them against that base URL.
Generated PDFs are ignored by Git.

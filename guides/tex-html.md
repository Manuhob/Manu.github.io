# Latex to html

Here's a simple procedure to convert latex code to an html file.  Assume I've written something "myTexFile.tex" with an accompanying bibliography "myTexBiblio.bib" file.  On the command line:

```
pandoc myTexFile.tex -f latex -t html -s -o myHtmlFile.html
--bibliography myTexBiblio.bib
```

## The options:

- -f specifies the source format, LaTeX

- -t specifies the target format (HTML)

- -s tells pandoc to produce a 'standalone' HTML file

- -o specifies the output filename

- --bibliography gives pandoc the .bib file for the citations in myTexFile.tex

Bingo.


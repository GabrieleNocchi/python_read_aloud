# python_read_aloud

Just a python script to read word documents or pdf out loud, skipping the content of parenthesis and square brackets (references).

Just something I like to use on the drafts of my manuscripts after I am tired reading them again, but can also take pdfs so it can also be used to read scientific papers aloud.
Word does the same thing, but I could not skip the parenthesis (which I want to skip, as most of them are references).

<b>Options: </b>

--voice (male/female)

-- rate (default: 150)

--start (default 1; starting paragraph for word docs, starting page for pdfs)


<b>Usage:</b>
<pre>python read.py your.pdf --voice male --rate 200 --start 2</pre>

or


<pre>python read.py your.docx --voice female --rate 400 --start 10</pre>

  

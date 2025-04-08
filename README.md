# python_read_aloud

Just a python script to read word documents or pdf out loud, skipping the content of parenthesis and square brackets (references).

Just something I like to use on the drafts of my manuscripts after I am tired of reading them again, but can also take pdfs so it can also be used to read aloud scientific papers.
Word does the same thing, but I could not easily skip the parenthesis (which I want to skip, as most of them are references), so I have asked chatGPT for a quick solution.

<b>Options: </b>

--voice (male/female)

-- rate (default: 150)

--start (default 1; starting paragraph for word docs, starting page for pdfs)


<b>Usage:</b>
<pre>python read.py your_file.pdf --voice male --rate 200 --start 2</pre>

or


<pre>python read.py your_file.docx --voice female --rate 400 --start 10</pre>


Libraries:

<pre>import pyttsx3
import docx
import re
import argparse
import PyPDF2</pre>

  

# Brain.ai
<p>
The goal is to design an android
application of a virtual assistant. It is
basically a voice assistant which would
help the user to provide answer to his
question. All the data would be send to
our server which would respond to the
given queries by using algorithms.
</p>
<h3>Features:</h3>
<ul>
  <li>
  Unit Conversion
  </li>
  <li>
  Search Summarization
  </li>
  <li>
  Maps search
  </li>
  <li>
  Live News
  </li>
  <li>
  Setting Alarm
  </li>
</ul>
<h2>What it does:</h2>
<p>
The assistant takes voice as input and
convert it to text and send the raw text
to server.(The voice input and voice to text is done on android using Google API and sent to the python server using socket used in brain_server.py)
</p>
<p>
The server uses some Natural
Language Processing tools such as
POS tagging, Named Entity
recognition to do semantic analysis of
the text and determines which module
will reply and what to reply
</p>
<h3>
Requirements:
</h3>
<ul>
  <li>
  Python2.7
  </li>
  <li>
  NLTK
  </li>
  <li>
  SPACY
  </li>
  <li>
  SEMANTICS.UNITS
  </li>
  <li>
  INFLECT
  </li>
    <li>
  BS4
  </li>
  <li>
  REQUESTS
  </li>
  <li>
  DUCKDUCKGO API
  </li>
</ul>

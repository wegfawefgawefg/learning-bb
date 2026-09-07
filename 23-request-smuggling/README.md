# Request smuggling and parser differences

If a frontend and backend disagree about message boundaries, normalization, or
routing, bytes can enter the wrong request. Model client -> proxy -> app. For
conflicting `Content-Length` and `Transfer-Encoding`, mark where each parser ends
the request. Extend to duplicates, whitespace, HTTP/2 downgrade, and paths.

A useful live lab needs at least two different HTTP parsers, so this lesson is a
design exercise rather than pretending one Flask server can reproduce it. Fix by
rejecting ambiguity and aligning/patching every hop.


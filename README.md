echo
====

A micro library for retrying failing operations inspired by [retry](https://github.com/igorw/retry). It's just as simple as decorating the function. It will retry n number of times and then raise a `FailingTooHard` exception.
```python
import requests
from pyecho import echo

@echo(10) # Retry function upto 10 times
def fetch():
	r = requests.get('http://google.com')
	return r.text

fetch()
```

## License
`echo` is distributed under MIT license, see `LICENSE` for more details.

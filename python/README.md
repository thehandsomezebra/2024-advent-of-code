
## day 1

```bash

cd python

#day 1
python day1.py

#day 1 unit tests
python -m unittest tests/test_day1a.py
python -m unittest tests/test_day1b.py

```



## All tests
```bash
cd python
python -m unittest discover -s tests -p 'test*.py'
```


## containerize it
```bash
#run from root
make run-python DAY=day1
```


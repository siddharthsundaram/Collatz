.PHONY: Collatz.log

FILES :=                              \
    Collatz.html                      \
    Collatz.log                       \
    Collatz.py                        \
    RunCollatz.in                     \
    RunCollatz.out                    \
    RunCollatz.py                     \
    TestCollatz.out                   \
    TestCollatz.py                    \
    cs330e-collatz-tests/koshachii2200-RunCollatz.in   \
    cs330e-collatz-tests/koshachii2200-RunCollatz.out  \
    cs330e-collatz-tests/koshachii2200-TestCollatz.out \
    cs330e-collatz-tests/koshachii2200-TestCollatz.py  \


ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
    DOC := docker run -it -v $$(PWD):/usr/cs330e -w /usr/cs330e fareszf/python
else ifeq ($(shell uname -p), unknown) # Windows
    PYTHON   := python                 # on my machine it's python
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := python -m pydoc        # on my machine it's pydoc
    AUTOPEP8 := autopep8
    DOC := docker run -it -v /$$(PWD):/usr/cs330e -w //usr/cs330e fareszf/python
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
    DOC := docker run -it -v $$(PWD):/usr/cs330e -w /usr/cs330e fareszf/python
endif

collatz-tests:
	git clone https://gitlab.com/fareszf/cs330e-collatz-tests.git

Collatz.html: Collatz.py
	$(PYDOC) -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.tmp: RunCollatz.in RunCollatz.out RunCollatz.py
	$(PYTHON) RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff --strip-trailing-cr RunCollatz.tmp RunCollatz.out

TestCollatz.tmp: TestCollatz.py
	$(COVERAGE) run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
	$(COVERAGE) report -m                      >> TestCollatz.tmp
	cat TestCollatz.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  RunCollatz.tmp
	rm -f  TestCollatz.tmp
	rm -rf __pycache__
	rm -rf cs330e-collatz-tests
	
docker:
	$(DOC)
	
config:
	git config -l

format:
	$(AUTOPEP8) -i Collatz.py
	$(AUTOPEP8) -i RunCollatz.py
	$(AUTOPEP8) -i TestCollatz.py

scrub:
	make clean
	rm -f  Collatz.html
	rm -f  Collatz.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status
	
versions:
	which       $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	which       $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which       git
	git         --version
	@echo
	which       make
	make        --version
	@echo
	which       $(PIP)
	$(PIP)      --version
	@echo
	which       $(PYLINT)
	$(PYLINT)   --version
	@echo
	which        $(PYTHON)
	$(PYTHON)    --version

test: Collatz.html Collatz.log RunCollatz.tmp TestCollatz.tmp collatz-tests check

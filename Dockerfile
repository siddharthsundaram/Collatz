FROM python:3

RUN apt-get update            && \
    apt-get -y install vim    && \
    apt-get install -y dos2unix

RUN pip install --upgrade pip && \
    pip --version             && \
    pip install autopep8      && \
    pip install coverage      && \
    pip install mypy          && \
    pip install pylint        && \
    pip install numpy         && \
    pip list

CMD bash
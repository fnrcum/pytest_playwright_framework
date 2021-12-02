FROM mcr.microsoft.com/playwright:focal

ADD . /paf

WORKDIR /paf

RUN mkdir reports

RUN pip3 install -r requirements.txt \
    && playwright install

ENTRYPOINT ["pytest"]
CMD [" "]





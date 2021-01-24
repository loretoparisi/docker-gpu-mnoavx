#
# @author Loreto Parisi (loretoparisi at gmail dot com)
# v1.0.0
#
# Copyright (c) 2021 Loreto Parisi - https://github.com/loretoparisi/docker
#
FROM pytorch/pytorch:latest

LABEL maintainer "loretoparisi at gmail dot com"

WORKDIR /app

# Matplotlib default directory
ENV MPLCONFIGDIR /app/.config/matplotlib

# app requirements
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["bash"]
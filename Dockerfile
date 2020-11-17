FROM python:3.8

RUN useradd -d /opt/light_worker -m light_worker
WORKDIR /opt/light_worker
USER light_worker

COPY --chown=light_worker ./light_worker.py /opt/light_worker/

ENTRYPOINT ["python3", "/opt/light_worker.py"]
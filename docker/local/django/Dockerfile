FROM docker.io/python:3.13.2-slim-bookworm as python

FROM python AS python-build-stage
ARG BUILD_ENVIRONMENT=requirements

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev

# Corregimos la ruta del requirements
COPY requirements.txt .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
  -r requirements.txt

FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=requirements

ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
  sudo git bash-completion nano ssh

RUN addgroup --system django && \
  adduser --system --ingroup django django && \
  mkdir -p ${APP_HOME}/staticfiles && \
  chown django:django ${APP_HOME}/staticfiles && \
  chmod 775 ${APP_HOME}/staticfiles

RUN apt-get update && apt-get install --no-install-recommends -y \
  libpq-dev \
  gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

# Corregimos las rutas de los scripts
COPY --chown=django:django docker/local/django/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django docker/local/django/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

## Creamos los directorios para Celery
#RUN mkdir -p /app/celery/{worker,beat,flower}
#
#COPY --chown=django:django docker/local/django/celery/worker/start.sh /start-celeryworker
#RUN sed -i 's/\r$//g' /start-celeryworker
#RUN chmod +x /start-celeryworker
#
#COPY --chown=django:django docker/local/django/celery/beat/start.sh /start-celerybeat
#RUN sed -i 's/\r$//g' /start-celerybeat
#RUN chmod +x /start-celerybeat
#
#COPY --chown=django:django docker/local/django/celery/flower/start.sh /start-flower
#RUN sed -i 's/\r$//g' /start-flower
#RUN chmod +x /start-flower

# Copiamos el código del proyecto
COPY --chown=django:django . ${APP_HOME}

RUN chown django:django ${APP_HOME}

USER django

ENTRYPOINT [ "/entrypoint" ]
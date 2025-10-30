FROM python:3.12.1-slim-bookworm

#RUN pip install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Add the virtual environment's bin directory to the PATH so Python tools work globally
# uv sync --locked creates the virtual environment at the current WORKDIR (/app)
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY .python-version pyproject.toml uv.lock ./
RUN uv sync --locked

COPY wk05-deployment/predict.py model.bin ./

EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696" ]
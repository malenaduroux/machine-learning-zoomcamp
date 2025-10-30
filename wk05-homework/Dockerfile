# Base image already includes pipeline_v2.bin
FROM agrigorev/zoomcamp-model:2025

# (Optional) Copy uv binary so we can install dependencies quickly
FROM ghcr.io/astral-sh/uv:latest AS uv
FROM agrigorev/zoomcamp-model:2025
COPY --from=uv /uv /uvx /bin/

# Set the working directory to match the base image
WORKDIR /code

# Copy dependency files
COPY pyproject.toml uv.lock .python-version ./

# Install dependencies using uv (in locked mode)
RUN uv sync --locked

# Copy your FastAPI app
COPY wk05-homework/predict.py ./

# Expose port for Uvicorn
EXPOSE 9696

# Set up virtualenv path for uv
ENV PATH="/code/.venv/bin:$PATH"

# Run FastAPI with Uvicorn
ENTRYPOINT ["uvicorn", "predict:code", "--host", "0.0.0.0", "--port", "9696"]

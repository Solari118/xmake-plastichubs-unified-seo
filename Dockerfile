FROM python:3.12-slim
WORKDIR /workspace
COPY . /workspace
RUN python scripts/validate_project.py
CMD ["python", "scripts/route_task.py", "--help"]

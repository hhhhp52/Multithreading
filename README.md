# Multithreading

## How To Run It

### Using Make Command

1. **Run locally:**
   1. Open your terminal.
   2. Clone the repository:
      ```
      git clone git@github.com:hhhhp52/Multithreading.git
      ```
   3. Navigate to the project directory:
      ```
      cd Multithreading
      ```
   4. Execute the command:
      ```
      python3 thread.py
      ```
      or
      ```
      make run-local-job
      ```

2. **Run using Docker:**
   1. Open your terminal.
   2. Clone the repository:
      ```
      git clone git@github.com:hhhhp52/Multithreading.git
      ```
   3. Ensure Docker is installed on your system.
   4. Build the Docker image:
      ```
      make build-image
      ```
   5. Run the Docker container:
      ```
      make run-docker-job
      ```
   6. If you want to restart without rebuilding the image, start from step 5. If you need to rebuild the image, start from step 4.

---

## Directory Structure

- **Multithreading/**
  - `.gitignore`: Ignores files not pushed to GitHub.
  - `Dockerfile`: Defines the Docker image configuration.
  - `Makefile`: Provides convenient commands for execution.
  - `requirements.txt`: Specifies Python package dependencies and versions.
  - `thread.py`: Main entry point and primary code file.

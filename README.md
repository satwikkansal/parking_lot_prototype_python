# Gojek submission

Submission for Parking lot problem.

## Instructions to run

> To run the interactive mode (CLI), simply ignore the `tests/test_input.txt` argument in the following commands.

### Running through shell script (Recommended)

```sh
$ bin/setup
$ bin/parking_lot tests/test_input.txt
```

To run functaionl spec,
```sh
$ bin/run_functional_tests
```

**Note:** The shell scripts fallback to Docker, if Python version 3.7+ is not detected in the system.


### Running directly using Python (Requires Python 3.7+)

```sh
$ python src/main.py tests/test_input.txt
```

### Running using Docker

```sh
$ docker build -t gojek-submission-satwik .
$ docker run -it gojek-submission-satwik
```

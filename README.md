# symeo-lambda-example

## :construction: Installation

### Minimum requirements

- [Python](https://www.python.org/) 3.10

### Install the application locally

- Run `git clone git@github.com:symeo-io/symeo-lambda-example.git` or `https://github.com/symeo-io/symeo-lambda-example.git`
- Run `cd symeo-lambda-example` to navigate to the code folder
- Run `pip install -r requirements.txt` to install project dependencies
- Run `pre-commit install` to set up the git hook scripts

## :wrench: Development

### Coding conventions

The coding conventions and style are enforced by the [black](https://github.com/psf/black) formatter.

To fix automatically format errors, run `black <target_directory>`.

To check all coding conventions before committing to your remote repo we use [pre-commit](https://pre-commit.com/) hooks. If you didn't already run `pre-commit install` right after cloning the repo, you should do it now.

## :office: Architectures

### Structure

The source code is contained in the `/src` directory:

```text
src
├── __init__.py
├── application
│   ├── __init__.py
│   └── lambda_processor.py
├── bootstrap
│   ├── __init__.py
│   ├── lambda_function_adwords_audience_device_report.py
│   └── lambda_function_dv360_standard_report.py
├── domain
│   ├── __init__.py
│   ├── default_raw_to_clean_processor.py
│   └── port
│       ├── __init__.py
│       ├── model
│       │   ├── __init__.py
│       │   ├── bucket_object.py
│       │   ├── source_object.py
│       │   └── target_object.py
│       ├── obtain
│       │   ├── __init__.py
│       │   ├── obtain_input_data_cleaner_adapter.py
│       │   ├── obtain_input_data_reader_adapter.py
│       │   ├── obtain_output_data_transformer_adapter.py
│       │   └── obtain_output_data_writer_adapter.py
│       └── request
│           ├── __init__.py
│           └── request_raw_to_clean_processor_adapter.py
└── infrastructure
    ├── __init__.py
    ├── cleaner
    │   ├── __init__.py
    │   ├── adwords
    │   │   ├── __init__.py
    │   │   └── adwords_audience_cleaner_adapter.py
    │   └── dv360
    │       ├── __init__.py
    │       └── dv360_report_cleaner_adapter.py
    ├── client
    │   ├── __init__.py
    │   └── aws_client.py
    ├── reader
    │   ├── __init__.py
    │   ├── s3_csv_reader_adapter.py
    │   └── s3_json_reader_adapter.py
    ├── transformer
    │   ├── __init__.py
    │   └── parquet_transformer_adapter.py
    └── writer
        ├── __init__.py
        └── s3_writer_adapter.py
```

The structure of this project follows **Hexagonal-Architecture** and **Domain-Driven-Design** principles and is seperated into 4 main folders:
1. `/application`: it will contain adapters related to your "application". For now, you will only find one application adapter (`lambda_processor`).
2. `/domain`: this is where all the business logic has to be.
3. `/infrastructure`: this is where all your adapters related to your infrastructure should be. You can already find several adapters in the [infrastructure](src/infrastructure) folder.
4. `/bootstrap`: this is where you will bootstrap your project by making [dependency injections](#entrypoint-and-dependency-injection).

## :rocket: Infrastructure

### Entrypoint and Dependency Injection

#### Entrypoint

This application has two different entrypoint that you can use when deploying it (`lambda_function_adwords_audience_device_report.py` or `lambda_function_dv360_standard_report`), located in the [bootstrap](./src/bootstrap) folder.

The way this project is built allows you to launch **two different lambda functions** depending on your needs but thanks to **Clean Architecture** and more specifically **Hexagonal Architecture** you
do not need to completely change the structure of your application. Moreover, your business code do not see a change from one lambda function to the other.

The things that differ are only technical implementation, and you can manage to change from one to the other through [dependency injections](#dependency-injection)

#### Dependency Injection

If you take the two different entrypoints ([lambda_function_adwords_audience_device_report.py](./src/bootstrap/lambda_function_adwords_audience_device_report.py) and
[lambda_function_dv360_standard_report](./src/bootstrap/lambda_function_dv360_standard_report.py), you will notice that they are very similar. In fact, the only thing that defer is the initialization of
the `DefaultRawToCleanProcessor` service.

```python
# lambda_function_adwords_audience_device_report.py
default_raw_to_clean_processor = DefaultRawToCleanProcessor(
    S3JsonReaderAdapter(aws_client),
    AdwordsAudienceCleanerAdapter(), # <-- different implementation
    ParquetTransformerAdapter(),
    S3WriterParquetAdapter(aws_client),
)
```

```python
# lambda_function_dv360_standard_report.py
default_raw_to_clean_processor = DefaultRawToCleanProcessor(
    S3CsvReaderAdapter(aws_client),
    DV360ReportCleanerAdapter(), # <-- different implementation
    ParquetTransformerAdapter(),
    S3WriterParquetAdapter(aws_client),
)
```

By instantiating our services at runtime with different technical implementations allows us to create different behaviors without changing
neither the structure of our code or our business code (present in the `domain` folder).

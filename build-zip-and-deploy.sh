# /bin/bash

rm -rf package my-deployment-package.zip
rm -f lambda_function.py
cp src/bootstrap/lambda_function_adwords_audience_device_report.py ./lambda_function.py
zip -g my-deployment-package.zip lambda_function.py
zip -g my-deployment-package.zip -r src/
aws lambda update-function-code --function-name symeo-stg-dtlk-gads-device-audience-R-C-lambda --zip-file fileb://my-deployment-package.zip --profile default
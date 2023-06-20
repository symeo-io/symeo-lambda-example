# /bin/bash


function build-and-deploy-lambda() {
  if [[ -f "$1" ]];then
    rm -rf package my-deployment-package.zip
  fi

  mv src/boostrap/$bootstrap_lambda_function_file_name ./lambda_function.py
  zip -g my-deployment-package.zip lambda_function.py
  zip -g my-deployment-package.zip -r src/
  aws lambda update-function-code --function-name $2 --zip-file fileb://my-deployment-package.zip --profile default
}
import unittest

from src.bootstrap.lambda_function_adwords_audience_device_report import lambda_handler


class LambdaProcessorIntegrationTest(unittest.TestCase):
    def test_should_process_s3_raw_csv_file_to_s3_clean_parquet(self):
        lambda_handler(
            self.__build_event(
                "tz=Europe_Paris/year=2021/month=11/day=10/first-report-2021-11-10.csv",
                "symeo-stg-dtlk-raw-dv360-daily-ipm",
            ),
            None,
        )

    def __build_event(self, bucket_key, bucket_name):
        return {
            "Records": [
                {
                    "messageId": "97c19a82-4b96-49f0-bad5-fd5946c3603f",
                    "receiptHandle": "AQEBz+ohllBn7F7+H6mnQ0g6U6rROGqFgsD783o+XaoJCCnlUcY8NU6k5qKg+hzzf+/81FTlo3AJQ2dvwEf9T3XLvTVeATLlRKMXmthl2l9l08ETzwIcprk+ImYYGkRPH/2eGjvGFfEArxDt+yNq1AeI6LMEdJo3sQ96atUJM0SXLiaVfSZBra/DmxSxuRuXLs7Ohe06bYIU5cze/nRq/QWKqTUzIBAohB5Esqd0SBVd8BeFptOtTnovziDpLFzy8LOFrVI373+ZoIDeqrwoWhWb+WOb0VDJuYb7NnOplYa7vOy2pccfyX6bprgKwuQAEw/5EsCdx6lcedygGcP3Xj435phm+/xuhDWiA6aP9mklbsbxQY1YQUtSsbSR/eUu8xgwcl3OfZ0pRH6MO5IG6Kpok54dQwN5yvHHekpi/CI3b98=",
                    "body": '{"version":"0","id":"5627b6e8-8bea-8ac7-3424-0ceb86ace103","detail-type":"AWS API Call via CloudTrail","source":"aws.s3","account":"757703129699","time":"2022-02-11T09:46:37Z","region":"eu-west-1","resources":[],"detail":{"eventVersion":"1.08","userIdentity":{"type":"AssumedRole","principalId":"AROA3A2VAHJRWST5LER2Z:pierre@symeo.tech","arn":"arn:aws:sts::757703129699:assumed-role/AWSReservedSSO_AWSAdministratorAccess_fe1cf894880e9253/pierre@symeo.tech","accountId":"757703129699","accessKeyId":"ASIA3A2VAHJRQC5XYJOD","sessionContext":{"sessionIssuer":{"type":"Role","principalId":"AROA3A2VAHJRWST5LER2Z","arn":"arn:aws:iam::757703129699:role/aws-reserved/sso.amazonaws.com/eu-west-1/AWSReservedSSO_AWSAdministratorAccess_fe1cf894880e9253","accountId":"757703129699","userName":"AWSReservedSSO_AWSAdministratorAccess_fe1cf894880e9253"},"attributes":{"creationDate":"2022-02-11T08:38:22Z","mfaAuthenticated":"false"}}},"eventTime":"2022-02-11T09:46:37Z","eventSource":"s3.amazonaws.com","eventName":"PutObject","awsRegion":"eu-west-1","sourceIPAddress":"217.128.140.35","userAgent":"[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36]","requestParameters":{"X-Amz-Date":"20220211T094637Z","bucketName":"symeo-stg-dtlk-raw-gads-device-bzi","X-Amz-Algorithm":"AWS4-HMAC-SHA256","x-amz-acl":"private","X-Amz-SignedHeaders":"content-md5;content-type;host;x-amz-acl;x-amz-storage-class","Host":"symeo-stg-dtlk-raw-gads-device-bzi.s3.eu-west-1.amazonaws.com","X-Amz-Expires":"300","key":"Europe_Paris.fr-FR.EUR.2022-01-17.gads-report-gender.1316752390.json","x-amz-storage-class":"STANDARD"},"responseElements":null,"additionalEventData":{"SignatureVersion":"SigV4","CipherSuite":"ECDHE-RSA-AES128-GCM-SHA256","bytesTransferredIn":21838.0,"AuthenticationMethod":"QueryString","x-amz-id-2":"dAnE6JIfuNr6yLao76efWsAYmwXXneym3GwFilsdYXC52fgMpEhIgVHrLfACpyEHCuaaCuWSQ+A=","bytesTransferredOut":0.0},"requestID":"FNQMP9GW6T92Y09S","eventID":"4851a383-e007-40d2-b5a3-087d2a7177dc","readOnly":false,"resources":[{"type":"AWS::S3::Object","ARN":"arn:aws:s3:::symeo-stg-dtlk-raw-gads-device-bzi/Europe_Paris.fr-FR.EUR.2022-01-17.gads-report-gender.1316752390.json"},{"accountId":"757703129699","type":"AWS::S3::Bucket","ARN":"arn:aws:s3:::symeo-stg-dtlk-raw-gads-device-bzi"}],"eventType":"AwsApiCall","managementEvent":false,"recipientAccountId":"757703129699","eventCategory":"Data"}}',
                    "attributes": {
                        "ApproximateReceiveCount": "2",
                        "SentTimestamp": "1644572802698",
                        "SenderId": "AIDAJ2E4ZHTZPIG4AM4I6",
                        "ApproximateFirstReceiveTimestamp": "1644572802706",
                    },
                    "messageAttributes": {},
                    "md5OfBody": "7c244d0d50aaa9eb63d6c9987c5c8914",
                    "eventSource": "aws:sqs",
                    "eventSourceARN": "arn:aws:sqs:eu-west-1:757703129699:symeo-stg-dtlk-gads-device-R-C-sqs",
                    "awsRegion": "eu-west-1",
                }
            ]
        }

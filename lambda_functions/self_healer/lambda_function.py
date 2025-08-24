import json
import boto3

def lambda_handler(event, context):
    issue_type = event.get("issue_type", "")
    ssm = boto3.client("ssm")

    if issue_type == "service_restart":
        ssm.send_command(
            InstanceIds=["i-0123456789abcdef0"],
            DocumentName="AWS-RunShellScript",
            Parameters={"commands": ["sudo systemctl restart my-service"]}
        )
        return {"status": "remediation triggered"}
    return {"status": "no action"}
import requests
import csv
from dagster import job, op, get_dagster_logger, schedule, repository


@op
def hello_cereal():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    get_dagster_logger().info(f"Found {len(cereals)} cereals")
    print(cereals)
    for cereal in cereals:
        get_dagster_logger().info(f"cereal: {cereal.keys()}")
        return cereals


@job
def hello_cereal_job():
    hello_cereal()

@schedule(
    cron_schedule="* * * * *",
    job=hello_cereal_job,
    execution_timezone="America/Mexico_City",
)
def good_morning_schedule(context):
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {"ops": {"hello_cereal": {"config": {"date": date}}}}

@repository
def hello_cereal_repository():
    return [hello_cereal_job, good_morning_schedule]


if __name__ == "__main__":
    result = hello_cereal_job.execute_in_process()
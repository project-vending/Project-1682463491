
import os

# Create the main project folder
project_folder = "Data Pipeline for Social Media Sentiment Analysis"
if not os.path.exists(project_folder):
    os.mkdir(project_folder)

# Create subfolders for each component of the project
aws_folder = os.path.join(project_folder, "AWS")
if not os.path.exists(aws_folder):
    os.mkdir(aws_folder)

 _folder = os.path.join(project_folder, "Python")
if not os.path.exists( _folder):
    os.mkdir( _folder)

airflow_folder = os.path.join(project_folder, "Airflow")
if not os.path.exists(airflow_folder):
    os.mkdir(airflow_folder)

docker_folder = os.path.join(project_folder, "Docker")
if not os.path.exists(docker_folder):
    os.mkdir(docker_folder)

sql_folder = os.path.join(project_folder, "SQL")
if not os.path.exists(sql_folder):
    os.mkdir(sql_folder)

# Create empty files for each component
aws_file = os.path.join(aws_folder, "aws.py")
if not os.path.exists(aws_file):
    open(aws_file, 'w').close()

 _file = os.path.join( _folder, "transform.py")
if not os.path.exists( _file):
    open( _file, 'w').close()

airflow_file = os.path.join(airflow_folder, "dags.py")
if not os.path.exists(airflow_file):
    open(airflow_file, 'w').close()

docker_file = os.path.join(docker_folder, "Dockerfile")
if not os.path.exists(docker_file):
    open(docker_file, 'w').close()

sql_file = os.path.join(sql_folder, "queries.sql")
if not os.path.exists(sql_file):
    open(sql_file, 'w').close()

# Create a file for Great Expectations
great_expectations_file = os.path.join(project_folder, "great_expectations.yml")
if not os.path.exists(great_expectations_file):
    open(great_expectations_file, 'w').close()

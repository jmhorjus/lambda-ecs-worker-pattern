# Constants (User configurable)

FULL_NAME_AND_EMAIL = 'Jan Horjus <jan.horjus@viasat.com>'  # For Dockerfile/POV-Ray builds.
APP_NAME = 'ecs-test-jhorjus'  # Used to generate derivative names unique to the application.

# create a repo here https://console.aws.amazon.com/ecs/home?region=us-east-1#/repositories
# DOCKERHUB_USER will be created as part of that
DOCKERHUB_USER = '831754492748.dkr.ecr.us-east-1.amazonaws.com'
DOCKERHUB_EMAIL = 'jan.horjus@viasat.com'
DOCKERHUB_REPO = 'jhorjus-testing'
DOCKERHUB_TAG = DOCKERHUB_USER + '/' + DOCKERHUB_REPO + ':' + APP_NAME

AWS_REGION = 'us-east-1'
AWS_CLUSTER_REGIONS = 'us-east-1c,us-east-1d'
AWS_PROFILE = 'art_ihs'  # The same profile used by your AWS CLI installation
AWS_SECURITY_GROUP_ID = 'sg-74bfdf0e'

SSH_KEY_NAME = 'automation.pem'  # Expected to be in ~/.ssh
ECS_CLUSTER = 'jhorjus'

pipeline {
    agent {
      docker {
        image 'jfloff/alpine-python'
      }
    }
    stages {
        stage('Checkout Repo') {
            steps {
                git credentialsId: 'github_key', url: 'git@github.com:davidhullster/flask-texttool.git'
            }
        }
        stage('Install Dependencies') {
          steps {
            script {
                sh """
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install pylint
                pip install -r requirements.txt
                """
            }
          }
        }
        stage('Linting') {
          steps {
            script {
                sh """
                source venv/bin/activate
                python -m pylint -E **/*.py
                """
            }
          }
        }
        stage('Testing') {
          steps {
            script {
              sh """
              source venv/bin/activate
              python -m unittest discover -s tests/
              """
            }
          }
        }
    }
    post {
    failure {
      script {
        msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
            }
    }
  }
}

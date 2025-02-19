pipeline {
    agent any

    stages {

        stage('Setup Virtual Environment') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '. venv/bin/activate && python -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                sh '. venv/bin/activate && python main.py'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && python -m pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

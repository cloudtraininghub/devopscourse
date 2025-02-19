pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install --upgrade pip'
            }
        }

        stage('Build') {
            steps {
                // Run your build commands
                sh 'python main.py build'
            }
        }

        stage('Test') {
            steps {
                // Run your test commands
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                // Add your deployment steps here
                echo 'Deploying...'
            }
        }
    }

    post {
        always {
            // Clean up workspace
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


pipeline {
    agent any

    stages {
        stage('clone repo') {
            steps {
                
                sh "python3 jinkins/my.py"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                
            }
        }
    }
}


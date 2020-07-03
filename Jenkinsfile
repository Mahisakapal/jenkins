
pipeline {
    agent any

    stages {
        stage('clone repo') {
            steps {
                
                sh "ls"
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
                sh "sudo python3 jinkins/my.py"
            }
        }
    }
}


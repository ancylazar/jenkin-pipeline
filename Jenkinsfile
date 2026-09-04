pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ancylazar/student-result-program.git'
            }
        }

        stage('Build') {
            steps {
                bat 'echo 75 65 80 | python student_result.py'
            }
        }

    }
}
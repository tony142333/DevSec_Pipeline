pipeline {
    agent any

    environment {
        // Since you are on Windows, we access SonarQube via localhost
        SONAR_HOST_URL = 'http://localhost:9000'
        IMAGE_NAME = 'fortress-app:latest'
    }

    stages {
        // STAGE 1: SAST (Code Security Scan)
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQubeScanner'
                    // We use the name you gave in Manage Jenkins (likely 'sonar-server')
                    withSonarQubeEnv('sonar-server') {
                        // WINDOWS COMMAND: uses 'bat' and points to the .bat executable
                        bat """
                            "${scannerHome}\\bin\\sonar-scanner.bat" \
                            -Dsonar.projectKey=DevSecOps-Pipeline \
                            -Dsonar.sources=PHASE1 \
                            -Dsonar.host.url=http://localhost:9000 \
                            -Dsonar.login=sonarqube-token
                        """
                    }
                }
            }
        }

        // STAGE 2: BUILD THE ARTIFACT
        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    dir('PHASE1') {
                        // WINDOWS COMMAND: uses 'bat'
                        bat "docker build -t ${IMAGE_NAME} ."
                    }
                }
            }
        }
    }
}
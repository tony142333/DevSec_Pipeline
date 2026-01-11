pipeline {
    agent any

    environment {
        // 1. UNLOCK THE VAULT: Get the real secret token and save it to 'SONAR_AUTH_TOKEN'
        SONAR_AUTH_TOKEN = credentials('sonarqube-token')

        // 2. USE 127.0.0.1: Safer than 'localhost' for Windows Services
        SONAR_HOST_URL = 'http://127.0.0.1:9000'
        IMAGE_NAME = 'fortress-app:latest'
    }

    stages {
        // STAGE 1: SAST (Code Security Scan)
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv('sonar-server') {
                        // WINDOWS COMMAND
                        // Note: We use %SONAR_AUTH_TOKEN% so the batch script reads the secret safely
                        bat """
                            "${scannerHome}\\bin\\sonar-scanner.bat" \
                            -Dsonar.projectKey=DevSecOps-Pipeline \
                            -Dsonar.sources=PHASE1 \
                            -Dsonar.host.url=http://127.0.0.1:9000 \
                            -Dsonar.login=%SONAR_AUTH_TOKEN%
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
                        bat "docker build -t ${IMAGE_NAME} ."
                    }
                }
            }
        }
    }
}



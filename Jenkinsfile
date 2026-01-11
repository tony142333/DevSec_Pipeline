pipeline {
    agent any

    environment {
        // This matches the name you gave in "Manage Jenkins -> System"
        SONAR_SERVER = 'sonar-server'
        IMAGE_NAME = 'fortress-app:latest'
    }

    stages {
        // STAGE 1: SAST (Code Security Scan)
        stage('SonarQube Analysis') {
            steps {
                script {
                    // We call the scanner tool we installed earlier
                    def scannerHome = tool 'SonarQubeScanner'

                    withSonarQubeEnv(SONAR_SERVER) {
                        sh "${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=DevSecOps-Pipeline \
                        -Dsonar.sources=PHASE1 \
                        -Dsonar.host.url=http://sonarqube-server:9000 \
                        -Dsonar.login=sonarqube-token"
                    }
                }
            }
        }

        // STAGE 2: BUILD THE ARTIFACT
        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // We move into the app folder where the Dockerfile lives
                    dir('PHASE1') {
                        sh "docker build -t ${IMAGE_NAME} ."
                    }
                }
            }
        }
    }
}
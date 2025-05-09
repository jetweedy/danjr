pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Frontend') {
            steps {
                dir('danjr-frontend') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }

        stage('Deploy via Ansible') {
            steps {
                dir('danjr-deploy') {
                    sh 'ansible-playbook deploy.yml'
                }
            }
        }
    }
}

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
                    sh 'echo "Running as user: $(whoami)"'
                    sh 'echo "PATH: $PATH"'
                    sh 'which npm || echo "npm not found!"'
                    sh 'npm list react-scripts || echo "react-scripts not installed"'
                    sh 'CI=false npm run build || echo "❌ npm build failed"'
                    sh 'ls -la build || echo "❌ build folder missing"'
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

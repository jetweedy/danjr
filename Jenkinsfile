pipeline {
    agent any

    tools {
        nodejs 'node18'
    }

    stages {

        //stage('Checkout Code') {
        //    steps {
        //        checkout scm
        //    }
        //}

        //stage('Build Frontend') {
        //    steps {
        //        dir('danjr-frontend') {
        //            sh 'npm install'
        //            sh 'CI=false npm run build'
        //            sh 'ls -la build || echo "❌ Build folder missing!"'
        //        }
        //    }
        //}


        stage('Verify What Jenkins Will Copy') {
            steps {
                dir('danjr-frontend/build') {
                    sh 'echo "📦 Checking contents of build folder..."'
                    sh 'ls -la'
                    sh 'grep "<h1>" index.html || echo "No <h1> in index.html"'
                    sh """grep "Tasks" ../src/App.js || echo 'No Tasks string in source'"""
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


pipeline {

    agent any

    stages {

        stage('Repository Information') {
            steps {
                echo "Repository downloaded successfully."

                sh 'pwd'
                sh 'ls -lah'
            }
        }

        stage('Create Build Directory') {
            steps {
                sh 'mkdir -p build'
            }
        }

        stage('Copy HTML') {
            steps {
                sh 'cp index.html build/'
            }
        }

        stage('Verify Build') {
            steps {
                sh 'ls -lah build'
            }
        }
        
stage('Git Information') {
    steps {
        sh 'git branch'
        sh 'git log --oneline -5'
        sh 'git status'
    }
}

    }

    post {

        success {
            archiveArtifacts artifacts: 'build/**'
            echo "Artifacts archived successfully."
        }

        failure {
            echo "Pipeline failed."
        }

        always {
            echo "Lesson 5 Pipeline Finished."
        }

    }

}

pipeline {
    agent any
    environment {
        PATH = "/opt/homebrew/Cellar/python@3.10/3.10.2/bin:$PATH"
    }
    stages {
        stage('Test Locust') {
                            steps {
                                sh 'Download e execucao do Locust'
                                git 'https://github.com/emersinrp/carga-price-ygg.git'
                                sh 'locust --headless -u 1 -r 1 --run-time 30m'

                            }

        }

    }
}
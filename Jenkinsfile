pipeline {
    agent any
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
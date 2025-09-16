pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile src/python/insert.py src/python/myfunction.py'
            }
        }

        // stage('Test') {
        //     steps {
        //         sh '''
        //         pytest \
        //         --junit-xml=src/python/test-reports/results.xml \
        //         src/python/test.py
        //         '''
        //     }
        //     post {
        //         always {
        //             junit 'src/python/test-reports/results.xml'
        //         }
        //     }
        // }

        stage('Deliver') {
            steps {
                sh 'pyinstaller --onefile src/python/insert.py' // créer un executable dist.insert
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                ansiblePlaybook credentialsId: 'ansible-ssh-key', 
                                inventory: 'ansible/inventory.yaml',
                                playbook: 'ansible/sites-playbook.yml',
                                colorized: true,
                                disableHostKeyChecking: true,
                                vaultCredentialsId: 'ansible-vault-password'

            }
        }
    }
}
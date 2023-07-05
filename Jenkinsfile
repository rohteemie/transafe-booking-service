pipeline {
  agent any

  environment {
	// Disable strict host key checking
	GIT_SSH_COMMAND = 'ssh -o StrictHostKeyChecking=no'
	}

  stages {
	stage('Checkout') {
		steps {
		// Checkout the source code from the repository
		checkout scm
		}
	}

  stage('Deploy') {
    steps {
		// Add your deployment steps here
    	sh 'ssh -i .ssh/id_rsa ubuntu@100.25.148.168 "mkdir -p ~/bookings"'
    	sh 'ssh -i .ssh/id_rsa ubuntu@100.25.148.168 "git clone https://github.com/rohteemie/transafe-booking-service.git"'
    	}
	}
  }
}
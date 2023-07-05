pipeline {
  agent any

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
    	sh 'ssh ubuntu@techalgo.tech "mkdir -p ~/bookings"'
    	sh 'ssh ubuntu@techalgo.tech "git clone https://github.com/rohteemie/transafe-booking-service.git"'
    }

	environment {
		// Disable strict host key checking
		GIT_SSH_COMMAND = 'ssh -o StrictHostKeyChecking=no'
	}

    }
  }
}

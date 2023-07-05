pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        // Checkout the source code from the repository
        checkout scm
      }
    }

    stage('Build') {
      steps {
        // Install dependencies and build the Python application
        sh 'echo "Hello Jenkins!"'
      }
    }

    stage('Deploy') {
      steps {
		// Add your deployment steps here
    	sh 'ssh ubuntu@18.204.8.62 "mkdir -p ~/bookings"'
    	sh 'ssh ubuntu@18.204.8.62 "git clone https://github.com/rohteemie/transafe-booking-service.git"'
      }
    }
  }
}

pipeline {

agent any

stages {
    stage('Checkout') {
        steps {
            git 'https://github.com/tamirfri/WorldOfGames.git'
// Get code from a GitHub repository
        }
    }
    stage('Build') {
        steps {
            script {
                docker.build('tamirfri/wog_server')
// Runs docker build to create and tag the specified
// image from a Dockerfile in the current directory.
// Returns the resulting Image object.
            }
        }
    }
    stage('Run') {
        steps {
            script {
// Creates an Image object with a specified name or ID.
                docker.image(
                    'tamirfri/wog_server'
                ).run(
                    '-p 8777:5000 --rm'
                )
// Uses docker run to run the image,
// and returns a Container which you could stop later.
            }
        }
    }
    stage('Test') {
        steps {
            script {
                docker.image(
                    'selenium/standalone-firefox'
                ).run(
                    '-p 4444:4444 --shm-size 2g --rm',
                    'python3 e2e.py localhost 8777'
                )
            }
        }
        post {
            cleanup {
                httpRequest 'http://localhost:8777/stop'
            }
        }
    }
    stage('Finalize') {
        steps {
            script {
                docker.withRegistry('', // 'https://index.docker.io/'
                                    'dockerhub') {
                    docker.image('tamirfri/wog_server').push()
// Pushes an image to the registry after
// tagging it as with the tag method. 
                }
            }
        }
    }
} // stages
} // pipeline
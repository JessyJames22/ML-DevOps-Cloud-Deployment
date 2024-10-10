# **ML-DevOps-Cloud-Deployment**



## **Overview**

This project demonstrates the end-to-end automated deployment of a machine learning model using DevOps practices and containerization techniques. The goal is to streamline the deployment process while ensuring that the model runs consistently across various environments.

## **Project Details**

I developed a customer segmentation model aimed at analyzing customer data to derive insights for targeted marketing strategies. The project includes several key steps in the machine learning lifecycle, encompassing model training, containerization, and deployment.

## **Key Components**

Customer Segmentation Model: Developed using Python and various libraries like Scikit-learn to analyze and segment customer data effectively.

Flask: To create a web interface for the application.

Docker Containerization: The model has been packaged into a Docker container, allowing it to run seamlessly across different environments.

Version Control: Git was employed for tracking changes throughout the project.

## **Features**

Customer data input through a user-friendly web interface.
Segmentation of customers based on their attributes.
Easy deployment through Docker, making it accessible for anyone to run the application locally.

## **Installation Instructions**

To run this project locally, follow these steps:

### **Option 1: Clone the Repository**
1. Clone the repository:
   git clone https://github.com/JessyJames22/ML-DevOps-Cloud-Deployment.git
   
2. Navigate to the project directory:
   cd ML-DevOps-Cloud-Deployment

3. Build the Docker image:
   docker build -t customer-segmentation-app .

4. Run the Docker container:
   docker run -p 5000:80 customer-segmentation-app

5. Access the application by visiting http://localhost:5000 in your web browser.

### **Option 2: Pull the Docker Image Directly**

You can also run the application directly by pulling the Docker image from Docker Hub:
1. Pull the Docker image:
   docker pull jessyjames22/customer-segmentation-app:latest

2. Run the Docker container:
   docker run -p 5000:80 jessyjames22/customer-segmentation-app

3. Access the application in your browser at http://localhost:5000.
   

## **Future Scope**
Although I have successfully implemented the model and its deployment through Docker, I plan to extend this project to include cloud deployment using platforms like AWS or Azure. This will allow for greater scalability and accessibility of the application.

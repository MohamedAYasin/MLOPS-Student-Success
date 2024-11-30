from locust import HttpUser, TaskSet, task, between
import json

class StudentDropoutPredictionTaskSet(TaskSet):
    @task
    def predict(self):
        # Payload with specified features
        student_data = {
            "Course": 171,
            "Daytime/evening attendance\t": 1,
            "Previous qualification": 1,
            "Previous qualification (grade)": 122,
            "Admission grade": 127.3,
            "Educational special needs": 0,
            "Tuition fees up to date": 1,
            "Gender": 1,
            "Scholarship holder": 0,
            "Age at enrollment": 20,
            "Curricular units 1st sem (credited)": 0,
            "Curricular units 1st sem (enrolled)": 0,
            "Curricular units 1st sem (evaluations)": 0,
            "Curricular units 1st sem (approved)": 0,
            "Curricular units 1st sem (grade)": 0,
            "Curricular units 1st sem (without evaluations)": 0,
            "Curricular units 2nd sem (credited)": 0,
            "Curricular units 2nd sem (enrolled)": 0,
            "Curricular units 2nd sem (evaluations)": 0,
            "Curricular units 2nd sem (approved)": 0,
            "Curricular units 2nd sem (grade)": 0,
            "Curricular units 2nd sem (without evaluations)": 0
        }

        # Send POST request to the /predict endpoint
        response = self.client.post("/predict", json=student_data)
        
        # Log the response for debugging
        try:
            response_data = response.json()
            print(f"Response: {json.dumps(response_data, indent=2)}")
        except json.JSONDecodeError:
            print(f"Failed to decode response: {response.text}")

class StudentDropoutPredictionUser(HttpUser):
    tasks = [StudentDropoutPredictionTaskSet]
    wait_time = between(1, 2)  # Simulates random wait time between requests
    host = "https://student-status-check-model.onrender.com"  # Replace with your actual API host

if __name__ == "__main__":
    import os
    os.system("locust -f locust_test.py --headless -u 100 -r 10 --host https://student-status-check-model.onrender.com")
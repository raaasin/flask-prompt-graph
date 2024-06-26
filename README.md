## OtamatCNC AI Assist

OtamatCNC AI Assist is a web-based application designed to assist users in selecting the appropriate CNC machine for their needs. The application employs a chatbot interface powered by Google's Generative AI to interact with users and guide them through the CNC machine selection process.

### Features

- **User Interaction**: Users can interact with the chatbot interface to provide information about their CNC requirements.
- **Real-time Assistance**: The chatbot provides real-time responses and suggestions based on the user's inputs.
- **Dynamic Web Interface**: The web interface dynamically adjusts based on user inputs to guide them through the selection process.
- **Responsive Design**: The application is designed to be responsive and works seamlessly across different devices and screen sizes.

### Components

The OtamatCNC AI Assist project consists of the following components:

1. **Flask Backend**:

   - The Flask backend (`app.py`) serves as the server-side logic for handling user requests and rendering HTML templates.
   - It processes user inputs, constructs messages for the chatbot, and renders the appropriate HTML templates.
2. **HTML Templates**:

   - `index.html`: This template presents a form to collect user inputs such as CNC name, material, and additional criteria.
   - `result.html`: This template displays the chatbot interface where users can interact with the AI to receive recommendations and guidance.
3. **Frontend Styling**:

   - The application utilizes Bootstrap for styling, providing a clean and visually appealing user interface.
   - Custom CSS styles are used to enhance the user experience and ensure consistency across different components.
4. **Google's Generative AI**:

   - The chatbot functionality is powered by Google's Generative AI, which provides intelligent responses to user queries and inputs related to CNC machine selection.

### Getting Started

To run the OtamatCNC AI Assist project locally, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed. If not, download and install Python from the official website.
3. Install the required Python dependencies by running `pip install -r requirements.txt`.
4. Run the Flask application by executing `python app.py` in the project directory.
5. Access the application in your web browser by navigating to `http://localhost:8000`.

### Usage

1. Upon accessing the application, users are presented with a form to input details about their CNC requirements.
2. Users fill in the required information such as CNC name, material, and additional criteria.
3. After submitting the form, the application processes the inputs, constructs a message for the chatbot, and displays the chat interface.
4. Users can interact with the chatbot to receive recommendations and guidance on selecting the appropriate CNC machine.
5. The chatbot provides real-time responses and suggestions based on the user's inputs and requirements.
6. Once the user is satisfied with the recommendations, they can proceed with further actions or inquiries.

### License

This project is licensed under the [MIT License](LICENSE).
# flask-prompt-graph

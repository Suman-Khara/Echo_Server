---

# Echo Server with Delayed Response and Time Measurement

This project demonstrates a basic TCP/IP echo server-client application with a 10-second processing delay on the server side. The client measures and displays the time taken for the server to process and respond to each request. Additionally, the client shows the time at which data was sent and received. This project is an example of network programming using Python's socket module.

## Features

- **Server**:
  - Handles multiple clients simultaneously using threading.
  - Introduces a 10-second delay before responding to each client request.
  - Modifies the echoed data slightly by appending ' (processed)'.
  
- **Client**:
  - Sends data to the server and displays the time of sending.
  - Receives data from the server and displays the time of receiving.
  - Calculates and displays the time interval between sending and receiving data.
  - Can repeatedly send messages until the user decides to stop.

## Prerequisites

- Python 3.x

## Getting Started

### Setting up the Server

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Suman-Khara/Echo_Server.git
    cd Echo_Server
    ```

2. **Run the server**:
    ```sh
    python server.py
    ```

### Setting up the Client

1. **Run the client**:
    ```sh
    python client.py
    ```

### Interaction

- The client will prompt for a message to send to the server.
- After sending the message, it will display the time of sending.
- The server will process the request with a 10-second delay and send back a modified response.
- The client will display the received message, the time of receiving, and the time interval between sending and receiving.
- The server will print the message received from each client and the client's address.


---

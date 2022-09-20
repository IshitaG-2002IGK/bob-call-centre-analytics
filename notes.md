step 1:

    Ingest data
        > data can be ingested as log files, audio files, customer data etc
    
Step 2: 

    Pass it to Azure blob storage. This helps us store the calls / recordings of the calls.
    Event is recorded using event hub

Step 3:

    Perform real time analytics
    Perform scoring of the data

Step 4:

    Archive all the ingested data after the analytics have been performed
    Dynamic dashboard can be displayed
    

Detailed process:

    1. Prepare input data (this can be done using IoTHub)
    2. Create a blob storage to store your data
    3. Create a stream analytics job using console
    4. Configure job input
    5. Configure job output
    6. Define the transformation query
    7. Run IoT simulator
    8. Start the stream analytics job and check the output

Azure IoT Hub is a managed service hosted in the cloud that acts as a central message hub for communication between an IoT application and its attached devices
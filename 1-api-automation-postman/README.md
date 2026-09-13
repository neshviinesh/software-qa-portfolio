# API Automation Testing Suite (GoRest)

## Project Overview
An automated API testing architecture designed to validate a RESTful backend. This suite executes full CRUD operations (Create, Read, Update, Delete) and runs automated assertions using JavaScript (Chai). 

## Testing Strategy
* **Data Validation:** Automated scripts verify correct JSON schema formatting and exact data matching.
* **Performance SLAs:** Assertions ensure all endpoints respond in under 1000ms.
* **Negative Testing:** Explicit validation of error handling, ensuring the API correctly blocks unauthorized access (401 errors) and rejects malformed data (422 errors).
* **Automated Data Chaining:** Utilized dynamic environment variables (`{{dynamic_user_id}}`) to seamlessly chain POST, PUT, and DELETE requests into a continuous, self-sustaining loop.

## How to Run This Suite
1. Import the Collection and Environment `.json` files into Postman.
2. Acquire a free Bearer Token from gorest.co.in.
3. Paste the token into the "Current Value" of the `bearer_token` environment variable.
4. Execute the suite via the Postman Collection Runner.

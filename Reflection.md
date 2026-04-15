# Module 11 Reflection

In this module, I implemented a Calculation model using SQLAlchemy and added validation using Pydantic schemas. This assignment helped me understand how the backend layers of an application work together, especially the interaction between models, schemas, and testing.

One of the key parts of this module was designing the Calculation model with fields such as `a`, `b`, `type`, and `result`. I decided to store the result in the database because it made testing and verification easier during integration tests. I also implemented a factory method to handle different calculation types like Add, Subtract, Multiply, and Divide. This helped keep the logic organized and made the code easier to extend.

A major learning point for me was input validation using Pydantic. I added checks to ensure only valid calculation types were accepted and handled edge cases like division by zero. This made the application more robust and prevented invalid data from being processed or stored.

I also worked on writing both unit tests and integration tests. The unit tests helped me verify the correctness of individual components like validation and calculation logic. The integration tests were more challenging because they involved connecting to a PostgreSQL database and ensuring that records were inserted and retrieved correctly. This gave me a better understanding of how the application behaves in a real environment.

Another important part of this assignment was the CI/CD pipeline. I used GitHub Actions to automatically run tests whenever code was pushed. I also configured the pipeline to build a Docker image and push it to Docker Hub after successful tests. This was a valuable experience because it showed how automated testing and deployment work together in real-world development.

One challenge I faced was with Docker and container management. I encountered issues like port conflicts and container name conflicts, which required me to stop or remove existing containers before running new ones. Troubleshooting these issues helped me understand how Docker networking and container lifecycle work.

Overall, this module helped me gain practical experience with backend development concepts, including modeling, validation, testing, and deployment. I feel more confident now in building structured applications and setting up automated workflows for testing and deployment.

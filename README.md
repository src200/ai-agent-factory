# AI Agent Factory

This project is all about building personal and professional AI agents that communicate with each other, built upon autogen, a powerful framework for automating the generation of code and content. Our goal is to create a suite of AI agents that can perform a variety of tasks, ranging from simple data collection to complex decision-making processes, all while interacting seamlessly with one another.

Utilizes the [Autogen framework](https://microsoft.github.io/autogen/) for rapid development and deployment of agents, significantly reducing the time from concept to implementation.

## Getting Started

This project uses pdm for dependency management and packaging. If you're not familiar with pdm, it's a tool for Python that helps manage projects by tracking libraries, handling configuration, and packaging. Here's how to get started:

1.  **Install pdm**: If you haven't installed pdm yet, you can do so by following the instructions on the [official pdm website](https://pdm-project.org/en/latest/).

2.  **Clone the Repository**: Get a copy of the project on your local machine by cloning the repository.

        git clone https://github.com/src200/ai-agent-factory.git

3.  **Navigate to the Project Directory**: Change into the project directory.

        cd ai-agent-factory

4.  **Install Dependencies**: Use pdm to install the project dependencies. This command reads the `pyproject.toml` file and installs all necessary packages.

        pdm install

This step is crucial as it ensures that all commands and scripts are run within the context of your project's dependencies, avoiding conflicts with other projects.

6.  **Run the Project**: Now that everything is set up, you can run the joke agent using:

        pdm run agents/jokes/joke-agent.py

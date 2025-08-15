# Project Synapse: Agentic Last-Mile Coordinator

Project Synapse is a proof-of-concept autonomous AI agent designed to intelligently resolve real-time, last-mile delivery disruptions. Instead of relying on rigid, rule-based systems, Synapse uses a Large Language Model (LLM) to reason about complex problems, select the appropriate digital tools, and execute multi-step plans to find a resolution.

This project was developed as a submission for the "Agentic AI" hackathon.

---

## Key Features

The agent has been successfully tested and can autonomously handle a wide range of complex scenarios, including:

* **Merchant Issues:** Proactively managing overloaded restaurants by notifying customers, rerouting drivers to optimize their time, and suggesting alternative merchants.
* **Recipient Unavailability:** Intelligently handling situations where a recipient is not home by contacting them for instructions, suggesting safe drop-off locations, and finding nearby secure lockers.
* **Damaged Packaging Disputes:** Acting as an impartial mediator in real-time disputes between customers and drivers, guiding evidence collection, analyzing the evidence to determine fault, and executing a fair resolution (e.g., issuing refunds, exonerating drivers, and logging merchant feedback).
* **India-Specific Challenges:**
    * **Vague Addresses:** Resolving ambiguous, landmark-based addresses by requesting clarification from the customer.
    * **Fake Delivery Attempts:** Verifying disputed "failed delivery" claims by checking the driver's simulated GPS data.
    * **OTP Failures:** Providing a secure, QR-code-based alternative for delivery confirmation when OTPs fail to arrive.

---

## System Architecture

The project is built with Python and LangChain, consisting of three main components:

1.  **`main.py` (The Agent's Brain):** This is the core of the application. It initializes the Google Gemini LLM, defines the agent's persona and logic through a detailed system prompt, and uses the LangChain `AgentExecutor` to run the main reasoning loop.
2.  **`tools.py` (The Agent's Hands):** This file contains the suite of simulated digital tools the agent can use. Each tool is a Python function that mimics a real-world API call (e.g., checking traffic, notifying a customer, verifying GPS data). The LLM's ability to choose the correct tool is based on the function's name and its docstring.
3.  **`logger.py` (The Agent's Voice):** A simple utility to provide clean, color-coded, and structured output to the command line, making the agent's "chain of thought" easy to follow and presentable for a demo.

---

## Prompt Engineering Strategies

The agent's intelligence is primarily driven by a multi-layered prompt engineering strategy within the `system` prompt in `main.py`.

#### 1. Role-Playing and Persona

The prompt begins by assigning a clear identity: **"You are Synapse, an expert AI agent..."**. This immediately frames the agent's purpose and encourages it to adopt a professional, problem-solving tone in its reasoning.

#### 2. Tool Manifest with Descriptions

The prompt includes a comprehensive list of all available tools under `**Your Available Tools Are:**`. Each tool is accompanied by a concise description of its function (e.g., *"`verify_delivery_attempt(...)`: Checks a driver's GPS data..."*). This acts as an internal manual, significantly improving the agent's ability to select the correct tool for a given task.

#### 3. Directive-Based Logic (If/Then Scoping)

This is the most critical strategy used to manage the agent's complex decision-making. Under `**Key Directives:**`, a series of explicit, rule-based instructions create a logical flowchart for the agent.

* **Problem Scoping:** The prompt forces the agent to first categorize a problem before acting. For example, the **`Dispute Types`** directive compels it to differentiate between a "damaged item" dispute and a "failed delivery" dispute, ensuring it enters the correct workflow from the start.
* **Conditional Workflows:** The prompt defines clear "if this, then that" logic for specific situations. The **`Verification Workflow`** directive tells the agent exactly how to react to both a "successful" and a "failed" GPS verification, preventing it from getting confused or taking an irrelevant next step.

---

## Setup and Usage

### 1. Prerequisites

* Python 3.9+
* A Google API Key with the Generative Language API enabled.

### 2. Setup Instructions

**a. Clone the Repository:**
```bash
git clone [https://github.com/your-username/project-synapse.git](https://github.com/your-username/project-synapse.git)
cd project-synapse
```

**b. Create a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**c. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**d. Configure API Key:**
Create a file named `.env` in the root of the project directory and add your Google API key:
```
GOOGLE_API_KEY="your_api_key_here"
```

### 3. How to Run

The application is run from the command line, with the disruption scenario passed as a string argument.

**Example Command:**
```bash
python main.py "A dispute has started at the door between customer C123 and driver D456 over a spilled drink from 'The Gourmet Kitchen'. Please mediate and resolve."
```

The agent's detailed, color-coded thought process and final resolution will be printed to the console.

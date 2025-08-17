"""
CLI interface for the refactored Project Synapse agent.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import colorama
from src.core.agent import SynapseAgent
from src.utils.logger import (
    bcolors, log_coordinator, log_final_answer, log_error, log_info
)

# Initialize colorama for cross-platform colored output
colorama.init(autoreset=True)


class SynapseCLI:
    """Command-line interface for the Synapse agent."""
    
    def __init__(self):
        """Initialize the CLI with the agent."""
        try:
            log_info("Initializing Synapse agent...")
            self.agent = SynapseAgent()
            log_info("Agent initialized successfully!")
        except Exception as e:
            log_error(f"Failed to initialize agent: {e}")
            raise
    
    def run(self):
        """Run the main interactive loop."""
        print(f"{bcolors.HEADER}{bcolors.BOLD}Welcome to Project Synapse Interactive CLI (Refactored)")
        print(f"{bcolors.HEADER}You can describe a delivery disruption, and the agent will try to resolve it.")
        print(f"{bcolors.HEADER}Type 'exit' or 'quit' to end the session.")
        print(f"{bcolors.HEADER}Type 'help' for available commands.\n")

        while True:
            try:
                # Get user input
                user_input = input(f"{bcolors.BOLD}Enter a disruption scenario: {bcolors.ENDC}")

                # Handle commands
                if user_input.lower() in ["exit", "quit"]:
                    print(f"{bcolors.WARNING}Ending session. Goodbye!")
                    break
                
                if user_input.lower() == "help":
                    self._show_help()
                    continue

                # Handle empty input
                if not user_input.strip():
                    continue

                # Process the scenario
                log_coordinator("Received new disruption. Handing over to the agent...")
                
                result = self.agent.process_scenario(user_input)
                log_final_answer(result)
                
                log_coordinator("Agent has completed its task and is ready for the next scenario.\n")

            except KeyboardInterrupt:
                print(f"\n{bcolors.WARNING}Session interrupted. Goodbye!")
                break
            except Exception as e:
                log_error(f"An unexpected error occurred: {e}")

    def _show_help(self):
        """Show help information."""
        print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}Available Commands:")
        print(f"{bcolors.OKCYAN}  help  - Show this help message")
        print(f"{bcolors.OKCYAN}  exit  - Exit the application")
        print(f"{bcolors.OKCYAN}  quit  - Exit the application")
        print(f"\n{bcolors.OKCYAN}Example Scenarios:")
        print(f"{bcolors.OKCYAN}  'Driver reports Pizza Palace is overloaded with 45-minute wait'")
        print(f"{bcolors.OKCYAN}  'Customer complains their food arrived spilled and damaged'")
        print(f"{bcolors.OKCYAN}  'Driver cannot find the address: Room 301, Near big temple'")
        print(f"{bcolors.OKCYAN}  'Customer says driver never arrived but marked as failed delivery'")
        print()


def main():
    """Main entry point for the CLI application."""
    try:
        cli = SynapseCLI()
        cli.run()
    except Exception as e:
        log_error(f"Failed to start application: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

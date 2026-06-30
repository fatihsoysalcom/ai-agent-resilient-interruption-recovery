import json
import time
import random
import os
import sys

# Configuration for the agent and simulation
STATE_FILE = "agent_state.json"
TOTAL_ITEMS = 10 # Total number of tasks/items for the agent to process
SIMULATED_INTERRUPT_CHANCE = 0.3 # 30% chance to simulate an interruption after each item

class AIAgent:
    def __init__(self, agent_id="Agent001"):
        self.agent_id = agent_id
        self.items_to_process = [f"Task_{i+1}" for i in range(TOTAL_ITEMS)]
        self.processed_items = []
        self.current_item_index = 0
        self.load_state() # Attempt to load previous state upon initialization

    def _save_state(self):
        """Saves the agent's current state to a file. This is crucial for recovery."""
        state = {
            "agent_id": self.agent_id,
            "items_to_process": self.items_to_process,
            "processed_items": self.processed_items,
            "current_item_index": self.current_item_index
        }
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=4)
        print(f"[{self.agent_id}] State saved. Processed: {len(self.processed_items)}, Next index: {self.current_item_index}")

    def load_state(self):
        """Loads the agent's state from a file if it exists, enabling resumption."""
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    state = json.load(f)
                self.agent_id = state.get("agent_id", self.agent_id)
                self.items_to_process = state.get("items_to_process", self.items_to_process)
                self.processed_items = state.get("processed_items", [])
                self.current_item_index = state.get("current_item_index", 0)
                print(f"[{self.agent_id}] State loaded from {STATE_FILE}. Resuming from item index {self.current_item_index}.")
            except json.JSONDecodeError:
                print(f"[{self.agent_id}] Corrupted state file found. Starting new task.")
                os.remove(STATE_FILE) # Remove corrupted file
        else:
            print(f"[{self.agent_id}] No saved state found. Starting new task.")

    def run(self):
        """Runs the agent's task, processing items and simulating interruptions."""
        print(f"[{self.agent_id}] Agent started. Total items: {len(self.items_to_process)}")

        # Loop continues from the last saved index, demonstrating resilience
        for i in range(self.current_item_index, len(self.items_to_process)):
            item = self.items_to_process[i]
            print(f"[{self.agent_id}] Processing item: {item}...")
            time.sleep(random.uniform(0.5, 1.5)) # Simulate work being done

            self.processed_items.append(item)
            self.current_item_index = i + 1 # Update index for the *next* item to process
            
            self._save_state() # Save state after each successful step to ensure progress is not lost

            # Simulate an interruption (e.g., power outage, software crash)
            if random.random() < SIMULATED_INTERRUPT_CHANCE and self.current_item_index < len(self.items_to_process):
                print(f"[{self.agent_id}] --- SIMULATING INTERRUPTION! Agent crashed. ---\n")
                sys.exit(1) # The agent process terminates abruptly

        print(f"\n[{self.agent_id}] All items processed: {self.processed_items}")
        # Clean up state file after successful completion of the entire task
        if os.path.exists(STATE_FILE):
            os.remove(STATE_FILE)
            print(f"[{self.agent_id}] State file {STATE_FILE} removed upon completion.")

if __name__ == "__main__":
    agent = AIAgent()
    try:
        agent.run()
    except SystemExit:
        # Catch SystemExit to allow for a clean exit message, though the program terminates.
        pass
    except Exception as e:
        print(f"[{agent.agent_id}] An unexpected error occurred: {e}")
        # In a real agent, you might want to save state even on unexpected errors
        # if the agent can recover or needs to log its last state before failure.

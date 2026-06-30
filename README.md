# AI Agent Resilient Interruption Recovery

This example demonstrates how a long-lived AI agent can be resilient to interruptions by persisting its state. The agent processes a series of tasks, saving its progress after each step. If the program is interrupted (simulated by a random crash), it can load its last saved state upon restart and continue processing from where it left off, ensuring no loss of completed work.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run it from your terminal: `python main.py`.
3. Run it multiple times. Observe how it either completes all tasks or crashes and then resumes from the last saved point on subsequent runs.

## Original Article

This example accompanies the Turkish article: [Uzun Soluklu Yapay Zeka Ajanları Kesintilerle Nasıl Başa Çıkıyor?](https://fatihsoysal.com/blog/uzun-soluklu-yapay-zeka-ajanlari-kesintilerle-nasil-basa-cikiyor/).

## License

MIT — see [LICENSE](LICENSE).

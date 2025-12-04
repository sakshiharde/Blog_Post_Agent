from agent import ResearchAgent
import sys

def main():
    # Check if topic is given
    if len(sys.argv) < 2:
        print("❌ Please provide a research topic.\n")
        print("Example:")
        print("python main.py \"Google AI Vision Research\"")
        return

    topic = sys.argv[1]
    print(f"\n🚀 Starting Research Agent for topic: {topic}\n")

    agent = ResearchAgent()

    # Run agent
    blog_output = agent.run(topic)

    print("\n==============================")
    print("📘 FINAL BLOG OUTPUT")
    print("==============================\n")
    print(blog_output)
    print("\n==============================")

if __name__ == "__main__":
    main()

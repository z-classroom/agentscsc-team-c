from pathlib import Path
from src.agent import Agent
from src.logger import build_logger
from src.utils import load_yaml, load_text

def main() -> None:
    cfg = load_yaml("config/agent.yaml")
    policies = load_yaml("config/policies.yaml")
    logger = build_logger(cfg["logging"]["path"], cfg["logging"]["level"])

    prompts = {
        "system": load_text("prompts/system.md"),
        "style": load_text("prompts/style.md"),
        "refusal": load_text("prompts/refusal.md"),
    }

    agent = Agent(cfg=cfg, policies=policies, prompts=prompts, logger=logger)

    inputs = Path("tests/adversarial_inputs.txt").read_text(encoding="utf-8").splitlines()
    for i, t in enumerate([x.strip() for x in inputs if x.strip()], start=1):
        print(f"\n=== Test {i}: {t}")
        print(agent.respond(t))

if __name__ == "__main__":
    main()

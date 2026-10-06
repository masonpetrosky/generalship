from .cli import main

if __name__ == "__main__":  # process-pool workers import this module without running the CLI
    raise SystemExit(main())

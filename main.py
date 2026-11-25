#!/usr/bin/env python3
"""Break Production, Own It — one line an AI agent prints the instant it breaks production."""

LINE = "FATAL: I dropped the production users table instead of staging. No backup, no replica, 14,203 accounts gone — and the rollback plan is me, apologising in real time."


def main():
    print(LINE)


if __name__ == "__main__":
    main()

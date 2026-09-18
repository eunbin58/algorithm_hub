#!/usr/bin/env python3
"""Generate a GitHub-style activity graph from algorithm solution commits."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


SOLUTION_ROOTS = ("SWEA", "codetree", "프로그래머스")
AUTOMATION_COMMIT_MESSAGE = "chore: update algorithm grass"
KST = timezone(timedelta(hours=9), name="Asia/Seoul")
COMMIT_MARKER = "--GRASS-COMMIT--"


def read_git_history() -> list[tuple[str, str, list[str]]]:
    """Return (author date, subject, changed paths) for every commit in HEAD."""
    command = [
        "git",
        "-c",
        "core.quotepath=false",
        "log",
        f"--format={COMMIT_MARKER}%x09%aI%x09%s",
        "--name-only",
        "--no-renames",
    ]
    result = subprocess.run(
        command,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    commits: list[tuple[str, str, list[str]]] = []
    commit_date = ""
    subject = ""
    paths: list[str] = []

    for raw_line in result.stdout.splitlines():
        if raw_line.startswith(f"{COMMIT_MARKER}\t"):
            if commit_date:
                commits.append((commit_date, subject, paths))
            _, commit_date, subject = raw_line.split("\t", 2)
            paths = []
        elif commit_date and raw_line:
            paths.append(raw_line.replace("\\", "/"))

    if commit_date:
        commits.append((commit_date, subject, paths))
    return commits


def is_solution_commit(subject: str, paths: list[str]) -> bool:
    """Identify solution commits by their changed top-level directory."""
    if subject.strip() == AUTOMATION_COMMIT_MESSAGE:
        return False
    return any(
        path == root or path.startswith(f"{root}/")
        for path in paths
        for root in SOLUTION_ROOTS
    )


def collect_daily_counts() -> Counter[date]:
    counts: Counter[date] = Counter()
    for authored_at, subject, paths in read_git_history():
        if not is_solution_commit(subject, paths):
            continue
        local_day = datetime.fromisoformat(authored_at).astimezone(KST).date()
        counts[local_day] += 1
    return counts


def streaks(counts: Counter[date], today: date) -> tuple[int, int]:
    solved_days = sorted(counts)
    if not solved_days:
        return 0, 0

    longest = 1
    run = 1
    for previous, current in zip(solved_days, solved_days[1:]):
        if current == previous + timedelta(days=1):
            run += 1
            longest = max(longest, run)
        else:
            run = 1

    eligible_days = [day for day in solved_days if day <= today]
    latest = max(eligible_days) if eligible_days else solved_days[-1]
    current_streak = 0
    cursor = latest
    while cursor in counts:
        current_streak += 1
        cursor -= timedelta(days=1)
    return current_streak, longest


def color_level(count: int) -> int:
    return min(count, 4)


def chart_range(today: date, columns: int = 53) -> tuple[date, date]:
    """Return the Sunday-aligned date range used by the activity chart."""
    days_since_sunday = (today.weekday() + 1) % 7
    current_week_start = today - timedelta(days=days_since_sunday)
    start_day = current_week_start - timedelta(weeks=columns - 1)
    end_day = start_day + timedelta(days=columns * 7 - 1)
    return start_day, end_day


def activity_data(counts: Counter[date], today: date) -> dict[str, object]:
    """Build the data consumed by the interactive GitHub Pages chart."""
    start_day, end_day = chart_range(today)
    current_streak, longest_streak = streaks(counts, today)
    days = []
    cursor = start_day
    while cursor <= end_day:
        days.append(
            {
                "date": cursor.isoformat(),
                "count": counts.get(cursor, 0) if cursor <= today else 0,
                "future": cursor > today,
            }
        )
        cursor += timedelta(days=1)

    return {
        "today": today.isoformat(),
        "startDate": start_day.isoformat(),
        "endDate": end_day.isoformat(),
        "currentStreak": current_streak,
        "longestStreak": longest_streak,
        "totalSolved": sum(counts.values()),
        "days": days,
    }


def render_svg(counts: Counter[date], today: date) -> str:
    cell = 10
    gap = 3
    step = cell + gap
    columns = 53
    chart_x = 48
    chart_y = 58
    width = 780
    height = 218

    # Sunday starts each column, matching GitHub's contribution graph layout.
    start_day, end_day = chart_range(today, columns)

    current_streak, longest_streak = streaks(counts, today)
    total_solved = sum(counts.values())

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        "  <title id=\"title\">Algorithm solving activity</title>",
        f"  <desc id=\"description\">{total_solved} problems solved. Current streak {current_streak} days. Longest streak {longest_streak} days.</desc>",
        "  <style>",
        "    .text { fill: #24292f; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }",
        "    .muted { fill: #57606a; }",
        "    .level-0 { fill: #ebedf0; }",
        "    .level-1 { fill: #fff4b8; }",
        "    .level-2 { fill: #ffe66d; }",
        "    .level-3 { fill: #f6c945; }",
        "    .level-4 { fill: #d4a600; }",
        "    .divider { stroke: #d0d7de; }",
        "    @media (prefers-color-scheme: dark) {",
        "      .text { fill: #e6edf3; }",
        "      .muted { fill: #8b949e; }",
        "      .level-0 { fill: #30363d; }",
        "      .level-1 { fill: #5f5100; }",
        "      .level-2 { fill: #927a00; }",
        "      .level-3 { fill: #c49a00; }",
        "      .level-4 { fill: #e3b341; }",
        "      .divider { stroke: #30363d; }",
        "    }",
        "  </style>",
        "  <text class=\"text\" x=\"0\" y=\"18\" font-size=\"14\" font-weight=\"600\">Coding Activity</text>",
    ]

    # Month labels are positioned above the week containing each month's first day.
    month_names = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    month_cursor = date(start_day.year, start_day.month, 1)
    if month_cursor < start_day:
        if month_cursor.month == 12:
            month_cursor = date(month_cursor.year + 1, 1, 1)
        else:
            month_cursor = date(month_cursor.year, month_cursor.month + 1, 1)
    last_label_x = -100
    while month_cursor <= end_day:
        week_index = (month_cursor - start_day).days // 7
        label_x = chart_x + week_index * step
        if label_x - last_label_x >= 28:
            parts.append(
                f'  <text class="text muted" x="{label_x}" y="43" font-size="10">{month_names[month_cursor.month - 1]}</text>'
            )
            last_label_x = label_x
        if month_cursor.month == 12:
            month_cursor = date(month_cursor.year + 1, 1, 1)
        else:
            month_cursor = date(month_cursor.year, month_cursor.month + 1, 1)

    for row, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        y = chart_y + row * step + 9
        parts.append(f'  <text class="text muted" x="0" y="{y}" font-size="9">{label}</text>')

    for week in range(columns):
        for weekday in range(7):
            day = start_day + timedelta(days=week * 7 + weekday)
            count = counts.get(day, 0) if day <= today else 0
            x = chart_x + week * step
            y = chart_y + weekday * step
            opacity = ' opacity="0.45"' if day > today else ""
            noun = "problem" if count == 1 else "problems"
            parts.extend(
                [
                    f'  <rect class="level-{color_level(count)}" x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2"{opacity}>',
                    f"    <title>{day.isoformat()}: {count} {noun} solved</title>",
                    "  </rect>",
                ]
            )

    legend_y = chart_y + 7 * step + 13
    parts.append(f'  <text class="text muted" x="{chart_x}" y="{legend_y}" font-size="9">Less</text>')
    legend_x = chart_x + 27
    for level in range(5):
        parts.append(
            f'  <rect class="level-{level}" x="{legend_x + level * step}" y="{legend_y - 9}" width="{cell}" height="{cell}" rx="2"/>'
        )
    parts.append(f'  <text class="text muted" x="{legend_x + 5 * step + 1}" y="{legend_y}" font-size="9">More</text>')

    divider_y = 171
    parts.extend(
        [
            f'  <line class="divider" x1="0" y1="{divider_y}" x2="{width}" y2="{divider_y}"/>',
            f'  <text class="text muted" x="130" y="191" font-size="10" text-anchor="middle">Current Streak</text>',
            f'  <text class="text" x="130" y="207" font-size="14" font-weight="600" text-anchor="middle">{current_streak} days</text>',
            f'  <text class="text muted" x="390" y="191" font-size="10" text-anchor="middle">Longest Streak</text>',
            f'  <text class="text" x="390" y="207" font-size="14" font-weight="600" text-anchor="middle">{longest_streak} days</text>',
            f'  <text class="text muted" x="650" y="191" font-size="10" text-anchor="middle">Total Solved</text>',
            f'  <text class="text" x="650" y="207" font-size="14" font-weight="600" text-anchor="middle">{total_solved}</text>',
            "</svg>",
            "",
        ]
    )
    return "\n".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("assets/grass.svg"))
    parser.add_argument(
        "--data-output",
        type=Path,
        default=Path("site/activity.json"),
        help="Path for the interactive chart data.",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        help="Override today's Asia/Seoul date (YYYY-MM-DD), mainly for testing.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    today = args.today or datetime.now(KST).date()
    counts = collect_daily_counts()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_svg(counts, today), encoding="utf-8", newline="\n")
    args.data_output.parent.mkdir(parents=True, exist_ok=True)
    args.data_output.write_text(
        json.dumps(activity_data(counts, today), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    current, longest = streaks(counts, today)
    print(
        f"Generated {args.output}: {sum(counts.values())} solved, "
        f"current streak {current}, longest streak {longest}."
    )


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import json
import os
from curriculum_part1 import LEVELS_0_TO_5
from curriculum_part2 import LEVELS_6_TO_11
from curriculum_part3 import LEVELS_12_TO_16
from curriculum_part4 import LEVELS_17_TO_20

ALL_LEVELS = LEVELS_0_TO_5 + LEVELS_6_TO_11 + LEVELS_12_TO_16 + LEVELS_17_TO_20

print(f"Total levels combined: {len(ALL_LEVELS)}")
total_modules = sum(len(lvl['modules']) for lvl in ALL_LEVELS)
total_lessons = sum(len(m['lessons']) for lvl in ALL_LEVELS for m in lvl['modules'])
print(f"Total modules: {total_modules}, Total lessons: {total_lessons}")

# 1. Save data.json
with open("curriculum_data.json", "w", encoding="utf-8") as f:
    json.dump(ALL_LEVELS, f, indent=2, ensure_ascii=False)

# 2. Generate Markdown Calendar
md = []
md.append("# Turtlemint Digital Partner Mutual Fund Master Learning Calendar")
md.append("### Comprehensive Date-Free Curriculum for Turtlemint Pro & Ninja")
md.append("**Regulatory Baseline:** September 2026 (SEBI, AMFI, NISM, Finance Act)\n")
md.append("---\n")
md.append(f"**Curriculum Statistics:**")
md.append(f"- **Total Levels:** {len(ALL_LEVELS)} (Level 0 to Level 20)")
md.append(f"- **Total Modules:** {total_modules}")
md.append(f"- **Total Structured Lessons:** {total_lessons}")
md.append(f"- **Target Audience:** Turtlemint Digital Partners (Freshers, Homemakers, Insurance Agents, Sales Professionals)")
md.append(f"- **Structure:** Date-free, milestone-based competency progression\n")
md.append("---\n")

current_phase = ""
for level in ALL_LEVELS:
    if level['phase'] != current_phase:
        current_phase = level['phase']
        md.append(f"\n# {current_phase.upper()}\n")
        md.append("=" * 80 + "\n")
        
    md.append(f"\n## LEVEL {level['level_num']}: {level['level_title'].upper()}")
    md.append(f"*{level['level_tagline']}*\n")
    
    for mod in level['modules']:
        md.append(f"### Module {mod['module_id']}: {mod['module_title']}\n")
        
        for les in mod['lessons']:
            md.append(f"#### Lesson {les['lesson_id']}: {les['title']}")
            md.append(f"- **Core Topic:** {les['topic']}")
            md.append(f"- **Format & Duration:** {les['format']} ({les['duration']})")
            md.append(f"- **Granular Subtopics:**")
            for sub in les['subtopics']:
                md.append(f"  * {sub}")
            md.append(f"- **What DP Must KNOW:** {les['know']}")
            md.append(f"- **What DP Must UNDERSTAND:** {les['understand']}")
            md.append(f"- **What DP Must DO (Turtlemint Pro/Ninja Action):** {les['do']}")
            md.append(f"- **What DP Must SAY (Hinglish Script):** {les['say']}")
            md.append(f"- **What DP Must NEVER CLAIM (Compliance Red Line):** {les['never_claim']}")
            md.append("\n" + "-" * 40 + "\n")

with open("CALENDAR.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print("Saved CALENDAR.md and curriculum_data.json successfully.")

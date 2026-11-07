#!/usr/bin/env python3
"""Correct the regenerated My Research Frameworks TXT and VTT transcripts.

Preserves every VTT timestamp and cue boundary. Does not invent missing speech.
Use --dry-run to inspect changes; creates .bak backups on first write.
"""
import argparse
from pathlib import Path
import re
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--dry-run', action='store_true')
parser.add_argument('files', nargs='*', default=[
    'my-research-frameworks.txt', 'my-research-frameworks.vtt'])
args = parser.parse_args()

# Order matters: specific phrases precede shorter replacements.
fixes = [
    (r'\bRelativistic Scalar Vector Entropy Plenum\b', 'Relativistic Scalar-Vector-Entropy Plenum'),
    (r'\bconstrained first account\b', 'constraint-first account'),
    (r'\bvictor flow math BFV\b', 'vector flow v'),
    (r'\bentropy\s+self\b', 'entropy S'),
    (r'\bSpherePOP\b', 'Spherepop'),
    (r'\bcommitted stake\b', 'committed state'),
    (r'\b8-byte memory cell\b', 'eight-byte memory-cell'),
    (r'\bforgetting, forgetting,', 'forgetting,'),
    (r'\binteract to constrain relationships\b', 'interact through constrained relationships'),
    (r'\bthe reversibility gate\b', 'the Reversibility Gate'),
    (r'\bthe latency of evidence\b', 'the Latency of Evidence'),
    (r'\bADMISSIBILITY AND IRREVERSIBILITY\b', 'Admissibility and Irreversibility'),
    (r'\bADMISSIBILITY is\b', 'Admissibility is'),
    (r'\boperations include pop, refuse, bind, transform, verify, and collapse\b',
     'operations include POP, REFUSE, BIND, TRANSFORM, VERIFY, and COLLAPSE'),
]

def fix_line(line):
    for pattern, replacement in fixes:
        line = re.sub(pattern, replacement, line)
    return line

for name in args.files:
    path = Path(name)
    if not path.is_file():
        print(f'MISSING: {path}')
        continue
    source = path.read_text(encoding='utf-8')
    # Work line-by-line so no correction can accidentally merge or shift cues.
    corrected = ''.join(fix_line(line) for line in source.splitlines(keepends=True))
    if path.suffix.lower() == '.vtt':
        stamp = r'(?m)^\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}\.\d{3}$'
        assert re.findall(stamp, source) == re.findall(stamp, corrected), 'VTT timing changed!'
    if corrected == source:
        print(f'{path}: unchanged')
        continue
    changes = [(i, a.rstrip(), b.rstrip()) for i, (a, b) in enumerate(
        zip(source.splitlines(), corrected.splitlines()), 1) if a != b]
    for lineno, old, new in changes:
        print(f'{path}:{lineno}:\n  - {old}\n  + {new}')
    if args.dry_run:
        print(f'{path}: {len(changes)} changed lines (dry run)')
    else:
        backup = path.with_name(path.name + '.bak')
        if not backup.exists():
            shutil.copy2(path, backup)
        path.write_text(corrected, encoding='utf-8')
        print(f'{path}: corrected ({len(changes)} lines); backup: {backup}')



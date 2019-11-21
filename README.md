# CTF Levels

A collection of [CTF](https://ctftime.org/ctf-wtf/) levels.

## Navigation

* [Usage](#usage)
* [Definitions](#definitions)
  * [Frontmatter](#frontmatter)
  * [Description](#description)
  * [Hint](#hint)
  * [Instructions](#instructions-optional)
  * [Attachments](#attachments-wherever-necessary)
  * [Solution](#solution-optional)
* [Examples](#examples)

## Usage

These levels are designed for [Facebook's CTF Hosting Server](https://github.com/facebook/fbctf).

```bash
python main.py -h
```

```
usage: main.py [-h] games [games ...]

Generate files for CTF in FBCTF Format

positional arguments:
  games       game folders

optional arguments:
  -h, --help  show this help message and exit
```

## Definitions

Create a new game,

```bash
mkdir games
mkdir games/game_name
mkdir games/game_name/levels
cd games/game_name/levels/
```

Create a new [level](#level),

```bash
mkdir level_name
touch README.md
```

>   #### Level
>
>   A level is a task in the Capture the Flag game.

Define `README.md` based on the following format

### Frontmatter

```
---
title: Level Title
country: Country
flag : Flag Text (convention : CTF{something})
points: points awarded for capture
bonus: points awarded as max(bonus - decrement * (number of times flag was captured), 0)
decrement: see bonus
penalty: points taken away if hint was requested
tag: something describing the
---
```

### Description

<code>
```
<br/>Describe the level, giving the participants some clues towards the approach they must follow so as to capture the flag.
This is raw text. No markdown allowed.<br/>
```
</code>

### Instructions (optional)

Provide instructions on how to generate the level attachments if necessary.

### Hint

<code>
```
<br/>Provide the participants with a hint. This message is shown once they 'purchase' a hint.
This is raw text. No markdown allowed.<br/>
```
</code>

### Attachments (wherever necessary)

```markdown
*   [relative_path_to_file](relative_path_to_file)
*   [relative_path_to_directory](relative_path_to_directory)
```

>   In the case where the attachment must be a git repo and you wish to track its changes, add it as a submodule of the main repo.

### Solution (optional)

Explain the solution.

## Examples

Checkout [`games/`](games/) for some levels.
